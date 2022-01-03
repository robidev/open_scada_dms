#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename

import string
import socket
import json
import subprocess
import time
import sys
import os
import logging

import pymongo
import redis

async_mode = None #"threading" #"eventlet" None
thread = None
tick = 0.001
mongoclient = None
logger = None

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
socketio = SocketIO(app, async_mode=async_mode)

#http calls
@app.route('/', methods = ['GET'])
def index():
  return render_template('index.html', async_mode=socketio.async_mode)


# web UI: event when client connects
@socketio.on('connect', namespace='')
def test_connect():
  global thread
  if thread is None:
    thread = socketio.start_background_task(target=worker)

# web UI: refresh page
@socketio.on('get_page_data', namespace='')
def get_page_data(data):
  emit('page_reload', {'data': ""})


#synchronous read call, returns dict with sub-elements
@socketio.on('read_value', namespace='')
def read_value(data):
  logger.debug("read value:" + str(data['id'])  )
  return -1


# write call, only supports DA elements
@socketio.on('write_value', namespace='')
def write_value(data):
  return "general error"


# register datapoint for polling/reporting
@socketio.on('register_datapoint', namespace='')
def register_datapoint(data):
  logger.debug("register datapoint:" + str(data) )

# register datapoint for polling/reporting
@socketio.on('unregister_datapoint', namespace='')
def register_datapoint(data):
  logger.debug("unregister datapoint:" + str(data) )


# web UI: load datamodels for registered IED's
@socketio.on('register_datapoint_finished', namespace='')
def register_datapoint_finished(data):
  logger.info("register datapoint finished")

# load svg schema data
def query_schema(x1,y1,x2,y2,z):
  global mongoclient
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
  db = mongoclient.scada

  cursor = db.schema_objects.find(
    {
      '$and':[{
        '$and':[
          { 
            '$or': [ 
              {'x':  {'$gte':x1 }},  
              {'x2': {'$gte':x1 }}, 
            ]
          },{
            '$or':[
              {'x':  {'$lte':x2 }},
              {'x2': {'$lte':x2 }} 
            ] 
          }
        ]
      },{
        '$and':[
          { 
            '$or': [ 
              {'y':  {'$gte':y1 }},  
              {'y2': {'$gte':y1 }}, 
            ]
          },{
            '$or':[
              {'y':  {'$lte':y2 }},
              {'y2': {'$lte':y2 }} 
            ] 
          }
        ]
      }]
    } 
  )

  data = []
  for object in cursor:
    svg = db.svg_templates.find_one({"name":object["svg"]})
    object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + string.Template(svg["svg"]).substitute(object['datapoints']) + "</svg>"
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")
    data.append(object)

  return data


@socketio.on('get_svg_for_schema', namespace='')
def get_svg_for_schema(data):
  logger.info("x: %i, y: %i, x2: %i, y2: %i, z: %i", data['x'],data['y'],data['x2'],data['y2'],data['z'])
  # query database for svg objects, based on coordinates
  in_view_new = query_schema(data['x'], data['y'], data['x2'], data['y2'], data['z'])

  # remove old items that should not be in view anymore
  for item in data['in_view']:
    if not any(d['id'] == item for d in in_view_new):
      socketio.emit("svg_object_remove_from_schema",item)

  # add new items that should be in view
  for item in in_view_new:
    if not item['id'] in data['in_view']:
      socketio.emit("svg_object_add_to_schema",item )
  

# load svg gis data
def query_gis_geojson(w,n,e,s,z):
  global mongoclient
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
  db = mongoclient.scada
  cursor = db.gis_objects.find({ 
    "geometry": {
     "$geoIntersects": {
        "$geometry": {
           "type": "Polygon" ,
           "coordinates": [ [ [w,n],[e,n],[e,s],[w,s],[w,n] ] ] # square
        }
      }
    }
  })
  data = []
  for item in cursor:
    item['_id'] = str(item['_id'])
    data.append(item)
  return data


# load svg gis data
def query_gis_svg(w,n,e,s,z):
  global mongoclient
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
  try:
    db = mongoclient.scada
    cursor = db.schema_objects.find({ 
      "location": {
      "$geoIntersects": {
          "$geometry": {
            "type": "Polygon" ,
            "coordinates": [ [ [w,n],[e,n],[e,s],[w,s],[w,n] ] ] # square
          }
        }
      }
    })

    data = []

    for object in cursor:
      svg = db.svg_templates.find_one({"name":object["svg"]})
      object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + string.Template(svg["svg"]).substitute(object['datapoints']) + "</svg>"
      object["id"] = "_" + str(object["_id"])
      object.pop("_id")
      data.append(object)
  except Exception as inst:
    return None

  return data


@socketio.on('get_svg_for_gis', namespace='')
def get_svg_for_gis(data):
  # query database for svg objects, based on coordinates
  in_view_new = query_gis_svg(data['w'], data['n'], data['e'], data['s'], data['z'])
  if in_view_new == None:
    return
  # remove old items that should not be in view anymore
  for item in data['in_view']:
    if not any(d['id'] == item for d in in_view_new):
      socketio.emit("svg_object_remove_from_gis",item)

  # add new items that should be in view
  for item in in_view_new:
    if not item['id'] in data['in_view']:
      socketio.emit("svg_object_add_to_gis",item )

  in_view_geojson = query_gis_geojson(data['w'], data['n'], data['e'], data['s'], data['z'])
  geojson = [{"type": "FeatureCollection", "features": in_view_geojson }]
  socketio.emit("geojson_object_add_to_gis",geojson )


# callbacks from libiec61850client
# called by client.poll
def readvaluecallback(key,data):
  logger.debug("callback: %s - %s" % (key,data))
  socketio.emit("svg_value_update_event_on_schema",{ 'element' : key, 'data' : data })


#background thread
def worker():
  socketio.sleep(tick)
  logger.info("worker treat started")
  while True:
    socketio.sleep(1)
    #logger.info("values polled")


if __name__ == '__main__':
  logger = logging.getLogger('webserver')
  logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)

  logger.info("started")

  mongoclient = pymongo.MongoClient('localhost', 27017, username="aaa",password="bbb", authSource='scada', authMechanism='SCRAM-SHA-256')
  rt_db = redis.Redis(host='localhost', port=6379, password="yourpassword")

  socketio.run(app,host="0.0.0.0")


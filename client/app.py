#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename

import string
import logging

import pymongo
import redis

async_mode = None #"threading" #"eventlet" None
thread = None
tick = 0.001
mongoclient = None
logger = None
clients = {}
rt_pubsub = None
redis_event_thread = None
rt_db = None

poll_datapoint = {}

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
socketio = SocketIO(app, async_mode=async_mode)


################################################

def add_listener(point):
  global rt_db
  #check redis for point,
  if rt_db.exists("data".point) > 0:
    # we allready get all redis data update events, so nothing to be done
    # possibly add psub for point in the future to limit amount of events
    # and/or increase reference count for subscribed data points
    return "rt"

  #else subscribe for mongodb poll(keep reference count)
  if not point in poll_datapoint:
    poll_datapoint[point] = {}
    poll_datapoint[point]['refCount'] = 0
    poll_datapoint[point]['value'] = None

  poll_datapoint[point]['refCount'] += 1

  return "poll"


def remove_listener(point):
  #check redis for point
  if rt_db.exists("data".point) > 0:
    # possibly remove psub for point
    # and/or decrease reference count
    return "rt"

  #else unsubscribe for mongodb poll(keep reference count)
  if point in poll_datapoint:
    if poll_datapoint[point] > 0:
      poll_datapoint[point]['refCount'] -= 1

  return "poll"


def redis_dataUpdate(msg):
  global rt_db
  key = msg['channel'][15:]
  data = rt_db.get(key)
  print("update",key[5:-6], data)
  updateDataPoint("iec60870://" + str(key),str(data)) # emit to clients


def poll_dataUpdate(point, data):
  updateDataPoint(point,data) # emit to clients

###############################################

@socketio.on('schema_addItems', namespace='')
def add_to_schema_database():
  global mongoclient
  db = mongoclient.scada
  db.schema_objects.insert_one({})
  return

@socketio.on('schema_editedItems', namespace='')
def update_schema_database():
  global mongoclient
  db = mongoclient.scada
  return

@socketio.on('schema_removeItems', namespace='')
def remove_from_schema_database():
  global mongoclient
  db = mongoclient.scada
  return

@socketio.on('gis_addItems', namespace='')
def add_to_gis_database():
  global mongoclient
  db = mongoclient.scada
  db.gis_objects.insert_one({})
  return

@socketio.on('gis_editedItems', namespace='')
def update_gis_database():
  global mongoclient
  db = mongoclient.scada
  return

@socketio.on('gis_removeItems', namespace='')
def remove_from_gis_database():
  global mongoclient
  db = mongoclient.scada
  return

@socketio.on('svg_addTemplate', namespace='')
def svg_addTemplate(template):
  global mongoclient
  db = mongoclient.scada
  # TODO: prevent nosql injection
  db.svg_templates.insert_one(template)
  return

###############################################

#http calls
@app.route('/', methods = ['GET'])
def index():
  return render_template('index.html', async_mode=socketio.async_mode)


# web UI: event when client connects
@socketio.on('connect', namespace='')
def connect(data):
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
  client = request.sid
  print("client:" + client)
  logger.info("register datapoint:" + str(data) )
  if not client in clients:
    clients[client] = []
  
  add_listener(data)
  # add to client list
  clients[client].append(data)
  ##########
  # send data update, for testing only!
  #updateDataPoint(data,"test")

def updateDataPoint(point, data_l):
  recepients = []
  # send data to all subscribed clients
  for client in clients:
    if point in clients[client]:
      recepients.append(client)
  socketio.emit("updateDataPoint",data={'d':data_l},to=recepients)


# register datapoint for polling/reporting
@socketio.on('unregister_datapoint', namespace='')
def unregister_datapoint(data):
  print("client:" + request.sid)
  client = request.sid
  logger.info("unregister datapoint:" + str(data) )
  if not client in clients:
    clients[client] = []

  if data in clients[client]:
    remove_listener(data)
    # remove item from client list
    clients[client].remove(data)

@socketio.on('disconnect')
def disconnect():
  print('Client disconnected: ' + request.sid )
  client = request.sid
  if client in clients:
    del clients[client]


# web UI: load datamodels for registered IED's
@socketio.on('register_datapoint_finished', namespace='')
def register_datapoint_finished(data):
  print(request.sid)
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


@socketio.on('get_svg_for_schema')#, namespace='')
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
  global mongoclient
  global rt_pubsub
  socketio.sleep(tick)
  logger.info("worker treat started")
  while True:
    socketio.sleep(1)
    for point in poll_datapoint:
      if poll_datapoint[point]['refCount'] > 0: # check if currently a client wants this datapoint
        # query mongodb for possible update
        db = mongoclient.scada
        data = db.data_timeseries.find({'id':point}).sort([('timestamp', -1)]).limit(1) # find newest value
        if data:
          value = data['value']
        else: # if value is not in mongodb, just give up (for now)
          value = 'UNKNOWN'

        # check if data changed since last check
        oldValue = poll_datapoint[point]['value']
        if oldValue != value: # update value, only if value was changed
          poll_datapoint[point]['value'] = value
          poll_dataUpdate(point, value)    
    logger.info("values polled")


if __name__ == '__main__':
  logger = logging.getLogger('webserver')
  logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)

  logger.info("started")

  mongoclient = pymongo.MongoClient('localhost', 27017, username="aaa",password="bbb", authSource='scada', authMechanism='SCRAM-SHA-256')
  rt_db = redis.Redis(host='localhost', port=6379, password="yourpassword")

  rt_pubsub = rt_db.pubsub()
  # TODO: should all keys be subscribed separately, and only when used, or filtered in python
  rt_pubsub.psubscribe(**{'__keyspace@0__:*.value': redis_dataUpdate})
  redis_event_thread = rt_pubsub.run_in_thread(sleep_time=0.01)

  socketio.run(app,host="0.0.0.0")

""""
  db = mongoclient.scada
  stream = db.data_timeseries.watch() # [{'$match': {'operationType': 'insert'}}]

https://pymongo.readthedocs.io/en/stable/api/pymongo/change_stream.html
try:
    resume_token = None
    pipeline = [{'$match': {'operationType': 'insert'}}]
    with db.collection.watch(pipeline) as stream:
        for insert_change in stream:
            print(insert_change)
            resume_token = stream.resume_token
except pymongo.errors.PyMongoError:
    # The ChangeStream encountered an unrecoverable error or the
    # resume attempt failed to recreate the cursor.
    if resume_token is None:
        # There is no usable resume token because there was a
        # failure during ChangeStream initialization.
        logging.error('...')
    else:
        # Use the interrupted ChangeStream's resume token to create
        # a new ChangeStream. The new stream will continue from the
        # last seen insert change without missing any events.
        with db.collection.watch(
                pipeline, resume_after=resume_token) as stream:
            for insert_change in stream:
                print(insert_change)

# watch for changes in mongodb
def mongo_watch_changes(stream):
    if stream.alive:
        change = stream.try_next()
        # Note that the ChangeStream's resume token may be updated
        # even when no changes are returned.
        for insert_change in stream:
            print(insert_change)
            resume_token = stream.resume_token
        print("Current resume token: %r" % (stream.resume_token,))
        if change is not None:
            print("Change document: %r" % (change,))
            return True
        else:
            return False
"""


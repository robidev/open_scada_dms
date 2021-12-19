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

async_mode = None #"threading" eventlet None
thread = None
tick = 0.001


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

# load svg data
def query(x1,y1,x2,y2,z):
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
  ct = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <g id="S12/D1/Q1/I1">
    <title>CTR</title>
    <text id="iec60870://127.0.0.1:10102/IED4_SMVMUnn/MMXU1.AvAPhs.mag.f" class="MEAS" data-text="Current: \{value\} A" fill="#ffffff" stroke="#ffffff" x="291.851085" y="125.166792" font-size="12" font-family="Helvetica, Arial, sans-serif" text-anchor="start" xml:space="preserve" font-weight="normal" font-style="normal">current: {value} A</text>
    </g>
    </svg>"""

  vt = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <g id="S12/E1/Q1/U1">
    <title>VTR</title>
    <text id="iec60870://127.0.0.1:9102/IED3_SMVMUnn/MMXU1.AvPhVPhs.mag.f" class="MEAS" data-text="Voltage: \{value\} V" fill="#ffffff" stroke="#ffffff" x="296" y="244.499945" font-size="12" font-family="Helvetica, Arial, sans-serif" text-anchor="start" xml:space="preserve" font-weight="normal" font-style="normal">voltage: {value} V</text>
    </g>
    </svg>"""

  cbr = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <g id="S12/E1/Q1/QA1" class="draggable-group">
    <title>CBR</title>
    <text id="iec60870://127.0.0.1:7102/IED1_XCBRGenericIO/XCBR1.Pos.stVal"     class="MEAS" data-text="CBR: QA1=\{value\}" fill="#ffffff" stroke="#ffffff" x="296" y="272.166593" font-size="12" font-family="Helvetica, Arial, sans-serif" text-anchor="start" xml:space="preserve" font-weight="normal" font-style="normal"></text>
    <rect id="iec60870://127.0.0.1:7102/IED1_XCBRGenericIO/XCBR1.Pos.stVal"     class="XCBR" height="22.553162" width="19.999974" y="257.946454" x="256.364398" stroke-width="1.5" stroke="#ffffff" fill="#ffffff">
      <animate id="open" attributeName="fill" attributeType="XML" to="black" dur="100ms" fill="freeze" />
      <animate id="transition" attributeName="fill" attributeType="XML" to="green" dur="10ms" fill="freeze" />
      <animate id="close" attributeName="fill" attributeType="XML"  to="white" dur="100ms" fill="freeze" /> 
      <animate id="error" attributeName="fill" attributeType="XML"  to="red" dur="10ms" fill="freeze" />           
    </rect>
    <rect id="iec60870://127.0.0.1:7102/IED1_XCBRGenericIO/CSWI1.Pos"     class="CSWI" height="22.553162" width="19.999974" y="257.946454" x="256.364398" stroke-width="1.5" stroke="none" fill="none"/>
    </g>
    </svg>"""

  swi = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <g id="S12/E1/Q1/QB1" class="draggable-group">
    <title>SWI</title>
    <text id="iec60870://$ioa"     class="MEAS" data-text="DIS: QB1=\{value\}" fill="#ffffff" stroke="#ffffff" x="296" y="314.666538" font-size="12" font-family="Helvetica, Arial, sans-serif" text-anchor="start" xml:space="preserve" font-weight="normal" font-style="normal"></text>
    <rect id="iec60870://127.0.0.1:7102/IED1_XCBRGenericIO/CSWI2.Pos"    class="CSWI" height="19" width="19" y="300.49959" x="256.864387" stroke="#ffffff" fill="#000000"/> 
    <line id="iec60870://127.0.0.1:7102/IED1_XCBRGenericIO/XSWI2.Pos.stVal"     class="XSWI" stroke="#ffffff" stroke-linecap="undefined" stroke-linejoin="undefined" y2="320" x2="266" y1="300" x1="266" stroke-width="4" fill="none">
        <animateTransform id="open" attributeName="transform" attributeType="XML" type="rotate" to="90 266 310 " dur="100ms" fill="freeze" />
        <animateTransform id="close" attributeName="transform" attributeType="XML" type="rotate" to="0 266 310 " dur="100ms" fill="freeze" />
        <animateTransform id="transition" attributeName="transform" attributeType="XML" type="rotate" to="45 266 310 " dur="100ms" fill="freeze" />
        <animateTransform id="error" attributeName="stroke" attributeType="XML" to="red" dur="100ms" fill="freeze" />
    </line>
    </g>
    </svg>"""

  ptr = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <line id="S12/D1/Q1/L1" class="LINE" stroke-linecap="undefined" stroke-linejoin="undefined" y2="153.934719" x2="266" y1="93.434721" x1="266" stroke-width="1.5" stroke="#ffffff" fill="none"/>

    <g id="S12/D1/T1">
    <title>PTR</title>
    <ellipse id="svg_T1_a" ry="18" rx="18" cy="171.753014" cx="266" fill-opacity="null" stroke-width="1.5" stroke="#ffffff" fill="none"/>
    <text    id="svg_T1_name" stroke="#ffffff"  xml:space="preserve" text-anchor="start" font-family="Helvetica, Arial, sans-serif" font-size="24" y="186.66199" x="296" stroke-width="null" fill="#ffffff">T1</text>
    <ellipse id="svg_T1_b" ry="18" rx="18" cy="196.290907" cx="266" fill-opacity="null" stroke-width="1.5" stroke="#ffffff" fill="none"/>
    </g>
 
    <line id="S12/E1/Q1/L2" class="LINE" stroke="#ffffff" stroke-linecap="undefined" stroke-linejoin="undefined" y2="256.43483" x2="266" y1="214.934859" x1="266" stroke-width="1.5" fill="none"/>
    </svg>"""

  feed = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <title>Bay 1</title>
    <text id="IFL" class="IFL" stroke="#ffffff" xml:space="preserve" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="24" y="80" x="266" fill="#ffffff">220KV Feed</text>
    <ellipse id="svg_top" stroke="#ffffff" ry="2.424242" rx="2.121212" cy="91.858974" cx="266" fill-opacity="null" stroke-width="1.5" fill="none"/>
    </svg>"""

  load = """<svg width="550" height="510" xmlns="http://www.w3.org/2000/svg" style="vector-effect: non-scaling-stroke;">
    <line id="S12/E1/W1/BB1" class="LINE" stroke="#ffffff" stroke-linecap="undefined" stroke-linejoin="undefined" y2="360" x2="266" y1="320.436511" x1="266" stroke-width="1.5" fill="none"/>
    <text id="LOAD" class="LOAD" stroke="#ffffff"  xml:space="preserve" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="24" y="380" x="266" fill="#ffffff">Load</text>
    </svg>"""
 
  ioa = "6002"
  swi = string.Template(swi).substitute(ioa=ioa)

  items = [
    {'id':1,'svg':ct,   'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980},
    {'id':2,'svg':vt,   'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980},
    {'id':3,'svg':cbr,  'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980},
    {'id':4,'svg':swi,  'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980},
    {'id':5,'svg':ptr,  'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980},
    {'id':6,'svg':feed, 'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980},
    {'id':7,'svg':load, 'x':5.842, 'y':51.981,'x2':5.843, 'y2':51.980}]
  return items

@socketio.on('get_svg_for_schema', namespace='')
def get_svg_for_schema(data):
  logger.info("x: %i, y: %i, z: %i", data['x'],data['y'],data['z'])
  # query database for svg objects, based on coordinates
  in_view_new = query(data['x'], data['y'], data['x']+100,data['y']+100, data['z'])

  # remove old items that should not be in view anymore
  for item in data['in_view']:
    if not any(d['id'] == item for d in in_view_new):
      socketio.emit("svg_object_remove_from_schema",item)

  # add new items that should be in view
  for item in in_view_new:
    if not item['id'] in data['in_view']:
      socketio.emit("svg_object_add_to_schema",item )
  


@socketio.on('get_svg_for_gis', namespace='')
def get_svg_for_gis(data):
  logger.info("x: %i, y: %i, z: %i", data['x'],data['y'],data['z'])
  # query database for svg objects, based on coordinates
  in_view_new = query(data['x'], data['y'], data['x']+100,data['y']+100, data['z'])

  # remove old items that should not be in view anymore
  for item in data['in_view']:
    if not any(d['id'] == item for d in in_view_new):
      socketio.emit("svg_object_remove_from_gis",item)

  # add new items that should be in view
  for item in in_view_new:
    if not item['id'] in data['in_view']:
      socketio.emit("svg_object_add_to_gis",item )

  geojson =  [{
        "type": "FeatureCollection", 
        "features": [
            {"type": "Feature", 
             "properties": 
                {
                "id": "one",
                },
             "geometry": 
                {"type": "LineString",
                 "coordinates": [[-81.0527, 33.9720], 
                                 [-79.6651, 34.9167], 
                                 [-85.0252, 38.6221]], 
                 "strokeColor": "#00FF00", 
                },
             "strokeColor": "#FF0000", 
             "style": {"strokeColor": "#000FF0"}
            },
            {"type": "Feature", 
             "properties": 
                {
                "id": "two",
                },
             "geometry": 
                {"type": "LineString",
                 "coordinates": [[-81.2527, 33.9720], 
                                 [-79.8651, 34.9167], 
                                 [-85.2252, 38.6221]], 
                 "strokeColor": "#00FF00", 
                },
             "strokeColor": "#FF0000", 
             "style": {"strokeColor": "#000FF0"}
            }
        ],
       "strokeColor": "#0FF000"
    }]

  geojson2 = [{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "stroke": "#ad7fa8",
        "stroke-width": 2,
        "stroke-opacity": 1
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            5.842629075050354,
            51.980789872371176
          ],
          [
            5.841186046600342,
            51.98081300094364
          ],
          [
            5.841400623321533,
            51.97933605242088
          ],
          [
            5.843364000320434,
            51.9789891111414
          ],
          [
            5.8451128005981445,
            51.97930631470222
          ],
          [
            5.845075249671936,
            51.979986973095556
          ],
          [
            5.843181610107422,
            51.98002001450193
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "stroke": "#729fcf",
        "stroke-width": 2,
        "stroke-opacity": 1,
        "fill": "#ef2929",
        "fill-opacity": 0.5
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              5.843503475189209,
              51.979742465930954
            ],
            [
              5.84347128868103,
              51.979303010510016
            ],
            [
              5.844458341598511,
              51.97937570268175
            ],
            [
              5.84447979927063,
              51.97972594512847
            ],
            [
              5.843911170959473,
              51.979887848730215
            ],
            [
              5.843503475189209,
              51.979742465930954
            ]
          ]
        ]
      }
    }
  ]
}]

  socketio.emit("geojson_object_add_to_gis",geojson2 )

#socketio.emit("geojson_object_update",{})

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


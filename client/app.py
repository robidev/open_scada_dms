#!/usr/bin/env python3
import os, sys
import threading
import string
import logging
import time
import uuid
import json
from datetime import datetime

from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit

import pymongo
from bson import ObjectId

import redis

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.bucket_api import BucketsApi


async_mode = None #"threading" #"eventlet" None
thread = None
tick = 0.001
mongoclient = None
logger = None
clients = {}
rt_pubsub = None
redis_event_thread = None
rt_db = None
get_value = None
ifs_status = {}

poll_datapoint = {}
alarm_rules_list = {}
alarm_table_mem = {}

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'BAD_SECRET_KEY'

#influxdb buckets
value_bucket = "bucket_1"
event_bucket = "bucket_2"

STATUS_POLL_INTERVAL = 2 # 2 seconds

socketio = SocketIO(app, async_mode=async_mode)

session_clients = {}

#http calls
@app.route('/', methods = ['GET'])
def index():
  if not 'user_id' in session:
    client_uuid = uuid.uuid4()
    session['user_id'] = client_uuid
    session_clients[client_uuid] = {}
  focus = str(request.args.get('focus'))
  if focus == None:
    focus = "0"
  return render_template('index.html', async_mode=socketio.async_mode, session=session, user_id = session['user_id'],focus = focus)

  

################################################

def add_listener(point):
  #global rt_db
  #check redis for point,
  #if rt_db.exists("data:" + point) > 0:
    # we allready get all redis data update events, so nothing to be done
    # possibly add psub for point in the future to limit amount of events
    # and/or increase reference count for subscribed data points
  #  return "rt"

  #else subscribe for db poll(keep reference count)
  global poll_datapoint
  if not point in poll_datapoint:
    poll_datapoint[point] = {}
    poll_datapoint[point]['refCount'] = 0
    poll_datapoint[point]['value'] = None

  poll_datapoint[point]['refCount'] += 1



def remove_listener(point):
  #global rt_db
  #check redis for point
  #if rt_db.exists("data:" + point) > 0:
    # possibly remove psub for point
    # and/or decrease reference count
  #  return "rt"

  #else unsubscribe for db poll(keep reference count)
  global poll_datapoint
  if point in poll_datapoint:
    if poll_datapoint[point]['refCount'] > 0:
      poll_datapoint[point]['refCount'] -= 1



###############################################
### Schema ###

@socketio.on('schema_addItems', namespace='')
def add_to_schema_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return None

  db = mongoclient.scada
  _id = db.schema_objects.insert_one(
    {'w':data['w'],
      'n':data['n'],
      'e':data['e'],
      's':data['s'],
      'svg':data['svg'], 
      'properties': data['properties'] }
      )
  # ensure _id gets retrieved
  return "_" + str(_id.inserted_id)


@socketio.on('schema_addGeojsonItem', namespace='')
def add_geojson_to_schema_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return None

  db = mongoclient.scada
  _id = db.schema_geojson.insert_one(
    {"type": data['type'], 
    "geometry": data["geometry"], 
    "properties": data["properties"]}
    )
    # ensure _id gets retrieved
  return "_" + str(_id.inserted_id)


@socketio.on('schema_editedItems', namespace='')
def update_schema_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  myquery = {'_id':ObjectId(data['_id'][1:])} # _id
  newvalues = {'w':data['w'],
      'n':data['n'],
      'e':data['e'],
      's':data['s'],
      'properties': data['properties'] }
      #'datapoints': data['dataPoints'] }
  db.schema_objects.update_one(myquery, {"$set": newvalues}, False) # update_many()


@socketio.on('schema_editedGeojsonItems', namespace='')
def update_schema_geojson_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  myquery = {'_id':ObjectId(data['_id'][1:])} # _id
  newvalues = {
    "geometry": data["geometry"], 
    "properties": data["properties"]
    } # x,y etc.
  #newvalues = {"geometry": data["geometry"], "properties.datapoints": data["properties"]['datapoints']} # x,y etc.
  db.schema_geojson.update_one(myquery, {"$set": newvalues}, False) # update_many()


@socketio.on('schema_removeItems', namespace='')
def remove_from_schema_database(uuid):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  db.schema_objects.delete_one({'_id':ObjectId(uuid[1:])})


@socketio.on('schema_removeGeojsonItems', namespace='')
def remove_from_schema_geojson_database(uuid):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  db.schema_geojson.delete_one({'_id':ObjectId(uuid[1:])})


### GIS ###

@socketio.on('gis_addItem', namespace='')
def add_to_gis_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return None

  db = mongoclient.scada
  if data['type'] == 'Svg':
    _id = db.gis_objects.insert_one(
      {"type": data['type'], 
      "location": data["location"], 
      "properties": data["properties"]}
      )
  else:
    _id = db.gis_objects.insert_one(
      {"type": data['type'], 
      "geometry": data["geometry"], 
      "properties": data["properties"]}
      )
  # ensure _id gets retrieved
  return "_" + str(_id.inserted_id)

@socketio.on('gis_editedItems', namespace='')
def update_gis_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  myquery = {'_id':ObjectId(data['_id'][1:])} # _id
  if data['type'] == 'Svg':
    newvalues = {"location": data["location"], "properties": data["properties"]} # x,y etc.
    #newvalues = {"location": data["location"], "properties.datapoints": data["properties"]['datapoints']} # x,y etc.
  else:
    newvalues = {"geometry": data["geometry"], "properties": data["properties"]} # x,y etc.
    #newvalues = {"geometry": data["geometry"], "properties.datapoints": data["properties"]['datapoints']} # x,y etc.
  db.gis_objects.update_one(myquery, {"$set": newvalues}, False) # update_many()


@socketio.on('gis_removeItems', namespace='')
def remove_from_gis_database(uuid):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  db.gis_objects.delete_one({'_id':ObjectId(uuid[1:])})


### templates ###

@socketio.on('svg_addTemplate', namespace='')
def svg_addTemplate(template):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  # TODO: prevent nosql injection
  db.svg_templates.insert_one(template)


@socketio.on('svg_getTemplates', namespace='')
def svg_getTemplate(_):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}

  db = mongoclient.scada
  cursor = db.svg_templates.find({})
  data = []
  for object in cursor:
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")
    data.append(object)

  return data

###############################################

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


# register datapoint for polling/reporting
@socketio.on('register_datapoint', namespace='')
def register_datapoint(point):
  global rt_db
  global poll_datapoint
  global clients
  client = request.sid
  logger.debug("register datapoint:" + str(point) )
  if not client in clients: # create a new client list, if it did not yet exist
    clients[client] = []
  
  add_listener(point) # increase refcount for listening to this datapoint
  # add to client list
  clients[client].append(point)
  # send data update for the point
  value = rt_db.get("data:" + point )
  if value != None:
    value = value.decode("utf-8")
  else:
    value = get_value(point)  #value = influxdb_get_value(point)
  logger.debug("reg type:" + str(type(value)) + ", value:" + str(value))
  if value == None:
    value = 'UNKNOWN'
  poll_datapoint[point]['value'] = value
  updateDataPoint(point,value) # emit to connected webclients  


def updateDataPoint(point, data_l):
  global clients
  recepients = []
  # send data to all subscribed clients
  for client in clients:
    if point in clients[client]:
      recepients.append(client)
  socketio.emit("updateDataPoint",data={'key':point,'value':data_l},to=recepients)


# register datapoint for polling/reporting
@socketio.on('unregister_datapoint', namespace='')
def unregister_datapoint(data):
  logger.debug("client:" + request.sid)
  client = request.sid
  logger.debug("unregister datapoint:" + str(data) )
  if not client in clients:
    clients[client] = []

  if data in clients[client]:
    remove_listener(data)
    # remove item from client list
    clients[client].remove(data)

@socketio.on('disconnect')
def disconnect():
  logger.info('Client disconnected: ' + request.sid )
  client = request.sid
  if client in clients:
    del clients[client]


# web UI: load datamodels for registered IED's
@socketio.on('register_datapoint_finished', namespace='')
def register_datapoint_finished(data):
  logger.debug(request.sid)
  logger.debug("register datapoint finished")

# load svg schema data
def query_schema_svg(x1,y1,x2,y2,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
  db = mongoclient.scada

  cursor = db.schema_objects.find(
    {
      '$and':[{
        '$and':[
          { 
            '$or': [ 
              {'w':  {'$gte':x1 }},  
              {'e': {'$gte':x1 }}, 
            ]
          },{
            '$or':[
              {'w':  {'$lte':x2 }},
              {'e': {'$lte':x2 }} 
            ] 
          }
        ]
      },{
        '$and':[
          { 
            '$or': [ 
              {'n':  {'$gte':y1 }},  
              {'s': {'$gte':y1 }}, 
            ]
          },{
            '$or':[
              {'n':  {'$lte':y2 }},
              {'s': {'$lte':y2 }} 
            ] 
          }
        ]
      }]
    } 
  )

  data = []
  for object in cursor:
    # check depth bounds
    if 'z_min' in object['properties'] and z < object['properties']['z_min']:
      continue
    if 'z_max' in object['properties'] and z > object['properties']['z_max']:
      continue
    
    try:
      svg = db.svg_templates.find_one({"name":object["svg"]})
    except Exception as ex:
      logger.error("while fetching svg template for '"+str(object["svg"])+"' : " + str(ex))
      continue
  
    result_svg = svg["svg"]
    if 'datapoints' in object["properties"]:
      result_svg = string.Template(svg["svg"]).substitute(object["properties"]['datapoints'])
      
    object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + result_svg + "</svg>"
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")

    data.append(object)

  return data


#the schema render function
@socketio.on('get_objects_for_schema')#, namespace='')
def get_objects_for_schema(data):

  # logger.info("x: %i, y: %i, x2: %i, y2: %i, z: %i", data['w'],data['n'],data['e'],data['s'],data['z'])
  # query database for svg objects, based on coordinates
  in_view_new = query_schema_svg(data['w'],data['n'],data['e'],data['s'], data['z'])

  # remove old items that should not be in view anymore
  for item in data['in_view']:
    if not any(d['id'] == item for d in in_view_new):
      socketio.emit("svg_object_remove_from_schema",item)

  # add new items that should be in view
  for item in in_view_new:
    if not item['id'] in data['in_view']:
      socketio.emit("svg_object_add_to_schema",item )

  
  in_view_geojson_schema = query_schema_geojson(data['w'], data['n'], data['e'], data['s'], data['z'])
  geojson = [{"type": "FeatureCollection", "features": in_view_geojson_schema }]
  socketio.emit("geojson_object_add_to_map_schema",geojson )
  
  

# load svg gis data
def query_schema_geojson(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that (partly) fall within that box, thus should be drawn
  db = mongoclient.scada
  cursor = db.schema_geojson.find({ 
    '$and':[
      {
        'type': 'Feature'
      },
      {
        "geometry": {
        "$geoIntersects": {
            "$geometry": {
              "type": "Polygon" ,
              "coordinates": [ [ [w,n],[e,n],[e,s],[w,s],[w,n] ] ] # square
            }
          }
        }
      }
    ]
  })
  data = []
  for item in cursor:
    # check depth bounds
    if 'z_min' in item['properties'] and z < item['properties']['z_min']:
      continue
    if 'z_max' in item['properties'] and z > item['properties']['z_max']:
      continue

    item['_id'] = "_" + str(item['_id'])
    data.append(item)
  return data


# load svg gis data
def query_gis_geojson(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that (partly) fall within that box, thus should be drawn
  db = mongoclient.scada
  cursor = db.gis_objects.find({ 
    '$and':[
      {
        'type': 'Feature'
      },
      {
        "geometry": {
        "$geoIntersects": {
            "$geometry": {
              "type": "Polygon" ,
              "coordinates": [ [ [w,n],[e,n],[e,s],[w,s],[w,n] ] ] # square
            }
          }
        }
      }
    ]
  })
  data = []
  for item in cursor:
    # check depth bounds
    if 'z_min' in item['properties'] and z < item['properties']['z_min']:
      continue
    if 'z_max' in item['properties'] and z > item['properties']['z_max']:
      continue

    item['_id'] = "_" + str(item['_id'])
    data.append(item)
  return data


# load svg gis data
def query_gis_svg(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that (partly) fall within that box, thus should be drawn

  db = mongoclient.scada
  cursor = db.gis_objects.find({ 
    '$and':[
      {
        'type': 'Svg'
      },
      {
        "location": {
        "$geoIntersects": {
            "$geometry": {
              "type": "Polygon" ,
              "coordinates": [ [ [w,n],[e,n],[e,s],[w,s],[w,n] ] ] # square
            }
          }
        }
      }
    ]
  })
  
  data = []

  for object in cursor:
    # check depth bounds
    if 'z_min' in object['properties'] and z < object['properties']['z_min']:
      continue
    if 'z_max' in object['properties'] and z > object['properties']['z_max']:
      continue
    
    try:
      svg = db.svg_templates.find_one({"name":object["properties"]["svg"]})
    except Exception as ex:
      logger.error("while fetching svg template for '"+str(object["properties"]["svg"])+"' : " + str(ex))
      continue
    
    result_svg = svg["svg"]
    if 'datapoints' in object["properties"]:
      result_svg = string.Template(svg["svg"]).substitute(object["properties"]['datapoints'])
      
    object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + result_svg + "</svg>"
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")

    data.append(object)

  return data


@socketio.on('get_objects_for_gis', namespace='')
def get_objects_for_gis(data):
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
  socketio.emit("geojson_object_add_to_map_gis",geojson )


@socketio.on('publish', namespace='')
def publish_operation(data):
  global rt_db
  if data['operation'] == 'select':
    logger.info("select:" + data['element'] + ">" + data['value'])
    rt_db.publish("select:" + data['element'],data['value'])
    publish_event(data['element'],"control:select",data['value'])
  if data['operation'] == 'operate':
    logger.info("operate:" + data['element'] + ">" + data['value'])
    rt_db.publish("operate:" + data['element'],data['value'])
    publish_event(data['element'],"control:operate",data['value'])
  if data['operation'] == 'cancel':  
    logger.info("cancel:" + data['element'])
    rt_db.publish("cancel:" + data['element'],"cancel")
    publish_event(data['element'],"control:cancel","None")


### front end status check
def get_ifs_status(ifs):
  global rt_db
  rt_db.publish("ifs_status:",ifs) # send a status request


def ifs_status_handler(message): # receive a status answer
  global ifs_status
  ifs = message['data'].decode("utf-8")
  old_status =  False
  if ifs in ifs_status:
    old_status =  ifs_status[ifs]['online']

  ifs_status[ifs] = {'lastseen': time.time(),'online': True}
  if ifs in ifs_status and old_status == False:
    publish_event(ifs,"status","online")
  

# call this on interval
def ifs_check_online(interval):
  global ifs_status
  while True:
    temp_ifs_status = ifs_status.copy() # shallow copy in case list changes size during operation
    for ifs in temp_ifs_status:
      if time.time() > (temp_ifs_status[ifs]['lastseen'] + (interval * 4)) and temp_ifs_status[ifs]['online'] == True: # if more than 2x poll-time, set offline
        # set IFS status to offline
        temp_ifs_status[ifs]['online'] = False
        publish_event(ifs,"status","offline")
    time.sleep(interval)




#######################################################################


def redis_dataUpdate(msg):
  global rt_db
  if rt_db == None:
    logger.error("No redis db connected")
    return

  key = msg['channel'][15:]
  data = rt_db.get(key)
  key_u8 = key.decode("utf-8")[5:]
  data_u8 = data.decode("utf-8")
  
  logger.debug("update: %s %s", str(key_u8), str(data_u8))
  updateDataPoint( key_u8,data_u8) # emit to connected webclients
  update_alarms( key_u8,data_u8 )



#def mongodb_get_value(point):
#  global mongoclient
#  # query mongodb for possible update
#  db = mongoclient.scada
# cursor = db.data_timeseries.find({'id':point}).sort([('timestamp', -1)]).limit(1) # find newest value
#  for object in cursor:
#    return object['value']
#  return None


def influxdb_get_value(point):
  global influxdb_query_api
  # query influxdb for possible update
  query = ' from(bucket:"' + value_bucket + '")\
    |> range(start: 0)\
    |> filter(fn:(r) => r._measurement == "datapoint")\
    |> filter(fn: (r) => r.id == "' + point + '")\
    |> last() '

  result = influxdb_query_api.query(org="scada", query=query)
  if result and len(result) > 0:
    for table in result:
      for record in table.records:
        return record.get_value() # return first result
  return None


###############################################################
###############################################################
###############################################################
### Alarm logic ###

# called if any updated value event is triggered, checks if an alarm should be modified
def update_alarms(key, value):
  global alarm_rules_list
  if key in alarm_rules_list:
    alarm_logic_list = alarm_rules_list[key]['alarm_logic_list']
    for alarm in alarm_logic_list:
      # alarm.
      #  value_1, value_2 = "number"
      #  logic = <,>,==,<>,!=
      try: # attempt to convert to int
        tryval = int(value)
        value = tryval
      except:
        pass #leave the value a string

      if isinstance(value, int):
        value_1 = int(alarm['value_1'])
        value_2 = int(alarm['value_2'])
      else:
        value_1 = alarm['value_1']
        value_2 = alarm['value_2']
      
      if alarm['logic'] == "==" and value == value_1:
        trigger_alarm(key, alarm, value)
      elif alarm['logic'] == "<" and value < value_1:
        trigger_alarm(key, alarm, value)
      elif alarm['logic'] == ">" and value > value_1:
        trigger_alarm(key, alarm, value)
      elif alarm['logic'] == "!=" and value != value_1:
        trigger_alarm(key, alarm, value)
      elif alarm['logic'] == "><" and value > value_1 and value < value_2:
        trigger_alarm(key, alarm, value)


def trigger_alarm(datapoint, alarm, value):
  global alarm_table_mem
  global mongoclient
  # check if event should only be send on state change (enables polling), or every check fires event
  if not datapoint in alarm_table_mem:
    alarm_table_mem[datapoint] = {}
  alert_id = alarm['alert_id']

  update = False
  if alarm['retrigger'] == True:
    update = True

  if "set_alarm" in alarm['action']:
    # if alarm can be retriggered, or if not, only trigger if state changes
    if (update == True or 
        not alert_id in alarm_table_mem[datapoint] or
        alarm_table_mem[datapoint][alert_id] != True):
      logger.debug("set alarm: " + datapoint)
      alarm_table_mem[datapoint][alert_id] = True
      update = True
      # add/update item in alarm_table @ mongodb
      db = mongoclient.scada
      time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f+00:00") #"2022/02/10 - 10:00:00"
      datapoint_and_alert_id = {'datapoint': datapoint, "alert_id": alert_id } 
      newvalues =  {
            "time":         time,
            "datapoint":    datapoint,
            "alert_id":     alert_id,
            "element":      alarm['element'],
            "message":      alarm['action']['set_alarm'],
            "severity":     alarm['severity'],
            "details":      alarm['details'],
            "value":        str(value),
            "alarm":        True, 
            "acknowledged": False, 
            "open":         True
          }
      db.alarm_table.update_one(datapoint_and_alert_id, {"$set": newvalues}, upsert=True)
      update_alarm_table(None)


  if "reset_alarm"in alarm['action']:
    if (update == True or 
        not alert_id in alarm_table_mem[datapoint] or
        alarm_table_mem[datapoint][alert_id] != False):
      logger.debug("reset alarm: " + datapoint)
      alarm_table_mem[datapoint][alert_id] = False
      update = True
      # update item in alarm_table @ mongodb
      db = mongoclient.scada
      time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f+00:00") #"2022/02/10 - 10:00:00"
      datapoint_and_alert_id = {'datapoint': datapoint, "alert_id": alert_id } 
      newvalues =  {
            "time":         time,
            "datapoint":    datapoint,
            "alert_id":     alert_id,
            "element":      alarm['element'],
            "message":      alarm['action']['reset_alarm'],
            "severity":     alarm['severity'],
            "details":      alarm['details'],
            "value":        str(value),
            "alarm":        False
          }
      db.alarm_table.update_one(datapoint_and_alert_id, {"$set": newvalues}, upsert=True)
      update_alarm_table(None)


  if "event" in alarm['action'] and update == True:
    publish_event(alarm['element'],alarm['action']['event'],value)

  if "script" in alarm['action']:
    logger.debug("run script:" + alarm['action']['script'])
    # subprocess....
  return


#########################################################################################
# alarm io with frontend

@socketio.on('update_alarm_state', namespace='')
def update_alarm_state(dataitem):
  global alarm_rules_list
  global mongoclient

  # object identifier
  datapoint = dataitem['datapoint']
  alert_id = dataitem['alert_id']

  #data to be modified/updated
  alarm = dataitem['alarm']
  ack = dataitem['acknowledged']
  open = dataitem['open']
  comment = ""
  if 'comment' in dataitem:
    comment = dataitem['comment']

  if not datapoint in alarm_rules_list:
    logger.warning("could not find datapoint in alarm list")
    return

  alarm_item = None
  for rule_index in alarm_rules_list[datapoint]['alarm_logic_list']:
    if alert_id == rule_index['alert_id']:
      alarm_item = rule_index
      break

  if alarm_item == None:
    logger.warning("could not find alert_id in alarm list[datapoint]")
    return

  db = mongoclient.scada
  this_alarm = {'datapoint': datapoint, "alert_id": alert_id } 
  newvalues =  {
        "alarm": alarm,
        "acknowledged": ack,
        "open": open,
        "comment": comment 
      }
  # get old values
  cursor = db.alarm_table.find(this_alarm)
  for object in cursor:
    oldack = object['acknowledged']
    oldopen = object['open']
    oldalarm = object['alarm']
  # set net values
  db.alarm_table.update_one(this_alarm, {"$set": newvalues}, upsert=False)
  logger.debug("++update_alarm_state")

  # check if event needs to be made
  if ack != oldack:
    publish_event(alarm_item['element'],"alarm acknowledged",ack)
    if comment != "":
      publish_event(alarm_item['element'],"alarm acknowledged "+str(ack)+" with comment:",comment)
  if open != oldopen:
    publish_event(alarm_item['element'],"alarm open",open)
    if comment != "":
      publish_event(alarm_item['element'],"alarm open  "+str(open)+" with comment:",comment)
  if alarm != oldalarm:
    publish_event(alarm_item['element'],"alarm raised",alarm)
    if comment != "":
      publish_event(alarm_item['element'],"alarm raised "+str(alarm)+" with comment:",comment)
  # set comment if provided

  update_alarm_table(None)


@socketio.on('get_alarm_table', namespace='')
def update_alarm_table(data):
  global alarm_table_mem
  global mongoclient

  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}

  db = mongoclient.scada
  cursor = db.alarm_table.find({})
  alarm_items = []
  for object in cursor:
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")
    alarm_items.append(object)

    # additional processing; set alarm state in memory
    datapoint = object["datapoint"]
    alert_id = object["alert_id"]
    if not datapoint in alarm_table_mem:
      alarm_table_mem[datapoint] = {}
    alarm_table_mem[datapoint][alert_id]=object["alarm"]

  socketio.emit('update_alarm_table', alarm_items)
  # return alarm_items


def get_alarm_logic():
  global alarm_rules_list
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}

  db = mongoclient.scada
  cursor = db.alarm_logic.find({})
  logger.debug("get_alarm_logic: got data from mongodb")
  # clear the list if desired
  alarm_rules_list = {}

  for object in cursor:
    logger.debug("get_alarm_logic: parsing object")
    datapoint = object["datapoint"]
    # set alarm state in memory
    if not datapoint in alarm_rules_list:
      alarm_rules_list[datapoint] = {}
      alarm_rules_list[datapoint]['alarm_logic_list'] = []

    alarm = {
      "alert_id":object["alert_id"],
      "logic":object["logic"],
      "value_1":object["value_1"], 
      "value_2":object["value_2"],
      "action": object["action"],
      "retrigger":object['retrigger'],
      "element":object['element'],
      "severity":object['severity'],
      "details":object['details']
    }

    alarm_rules_list[datapoint]['alarm_logic_list'].append(alarm)
  logger.debug("get_alarm_logic: done")


@socketio.on('get_alarm_rules', namespace='')
def get_alarm_rules(data):
  global alarm_rules_list
  if len(alarm_rules_list) == 0:
    get_alarm_logic()
  return json.dumps(alarm_rules_list, indent=4)


@socketio.on('save_alarm_rules', namespace='')
def save_alarm_rules(data):
  try:
    local_alarm_list = json.loads(data)
  except:
    logger.error("could not parse json data")
    return False

  try:
    global mongoclient
    db = mongoclient.scada

    db.alarm_logic.drop()
    #db.createCollection("alarm_logic")
    for datapoint in local_alarm_list:
      for alarm in local_alarm_list[datapoint]['alarm_logic_list']:
        alarm['datapoint'] = datapoint
        db.alarm_logic.insert_one(alarm)
        alarm.pop("_id") # insert_one adds an _id, that we dont need
        alarm.pop('datapoint')
  except:
    logger.error("could not save alarm rule data")
    return False

  global alarm_rules_list
  alarm_rules_list = local_alarm_list
  return True


##############################################################################
##############################################################################
##############################################################################
### Event logic ###
def publish_event(element,msg,value):
  # add event item @ influxdb
  global influxdb_write_api
  current_time = datetime.utcnow()
  p = Point("event").tag("element", element).time(int(current_time.timestamp()*1000000),write_precision='us').field("message", msg).field("value", str(value))
  influxdb_write_api.write(bucket=event_bucket, record=p)
  socketio.emit('add_event_to_table', {"time":current_time.strftime("%Y-%m-%d %H:%M:%S.%f+00:00"), 'element':element, 'msg':msg, 'value':value})
  # re-eval if we need to trigger an alarm-rule. this can become recursive, but due to the "." concatination, we prevent an endless loop in the logic
  update_alarms( element + "." + msg, value )


@socketio.on('get_event_table', namespace='')
def get_event_table(param):
  # retrieve events from influxdb
  global influxdb_query_api
  # query influxdb for possible update
  query = ' from(bucket:"' + event_bucket + '")\
    |> range(start: 0)\
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '

  data = []
  result = influxdb_query_api.query(org="scada", query=query)
  if result and len(result) > 0:
    for table in result:
      for record in table.records:
        timestmp = str(record.values["_time"])
        elem = str(record.values["element"])
        msg =  str(record.values["message"]) #str(record.values["_field"])
        val =  str(record.values["value"]) #str(record.values["_value"])
        data.append({"time":timestmp, "element":elem, "msg": msg, "value": val})

  socketio.emit('update_event_table', data)


###############################################################
###############################################################
###############################################################
### dataprovider config ###
# retrieve dataprovider's from mongodb
@socketio.on('get_dataproviders', namespace='')
def get_dataproviders(data):
  global mongoclient
  global rt_db
  
  db = mongoclient.scada
  cursor = db.dataprovider_list.find({})

  data = []
  for object in cursor:
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")

    dataprovider_on = rt_db.get("connections:"+object["dataprovider"]+".active")
    if dataprovider_on == b'1':
      object["online"] = True
    else:
      object["online"] = False

    data.append(object)

  return data

def update_dataprovider_status(dataprovider):
  dataprovider_on = rt_db.get("connections:"+object["dataprovider"]+".active")
  online = False
  if dataprovider_on == b'1':
    online = True
  emit('update_dataprovider_status',{'dataprovider':dataprovider,'online':online})


  # edit/add dataprovider's from mongodb
@socketio.on('edit_dataprovider', namespace='')
def edit_dataprovider(data):
  global mongoclient
  try:
    item = json.loads(data)
    dataprovider = item['dataprovider']
    enabled = int(item['enabled'])
    IFS = item['IFS'] 
    type = item['type']

    db = mongoclient.scada
    newvalues =  {
        "enabled": enabled,
        "IFS": IFS,
        "type": type
      }
    _id = db.dataprovider_list.update_one({"dataprovider":dataprovider}, {"$set": newvalues}, upsert=True)
    # ensure _id gets retrieved
    return "_" + str(_id.upserted_id)
  except:
    logger.error("could not edit dataprovider")
    return False


  # delete dataprovider's from mongodb
@socketio.on('delete_dataprovider', namespace='')
def del_dataprovider(uuid):
  global mongoclient
  db = mongoclient.scada
  try:
    db.dataprovider_list.delete_one({'_id':ObjectId(uuid[1:])})
    return True
  except:
    logger.error("could not delete dataprovider")
    return False


###############################################################
###############################################################
###############################################################

def refresh_datapoints(force_update=True):
  global rt_db
  global poll_datapoint
  new_poll_datapoint = poll_datapoint.copy() # make shallow copy to account for changes during iteration
  for point in new_poll_datapoint:
    if new_poll_datapoint[point]['refCount'] > 0: # check if currently a client wants this datapoint updated

      value = rt_db.get("data:" + point )
      if value != None:
        value = value.decode("utf-8")
      else:
        value = get_value(point)  #value = influxdb_get_value(point)
      #logger.debug("ref type:" + str(type(value)) + ", value:" + str(value))
      if value == None:
        value = 'UNKNOWN'

      # check if data changed since last check
      oldValue = new_poll_datapoint[point]['value']
      if oldValue != value or force_update == True: # update value, only if value was changed, or if update is forced)
        poll_datapoint[point]['value'] = value # update the actual dict
        updateDataPoint(point,value) # emit to connected webclients  


#background thread
def worker():
  socketio.sleep(tick)
  logger.debug("polling thread started")
  interval = 50
  interval_counter = 0
  while True:
    socketio.sleep(0.2)
    if influxdb_client == None: #mongoclient == None:
      logger.error("no db connection")
      socketio.sleep(10)
      continue

    if interval_counter % interval == 0: # update value, only if value was changed, and every 10 seconds (to keep client in sync)
      refresh_datapoints(True)
    else:
      refresh_datapoints(False)
    interval_counter += 1


def redis_events():
  global rt_pubsub
  while True:
    if rt_pubsub == None:
      logger.error("no redis connection")
      socketio.sleep(10)
      continue
    message = rt_pubsub.get_message()
    if message:
      logger.warning("missed event:" + str(message))
    else:
      socketio.sleep(0.01)


if __name__ == '__main__':
  logger = logging.getLogger('webserver')
  logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)

  mongodb_host = "mongodb"
  mongodb_db = "scada"
  mongodb_username="dbuser"
  mongodb_password="mongo_secret"

  redis_host = "localhost"
  redis_password = "redis_secret"

  influxdb_host = "http://127.0.0.1:8086"
  influxdb_api = "influxdb_secret"
  influxdb_org = "scada"

  if len(sys.argv) > 1:
    if sys.argv[1] == "remote":
      logger.info("remote host parameters (for inside docker-compose network)")
      mongodb_host = os.environ['IFS_MONGODB_HOST']
      mongodb_db = os.environ['IFS_MONGODB_DB']
      mongodb_username=os.environ['IFS_MONGODB_USERNAME']
      mongodb_password=os.environ['IFS_MONGODB_PASSWORD']

      redis_host = os.environ['IFS_REDIS_HOST']
      redis_password = os.environ['IFS_REDIS_PASSWORD']

      influxdb_host = os.environ['IFS_INFLUXDB_HOST'] #"http://influxdb:8086"
      influxdb_api = os.environ['IFS_INFLUXDB_API']
      influxdb_org = os.environ['IFS_INFLUXDB_ORG']

  try:
    mongoclient = pymongo.MongoClient(mongodb_host, 27017,  #'localhost', 27017, <- added mongodb to localhost for resolution of the replicaset, else there is a coonect error
      username=mongodb_username,
      password=mongodb_password, 
      authSource=mongodb_db, 
      authMechanism='SCRAM-SHA-256', 
      connect=True, 
      connectTimeoutMS=2000,
      socketTimeoutMS=2000)
    logger.info("connected to mongodb")
    db = mongoclient.scada
    logger.info("mongodb: set db")
    get_alarm_logic()
    logger.info("mongodb: alarm logic loaded")

  except Exception as e:
    logger.error("mongodb: exception while initialising mongodb connection: " + str(e))
    mongoclient = None
    exit(-1)

  try:
    rt_db = redis.Redis(host=redis_host, port=6379, password=redis_password)
    rt_pubsub = rt_db.pubsub()

    rt_pubsub.psubscribe(**{'__keyspace@0__:data:*': redis_dataUpdate}) # needed for values in clients and alarms
    rt_pubsub.subscribe(**{ "ifs_status_online": ifs_status_handler })
    
    redis_event_thread = socketio.start_background_task(target=redis_events)
    logger.info("connected to redis")
  except:
    logger.error("there is an issue with redis db")
    rt_db = None
    exit(-1)

  try:
    influxdb_client = InfluxDBClient(url=influxdb_host, 
            token=influxdb_api, 
            org=influxdb_org)
    influxdb_query_api = influxdb_client.query_api()
    influxdb_write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)

    influxdb_bucket_api = influxdb_client.buckets_api()
    vbucket = influxdb_bucket_api.find_bucket_by_name(value_bucket)
    if vbucket == None:
      logger.error("cannot find value bucket, is the influxdb initialised?")
      exit(-1)

    ebucket = influxdb_bucket_api.find_bucket_by_name(event_bucket)
    if ebucket == None:
      logger.warning("cannot find event bucket, creating it")
      influxdb_bucket_api.create_bucket(bucket_name=event_bucket, description="a bucket for events", retention_rules=vbucket.retention_rules)
    else:
      logger.debug("found event bucket")

  except Exception as e:
    logger.error("there is an issue with influxdb:" + str(e))
    influxdb_client = None
    influxdb_write_api = None
    exit(-1)

  # get values
  get_value = influxdb_get_value # mongodb_get_value

  status_poll_thread = threading.Thread(target=ifs_check_online, args=(STATUS_POLL_INTERVAL,))
  status_poll_thread.start()

  logger.info("starting webserver")
  socketio.run(app,host="0.0.0.0")



#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

import string
import logging

import pymongo
from bson import ObjectId
import redis
import uuid
import json


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

poll_datapoint = {}
alarm_list = {}

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'BAD_SECRET_KEY'

#influxdb buckets
value_bucket = "bucket_1"
event_bucket = "bucket_2"

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

  #else subscribe for mongodb poll(keep reference count)
  if not point in poll_datapoint:
    poll_datapoint[point] = {}
    poll_datapoint[point]['refCount'] = 0
    poll_datapoint[point]['value'] = None

  poll_datapoint[point]['refCount'] += 1

  return "poll"


def remove_listener(point):
  #global rt_db
  #check redis for point
  #if rt_db.exists("data:" + point) > 0:
    # possibly remove psub for point
    # and/or decrease reference count
  #  return "rt"

  #else unsubscribe for mongodb poll(keep reference count)
  if point in poll_datapoint:
    if poll_datapoint[point]['refCount'] > 0:
      poll_datapoint[point]['refCount'] -= 1

  return "poll"


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
      'datapoints': data['dataPoints'] }
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
  _id = db.schema_geojson.insert_one({"type": data['type'], "geometry": data["geometry"], "properties": data["properties"]})
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
      'datapoints': data['dataPoints'] }
  db.schema_objects.update_one(myquery, {"$set": newvalues}, False) # update_many()


@socketio.on('schema_editedGeojsonItems', namespace='')
def update_schema_geojson_database(data):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  myquery = {'_id':ObjectId(data['_id'][1:])} # _id
  newvalues = {"geometry": data["geometry"], "properties": data["properties"]} # x,y etc.
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
    _id = db.gis_objects.insert_one({"type": data['type'], "location": data["location"], "properties": data["properties"]})
  else:
    _id = db.gis_objects.insert_one({"type": data['type'], "geometry": data["geometry"], "properties": data["properties"]})
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
    newvalues = {"location": data["location"], "properties.datapoints": data["properties"]['datapoints']} # x,y etc.
  else:
    newvalues = {"geometry": data["geometry"], "properties.datapoints": data["properties"]['datapoints']} # x,y etc.
  db.gis_objects.update_one(myquery, {"$set": newvalues}, False) # update_many()


@socketio.on('gis_removeItems', namespace='')
def remove_from_gis_database(uuid):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return

  db = mongoclient.scada
  db.gis_objects.delete_one({'_id':ObjectId(uuid[1:])})

  #TEST! TODO remove
  #new_alarm_check("iec60870-5-104://127.0.0.1:2404/MeasuredValueScaled/101",  
  #  alert_id = 1, # alert id within this datapoint
  #  logic = ">", # logic to apply to value
  #  value_1 = 89,value_2 = 0, # test values to check logic and value with
  #  actions = {"set_alarm":"OverVoltage"}, # actions to perform on match
  #  retrigger = False, # retrigger on every match, or only if new alarm (allows for polling)
  #  element = { "B1":"s1","B2":"a/b/c","B3":"d" } # text elements to be logged in alarm/event window
  #  )
  #new_alarm_check("iec60870-5-104://127.0.0.1:2404/MeasuredValueScaled/101",  
  #  alert_id = 2, # alert id within this datapoint
  #  logic = "<", # logic to apply to value
  #  value_1 = 90,value_2 = 0, # test values to check logic and value with
  #  actions = {"reset_alarm":"OverVoltage"}, # actions to perform on match
  #  retrigger = False, # retrigger on every match, or only if new alarm (allows for polling)
  #  element = { "B1":"s1","B2":"a/b/c","B3":"d" } # text elements to be logged in alarm/event window
  #  )


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
def register_datapoint(data):
  client = request.sid
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
  socketio.emit("updateDataPoint",data={'key':point,'value':data_l},to=recepients)


# register datapoint for polling/reporting
@socketio.on('unregister_datapoint', namespace='')
def unregister_datapoint(data):
  logger.info("client:" + request.sid)
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
  logger.info('Client disconnected: ' + request.sid )
  client = request.sid
  if client in clients:
    del clients[client]


# web UI: load datamodels for registered IED's
@socketio.on('register_datapoint_finished', namespace='')
def register_datapoint_finished(data):
  logger.info(request.sid)
  logger.info("register datapoint finished")

# load svg schema data
def query_schema(x1,y1,x2,y2,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, FUTURE TODO: and z-depth
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
    svg = db.svg_templates.find_one({"name":object["svg"]})
    object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + string.Template(svg["svg"]).substitute(object['datapoints']) + "</svg>"
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")
    data.append(object)

  return data


#the schema render function
@socketio.on('get_svg_for_schema')#, namespace='')
def get_svg_for_schema(data):

  logger.info("x: %i, y: %i, x2: %i, y2: %i, z: %i", data['w'],data['n'],data['e'],data['s'],data['z'])
  # query database for svg objects, based on coordinates
  in_view_new = query_schema(data['w'],data['n'],data['e'],data['s'], data['z'])

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
  socketio.emit("geojson_object_add_to_map",geojson )
  

# load svg gis data
def query_schema_geojson(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, FUTURE TODO:  and z-depth
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
    item['_id'] = "_" + str(item['_id'])
    data.append(item)
  return data


# load svg gis data
def query_gis_geojson(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, FUTURE TODO: and z-depth
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
    item['_id'] = "_" + str(item['_id'])
    data.append(item)
  return data


# load svg gis data
def query_gis_svg(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, FUTURE TODO: and z-depth
  # return list of svg items that (partly) fall within that box, thus should be drawn
  try:
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
      svg = db.svg_templates.find_one({"name":object["properties"]["svg"]})
      object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + string.Template(svg["svg"]).substitute(object["properties"]['datapoints']) + "</svg>"
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
  socketio.emit("geojson_object_add_to_map",geojson )


@socketio.on('publish', namespace='')
def publish_operation(data):
  global rt_db
  if data['operation'] == 'select':
    logger.info("select:" + data['element'] + ">" + data['value'])
    rt_db.publish("select:" + data['element'],data['value'])
  if data['operation'] == 'operate':
    logger.info("operate:" + data['element'] + ">" + data['value'])
    rt_db.publish("operate:" + data['element'],data['value'])
  if data['operation'] == 'cancel':  
    logger.info("cancel:" + data['element'])
    rt_db.publish("cancel:" + data['element'],"cancel")


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
  
  logger.info("update: %s %s", str(key_u8), str(data_u8))
  updateDataPoint( key_u8,data_u8) # emit to connected webclients
  update_alarms( key_u8,data_u8 )


def poll_dataUpdate(point, data):
  updateDataPoint(point,data) # emit to connected webclients


def mongodb_get_value(point):
  global mongoclient
  # query mongodb for possible update
  db = mongoclient.scada
  cursor = db.data_timeseries.find({'id':point}).sort([('timestamp', -1)]).limit(1) # find newest value
  for object in cursor:
    return object['value']
  return None


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

def update_alarms(key, value):
  global alarm_list
  if key in alarm_list:
    alarm_logic_list = alarm_list[key]['alarm_logic_list']
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


def trigger_alarm(key, alarm, value):
  global alarm_list
  global mongoclient
  # check if event should only be send on state change (enables polling), or every check fires event
  alert_id = alarm['alert_id']

  if alarm['retrigger'] == True:
    update = True
  else:
    update = False

  if "set_alarm" in alarm['action']:
    # if alarm can be retriggered, or if not, only trigger if state changes
    if alarm['retrigger'] == True or (alarm['retrigger'] == False and alarm_list[key][alert_id] != True):
      print("set alarm: " + key)
      alarm_list[key][alert_id] = True
      update = True
      # add/update item in alarm_table @ mongodb
      db = mongoclient.scada
      time = "2022/02/10 - 10:00:00"
      myquery = {'datapoint': key, "alert_id": alert_id } 
      newvalues =  {
            "time":         time,
            "datapoint":    key,
            "alert_id":     alert_id,
            "element":      alarm['element'],
            "message":      alarm['action']['set_alarm'],
            "value":        str(value),
            "alarm":        True, 
            "acknowledged": False, 
            "open":         True
          }
      db.alarm_table.update_one(myquery, {"$set": newvalues}, upsert=True)
      get_alarm_table(None)


  if "reset_alarm"in alarm['action']:
    if alarm['retrigger'] == True or (alarm['retrigger'] == False and alarm_list[key][alert_id] != False):
      print("reset alarm: " + key)
      alarm_list[key][alert_id] = False
      update = True
      # update item in alarm_table @ mongodb
      db = mongoclient.scada
      time = "2022/02/10 - 10:00:00"
      myquery = {'datapoint': key, "alert_id": alert_id } 
      newvalues =  {
            "time":         time,
            "datapoint":    key,
            "alert_id":     alert_id,
            "element":      alarm['element'],
            "message":      alarm['action']['reset_alarm'],
            "value":        str(value),
            "alarm":        False
          }
      db.alarm_table.update_one(myquery, {"$set": newvalues}, upsert=True)
      get_alarm_table(None)


  if "event" in alarm['action'] and update == True:
    publish_event(alarm['element'],alarm['action']['event'],value)

  if "script" in alarm['action']:
    print("run script:" + alarm['action']['script'])
    # subprocess....
  return


def new_alarm_check(datapoint,  
    alert_id = 1, # alert id within this datapoint
    logic = ">", # logic to apply to value
    value_1 = 0,value_2 = 0, # test values to check logic and value with
    actions = {"set_alarm":"Al1"}, # actions to perform on match (value of set_alarm is used in message)
    retrigger = True, # retrigger on every match, or only if new alarm (allows for polling)
    element = { "B1":"s1","B2":"a/b/c","B3":"d" } # text elements to be logged in alarm/event window
    ): 
  """
  logic = "" #  <,>,==,<>,!=
  actions = {
    "set_alarm":"Al1", 
    "reset_alarm":"AL1",
    "event":"EV1", 
    "script":"/var/script/run1"
    }
  """
  global alarm_list
  alarm = {
    "alert_id":alert_id,
    "logic":logic,
    "value_1":value_1, 
    "value_2":value_2,
    "action": actions,
    "retrigger":retrigger,
    "element":element,
  }

  if not datapoint in alarm_list:
    alarm_list[datapoint] = {}
    alarm_list[datapoint]['alarm_logic_list'] = []
    alarm_list[datapoint][alert_id]=False

  alarm_list[datapoint]['alarm_logic_list'].append(alarm)

  # add alarm to alarm_list in mongodb (TODO: should we check on alert_id for update/insert?)
  global mongoclient
  db = mongoclient.scada
  alarm['datapoint'] = datapoint
  db.alarm_logic.insert_one(alarm)


@socketio.on('update_alarm_state', namespace='')
def update_alarm_state(dataitem):
  global alarm_list
  global mongoclient

  # object identifier
  datapoint = dataitem['datapoint']
  alert_id = dataitem['alert_id']

  #data to be modified/updated
  alarm = dataitem['alarm']
  ack = dataitem['acknowledged']
  open = dataitem['open']

  if not datapoint in alarm_list:
    print("could not find datapoint in alarm list")
    return
  if not alert_id in alarm_list[datapoint]:
    print("could not find alert_id in alarm list[datapoint]")
    return

  db = mongoclient.scada
  myquery = {'datapoint': datapoint, "alert_id": alert_id } 
  newvalues =  {
        "alarm": alarm,
        "acknowledged": ack,
        "open": open
      }
  # get old values
  cursor = db.alarm_table.find(myquery)
  for object in cursor:
    oldack = object['acknowledged']
    oldopen = object['open']
  # set net values
  db.alarm_table.update_one(myquery, {"$set": newvalues}, upsert=False)
  print("++update_alarm_state")
  # check if event needs to be made
  for alarm_item in  alarm_list[datapoint]['alarm_logic_list']:
    if alarm_item['alert_id'] == alert_id:
      print("-- ack:" + str(ack) + " open:" + str(open) + " alarm:" + str(alarm))
      if ack != oldack:
        if ack  == True:
          publish_event(json.dumps(alarm_item['element']),"alarm acknowledged",True)
        else:
          publish_event(json.dumps(alarm_item['element']),"alarm unacknowledged",False)
      if open != oldopen:
        if open == True:
          publish_event(json.dumps(alarm_item['element']),"alarm set open",True)
        else:
          publish_event(json.dumps(alarm_item['element']),"alarm set closed",False)
      if alarm != alarm_list[datapoint][alert_id]:
        if alarm == True:
          publish_event(json.dumps(alarm_item['element']),"alarm manually raised",True)
        else:
          publish_event(json.dumps(alarm_item['element']),"alarm manually lowered",False)
      break

  get_alarm_table(None)



#########################################################################################
# io with frontend

@socketio.on('get_alarm_table', namespace='')
def get_alarm_table(data):
  global alarm_list
  global mongoclient

  # event test
  #publish_event("element_1","alarm set closed","TEST") # test

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
    datapoint = object["datapoint"]
    alert_id = object["alert_id"]
    # set alarm state in memory
    if not datapoint in alarm_list:
      alarm_list[datapoint] = {}
      alarm_list[datapoint]['alarm_logic_list'] = []
    
    alarm_list[datapoint][alert_id]=object["alarm"]

  socketio.emit('update_alarm_table', alarm_items)
  # return alarm_items


def get_alarm_logic(clear=True):
  global alarm_list
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}

  db = mongoclient.scada
  cursor = db.alarm_logic.find({})
  logger.info("get_alarm_logic: got data from mongodb")
  # clear the list if desired
  if clear == True:
    alarm_list = {}

  for object in cursor:
    logger.info("get_alarm_logic: parsing object")
    datapoint = object["datapoint"]
    alert_id = object["alert_id"]
    # set alarm state in memory
    if not datapoint in alarm_list:
      alarm_list[datapoint] = {}
      alarm_list[datapoint]['alarm_logic_list'] = []
    if not alert_id in alarm_list[datapoint]:
      alarm_list[datapoint][alert_id]=False

    alarm = {
      "alert_id":alert_id,
      "logic":object["logic"],
      "value_1":object["value_1"], 
      "value_2":object["value_2"],
      "action": object["action"],
      "retrigger":object['retrigger'],
      "element":object['element'],
    }

    alarm_list[datapoint]['alarm_logic_list'].append(alarm)
  logger.info("get_alarm_logic: done")


@socketio.on('get_alarm_rules', namespace='')
def get_alarm_rules(data):
  global alarm_list
  if len(alarm_list) == 0:
    get_alarm_logic()
  return json.dumps(alarm_list, indent=4)

@socketio.on('save_alarm_rules', namespace='')
def save_alarm_rules(data):
  local_alarm_list = json.loads(data)
  global mongoclient
  db = mongoclient.scada

  db.alarm_logic.drop()
  #db.createCollection("alarm_logic")
  for datapoint in local_alarm_list:
    for alarm in local_alarm_list[datapoint]['alarm_logic_list']:
      alarm['datapoint'] = datapoint
      db.alarm_logic.insert_one(alarm)
  
  global alarm_list
  alarm_list = local_alarm_list


### Event logic ###
def publish_event(element,msg,value):
  # IFS: rtu connect/discoonect (with additional values for substsation/bay info if available)
  # main: db's up/down, client connect/disconnect(not page refresh, but new session cookie)
  #   operate/select/cancel command and result (of action, and actual process)
  #   alarms trigger
  el = json.dumps(element)
  # print("-- element: %s, message: %s, value: %s" % (el, msg, str(value)))
  # add event item @ influxdb
  global influxdb_write_api
  p = Point("event").tag("element", el).field("message", msg).field("value", str(value))
  influxdb_write_api.write(bucket=event_bucket, record=p)
  socketio.emit('add_event_to_table', {'element':element, 'message':msg, 'value':value})


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

# retrieve RTU's from mongodb
@socketio.on('get_rtu_list', namespace='')
def get_RTU_list():
  global mongoclient
  db = mongoclient.scada
  cursor = db.rtu_list.find({})

  data = []
  for object in cursor:
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")
    data.append(object)

  return data


  # edit/add RTU's from mongodb
@socketio.on('edit_rtu', namespace='')
def add_RTU(rtu, enabled, IFS):
  global mongoclient
  db = mongoclient.scada
  newvalues =  {
      "enabled": enabled,
      "IFS": IFS,
    }
  _id = db.rtu_list.insert_one({"RTU":rtu}, {"$set": newvalues}, upsert=True)
  # ensure _id gets retrieved
  return "_" + str(_id.inserted_id)


  # delete RTU's from mongodb
@socketio.on('del_rtu', namespace='')
def del_RTU(uuid):
  global mongoclient
  db = mongoclient.scada
  db.rtu_list.delete_one({'_id':ObjectId(uuid[1:])})


###############################################################
###############################################################
###############################################################

#background thread
def worker():
  socketio.sleep(tick)
  logger.info("polling thread started")
  interval = 10
  interval_counter = 0
  while True:
    socketio.sleep(1)
    if influxdb_client == None: #mongoclient == None:
      logger.error("no db connection")
      socketio.sleep(10)
      continue

    for point in poll_datapoint:
      if poll_datapoint[point]['refCount'] > 0: # check if currently a client wants this datapoint updated

        value = get_value(point)  #value = influxdb_get_value(point)

        if value == None:
          value = 'UNKNOWN'

        # check if data changed since last check
        oldValue = poll_datapoint[point]['value']
        if oldValue != value or interval_counter % interval == 0: # update value, only if value was changed, and every 10 seconds (to keep client in sync)
          poll_datapoint[point]['value'] = value
          poll_dataUpdate(point, value)    
    logger.debug("values polled")
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

  try:
    mongoclient = pymongo.MongoClient('mongodb', 27017,  #'localhost', 27017, <- added mongodb to localhost for resolution of the replicaset, else there is a coonect error
      username="aaa",
      password="bbb", 
      authSource='scada', 
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

  try:
    rt_db = redis.Redis(host='localhost', port=6379, password="yourpassword")
    rt_pubsub = rt_db.pubsub()
    # TODO: should all keys be subscribed separately, and only when used, or filtered in python
    rt_pubsub.psubscribe(**{'__keyspace@0__:data:*': redis_dataUpdate})
    redis_event_thread = socketio.start_background_task(target=redis_events)
    logger.info("connected to redis")
  except:
    logger.error("there is an issue with redis db")
    rt_db = None


  try:
    influxdb_client = InfluxDBClient(url="http://127.0.0.1:8086", 
            token="_gJ3M3xVsoQKUFJTpFS4-OzEdGeNz2hKl_TJ2jXyfT4Tnf_QXTOWvS3z3sPfSqruhBEX0ztQkzJ8mmVQZpftzw==", 
            org="scada")
    influxdb_query_api = influxdb_client.query_api()

    influxdb_write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
  except:
    logger.error("there is an issue with influxdb")
    influxdb_client = None
    influxdb_write_api = None

  # get values
  get_value = influxdb_get_value
  #get_value = mongodb_get_value

  logger.info("starting webserver")
  #publish_event("system","webserver ready","ok")
  socketio.run(app,host="0.0.0.0")



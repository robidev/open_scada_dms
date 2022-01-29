#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit

import string
import logging

import pymongo
from bson import ObjectId
import redis
import uuid


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
app.secret_key = 'BAD_SECRET_KEY'


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


def redis_dataUpdate(msg):
  global rt_db
  if rt_db == None:
    logger.error("No redis db connected")
    return

  key = msg['channel'][15:]
  data = rt_db.get(key)
  key_u8 = key.decode("utf-8")[5:]
  data_u8 = data.decode("utf-8")
  
  logger.info("update",key_u8, data_u8)
  updateDataPoint( key_u8,data_u8) # emit to clients


def poll_dataUpdate(point, data):
  updateDataPoint(point,data) # emit to clients

###############################################

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
    svg = db.svg_templates.find_one({"name":object["svg"]})
    object["svg"] = '<svg xmlns="http://www.w3.org/2000/svg">' + string.Template(svg["svg"]).substitute(object['datapoints']) + "</svg>"
    object["id"] = "_" + str(object["_id"])
    object.pop("_id")
    data.append(object)

  return data


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
  socketio.emit("geojson_object_add_to_schema",geojson )
  

# load svg gis data
def query_schema_geojson(w,n,e,s,z):
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
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
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
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
  # perform a query, based on a x/y box, and z-depth
  # return list of svg items that fall within that box, thus should be drawn
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
  socketio.emit("geojson_object_add_to_gis",geojson )


# callbacks from libiec61850client
# called by client.poll
def readvaluecallback(key,data):
  logger.debug("callback: %s - %s" % (key,data))
  socketio.emit("svg_value_update_event_on_schema",{ 'element' : key, 'data' : data })


#background thread
def worker():
  global mongoclient
  socketio.sleep(tick)
  logger.info("polling treat started")
  interval = 10
  interval_counter = 0
  while True:
    socketio.sleep(1)
    if mongoclient == None:
      logger.error("no mongodb connection")
      socketio.sleep(10)
      continue

    for point in poll_datapoint:
      if poll_datapoint[point]['refCount'] > 0: # check if currently a client wants this datapoint
        # query mongodb for possible update
        db = mongoclient.scada
        data = None
        cursor = db.data_timeseries.find({'id':point}).sort([('timestamp', -1)]).limit(1) # find newest value
        for object in cursor:
          data = object
          break

        if data:
          value = data['value']
        else: # if value is not in mongodb, just give up (for now)
          value = 'UNKNOWN'

        # check if data changed since last check
        oldValue = poll_datapoint[point]['value']
        if oldValue != value or interval_counter % interval == 0: # update value, only if value was changed, and every 10 seconds (to keep client in sync)
          poll_datapoint[point]['value'] = value
          poll_dataUpdate(point, value)    
    logger.info("values polled")
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
    mongoclient = pymongo.MongoClient('localhost', 27017, 
      username="aaa",
      password="bbb", 
      authSource='scada', 
      authMechanism='SCRAM-SHA-256', 
      connect=True, 
      connectTimeoutMS=2000,
      socketTimeoutMS=2000)

    db = mongoclient.scada
    cursor = db.data_timeseries.find({}).limit(1) # find newest value
    for object in cursor:
      logger.info("connected to mongodb")

  except:
    logger.error("could not connect to mongodb")
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

  logger.info("starting webserver")
  socketio.run(app,host="0.0.0.0")




#/usr/bin/env python
#  
# datapoints of normal/fail are the sensor-nodes, or the nodes coming from this dataprovider if no sensor in this network-part :
#   properties: { "v_node_list" : [{ type, node },..] }
# transformers(geojson), within property is also the connection of both datapoints : 
#   properties: { "v_node_list" : [{ type, link1, link2},..] }
# switch within property is also the connection of both datapoints : 
#   properties: { "v_node_list" : [{ type, link1, link2, input},..] }
#
import logging, time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

import pymongo
from bson import ObjectId
import redis

value_bucket = "bucket_1"

# query all nodes in schema for properties, v_node_list
# for all results (all v_node_lists)
#    make dict of id : {type, node(s), (input), value=0, to_be_resolved=true}
#link = {
#    "type": "ext", # ext, link,
#    "uri": "iec60870-5-104://127.0.0.1:2404/MeasuredValueScaled/100", # URI
#    "value": 0,
#    "to_be_resolved": True
#}  links = {"1234567": link}
#node = {
#    "type": "coupling", # coupling, switch
#    "link1": get_link_byref(links, "iec60870-5-104://127.0.0.1:2404/MeasuredValueScaled/100"), # URI
#    "link2": get_link_byref(links, "solver://127.0.0.1/link/100"), # URI
#    "to_be_resolved": True
#    #"input":"iec60870-5-104://127.0.0.1:2404/DoublePointValue/100"
#}
#nodes = {"1234567": node}
def get_schema_data():
  global mongoclient
  if mongoclient == None:
    logger.error("no mongodb connection")
    return {}
  # perform a query, based on a x/y box, FUTURE TODO:  and z-depth
  # return list of svg items that (partly) fall within that box, thus should be drawn
  db = mongoclient.scada
  cursor1 = db.schema_objects.find(
    { 'properties.v_node_list': {'$exists': True } },
    { 'properties.v_node_list': 1 } 
    )

  links = {}
  nodes = {}
  for item in cursor1:
    for subkey, subitem in item['properties']['v_node_list'].items():
        subitem["to_be_resolved"] = True
        if subitem['type'] == "ext" or subitem['type'] == "link":
            subitem["value"] = 0
            links[str(item['_id']) + "_" + subkey ] = subitem
        if subitem['type'] == "coupling" or subitem['type'] == "switch":
            nodes[str(item['_id']) + "_" + subkey ] = subitem

  cursor2 = db.schema_geojson.find(
        { 'properties.v_node_list': {'$exists': True } } , 
        { 'properties.v_node_list': 1 } 
    )
  for item in cursor2:
    for subkey, subitem in item['properties']['v_node_list'].items():
        subitem["to_be_resolved"] = True
        if subitem['type'] == "ext" or subitem['type'] == "link":
            subitem["value"] = 0
            links[str(item['_id']) + "_" + subkey ] = subitem
        if subitem['type'] == "coupling" or subitem['type'] == "switch":
            nodes[str(item['_id']) + "_" + subkey ] = subitem
  return links, nodes




def get_network_mongodb():
    links, nodes = get_schema_data()

    # remove all id's of type link with duplicate node, slow, but ok for now
    temp = []
    result_link = dict()
    for key, link in links.items():
        if link['uri'] not in temp:
            temp.append(link['uri'])
            result_link[key] = link
        else:
            logger.warning("removed nonsensical link: "+ str(key) +", both links have same ref")
    links = result_link

    # remove nonsensical nodes, where both refs are the same, and
    # remove all id's of type coupling with both nodes duplicate + warn,  keep duplicate switch nodes, but warn

    temp = []
    result_nodes = dict()
    for key, node in nodes.items():
        if node['link1'] == node['link2']:
            logger.warning("removed nonsensical node: "+ str(key) +", both links have same ref")
            continue

        forward = node['type'] + "_" + node['link1'] + node['link2']
        reverse = node['type'] + "_" + node['link2'] + node['link1']    
        if forward in temp or reverse in temp:
            if node['type'] == "coupling":
                logger.warning("duplicate coupling, removing second one: " + str(key))
                continue
            else:
                logger.warning("duplicate switch: " + str(key) + ", keeping node")
        # append to resulting list
        temp.append(forward)
        temp.append(reverse)

        # remove nodes that reference to items that not resolve
        link1 = get_link_byref(links, node['link1'])
        if link1 == None:
            logger.warning("could not resolve link: " + str(node['link1']))
            continue
        node['link1'] = link1

        link2 = get_link_byref(links, node['link2'])
        if link2 == None:
            logger.warning("could not resolve link: " + str(node['link2']))
            continue
        node['link2'] = link2

        result_nodes[key] = node
    nodes = result_nodes

    return nodes, links #return 2 dicts, 1 of link/ext nodes, one of coupling/switch nodes


def get_link_byref(link_list, ref): 
    for link in link_list:
        if link_list[link]['uri'] == ref:
            return link_list[link] # TODO ensure a reference to the original object is passed, not a copy
    return None



def publish_signals(link_list):
    # copy dict over to redis, without ext values
    for link in link_list:
        if link_list[link]['type'] == "link":
            rt_db.set("data:" + link_list[link]['uri'], int(link_list[link]['value']) )


def get_datapoint_value(ref):
    #get datapoint value from redis or influxdb, 
    data = rt_db.get("data:" + ref )
    if data != None:
        return int(data.decode("utf-8"))

    influxdata = influxdb_get_value(ref)
    if influxdata != None:
        return influxdata
    return 0


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


def re_init(list):
    for item in list:
        list[item]['to_be_resolved'] = True


# update the calculation if a redis update event happened
def redis_dataUpdate(msg):
    global update
    # TODO: only update when an ext is updated
    update = True


# watch for changes in mongodb
def mongo_watch_changes(stream):
    if stream.alive:
        change = stream.try_next()
        # Note that the ChangeStream's resume token may be updated
        # even when no changes are returned.
        print("Current resume token: %r" % (stream.resume_token,))
        if change is not None:
            print("Change document: %r" % (change,))
            return True
        else:
            return False


def calculate_network(node_list, link_list):
    # take all sensors(i.e external datapoints), for these, voltage is known, init those nodes with that value, to-be-resolved = false
    for link in link_list:
        if link_list[link]['type'] == 'ext':
            try:
                link_list[link]['value'] = get_datapoint_value(link_list[link]['uri'])
                link_list[link]['to_be_resolved'] = False
            except Exception as e:
                logger.error("could not resolve datapoint value. Error:" + str(e))
    # all other links(i.e. own datapoint type) left as: to_be_resolved = true

    # check if all is resolved, or no mutations anymore
    resolved = 0
    while True:
        old_resolved = resolved # store result of previous iteration
        resolved = 0   # count amount of resolved nodes
        to_be_resolved = 0 # count amount of nodes to resolve

        for node in node_list:
            if node_list[node]['to_be_resolved'] == False: # already resolved
                resolved = resolved + 1 # count how many we skip
                continue
            to_be_resolved = to_be_resolved + 1
            
            link1 = node_list[node]['link1']
            link2 = node_list[node]['link2']

            if link1['to_be_resolved'] == True and link2['to_be_resolved'] == True: # nothing to solve if both unkown, wait until more info
                continue
            elif link1['to_be_resolved'] == False and link2['to_be_resolved'] == False: # both are known, nothing to be done, so dont try to resolve anymore this coupling/switch
                node_list[node]['to_be_resolved'] = False
                continue

            if node_list[node]['type'] == 'coupling':
                # one should here be tresolved, and the other not, if so, copy value, to-be-resolved = false of coupling, and link
                if link1['to_be_resolved'] == True:
                    link1['value'] = link2['value'] # FUTURE: value * ratio, 
                    link1['to_be_resolved'] = False
                if link2['to_be_resolved'] == True:
                    link2['value'] = link1['value'] # FUTURE: value * ratio,  
                    link2['to_be_resolved'] = False
                node_list[node]['to_be_resolved'] = False

            if node_list[node]['type'] == 'switch':
                # one should here be tresolved, and the other not, if so, check switch state
                conducting = get_datapoint_value(node_list[node]['input'])
                if conducting > 0: # if switch is conducting, copy value, else leave them unknown
                    if link1['to_be_resolved'] == True:
                        link1['value'] = link2['value'] 
                        link1['to_be_resolved'] = False
                    if link2['to_be_resolved'] == True:
                        link2['value'] = link1['value']   
                        link2['to_be_resolved'] = False
                node_list[node]['to_be_resolved'] = False
            # end type checks
            resolved = resolved + 1 # count how many we have done

        # end for loop for all nodes
        
        if to_be_resolved == 0 or old_resolved == resolved: # if true, no more (new) resolves, so quit
            break
    # end while loop for resove iterations


if __name__ == "__main__":
    global update

    logger = logging.getLogger('solver')
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

    #connect redis, mongodb and influxdb
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
        #stream_svg = db.schema_objects.watch()
        #stream_geo = db.schema_geojson.watch()
    except Exception as e:
        logger.error("mongodb: exception while initialising mongodb connection: " + str(e))
        mongoclient = None

    try:
        rt_db = redis.Redis(host='localhost', port=6379, password="yourpassword")
        #rt_pubsub = rt_db.pubsub()
        # TODO: should all keys be subscribed separately, and only when used, or filtered in python
        #rt_pubsub.psubscribe(**{'__keyspace@0__:data:*': redis_dataUpdate})
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


    # retrieve all unique items in mongodb, and put them in dict, based on type(link-node, ext, switch, coupling). dict contains node(s)
    node_list, link_list = get_network_mongodb()
    publish_signals(link_list) # publish link_list dict with id and value (ignore ext, as it is input) to redis

    update = True
    settime = 0
    while True:
        timer = int(time.monotonic())
        if update == True:
            re_init(node_list)
            re_init(link_list)        
            calculate_network(node_list, link_list)
            publish_signals(link_list)
            update = False
            settime = int(time.monotonic()) + 10
        # rerun calc periodic, 
        if timer > settime:
            update = True


        #if rt_pubsub == None:
        #    logger.error("no redis connection")
        #    continue
        #else:
        #    message = rt_pubsub.get_message()
        #    if message:
        #        logger.warning("missed event:" + str(message))
        #    else:
        #        time.sleep(0.01)
        # update calc if mongodb updates
        #if mongo_watch_changes(stream_svg) == True or mongo_watch_changes(stream_geo) == True:
        #    node_list, link_list = get_network_mongodb()
        #    update = True

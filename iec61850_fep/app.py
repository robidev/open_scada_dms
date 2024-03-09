#!/usr/bin/env python3

import os
import time
import sys
import logging
import redis
import libiec61850client

import pymongo

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

FEP_NAME = "FEP_A"
LIMIT = 100
update_datapoint = None
value_bucket = "bucket_1"

hosts_info = {}
async_msg = []
async_rpt = {}
INTERVAL = 0.1

#def update_datapoint_mongodb(tupl, ref, value):
#    global scada_database
#    data = {
#        "id":           "iec61850://" + tupl + "/" + ref,
#        "ied":          tupl,
#        "ref":          ref,
#        "value":        int(value),
#        "quality":      "good",
#        "timestamp":    int(time.time()*1000)
#    }
#    scada_database.data_timeseries.insert_one(data)

def update_datapoint_influxdb(ied, ref, value):
    global influxdb_write_api
    id = "iec61850://" + ied + "/" + ref

    p = Point("datapoint").tag("id", id).tag("quality", "good").field("value", int(value))
    influxdb_write_api.write(bucket=value_bucket, record=p)
    return


def callback(ied, data):
    global rt_db
    logger.debug("IED:" + ied + " - update:" + str(data))
    for key, value in data.items():
        set_data(ied,key, value['value'])

        
def set_data(ied,key,value):
    # push to realtime db
    rt_db.set("data:iec61850://"+ied+"/"+str(key), int(value))# {ied, type, ioa}{value, timestamp, quality}
    # push timeseries data to time series db 
    update_datapoint(ied, key, value)


def operate_handler(message):
    global iecclient
    logger.debug("> operate:"+str(message))
    # TODO: try/catch for int conversion
    iecclient.operate(message['channel'][8:].decode("utf-8") , int(message['data'].decode("utf-8")) )


def select_handler(message):
    global iecclient
    logger.debug("> select:"+str(message))
    # TODO: try/catch for int conversion
    iecclient.select(message['channel'][7:].decode("utf-8") , int(message['data'].decode("utf-8")) )


def cancel_handler(message):
    global iecclient
    logger.debug("> cancel:"+str(message))
    iecclient.cancel(str(id))



def fep_status(message):
    if message['data'].decode("utf-8") == FEP_NAME:
        logger.info("status fep:"+str(message))


def get_IED(ied):
    global iecclient
    _ied = ied.split(":")
    ip = _ied[0]
    if len(_ied) > 1:
        port = int(_ied[1])
    else:
        port = 102

    return iecclient.getIED(ip, port)


def remove_IED(ied):
    global iecclient
    _ied = ied.split(":")
    ip = _ied[0]
    if len(_ied) > 1:
        port = int(_ied[1])
    else:
        port = 102

    return iecclient.removeIED(ip, port)



# retrieve IED's from mongodb
def get_IED_list():
    global scada_database
    cursor = scada_database.dataprovider_list.find({"enabled": 1, "IFS": FEP_NAME}).distinct('dataprovider') # dataprovider is for this type of FEP an IED
    if len(cursor) > LIMIT:
        logger.error("too much IED's for this FEP. limit: %i, found: %i" % (LIMIT, len(cursor)))
    return cursor[:LIMIT]


# watch for changes in mongodb
def mongo_watch_changes(stream):
    if stream.alive:
        change = stream.try_next()
        # Note that the ChangeStream's resume token may be updated
        # even when no changes are returned.
        logger.debug("Current resume token: %r" % (stream.resume_token,))
        if change is not None:
            logger.debug("Change document: %r" % (change,))
            return True
        else:
            return False


# callbacks from libiec61850client
# called by client.poll
def readvaluecallback(key,data):
    logger.debug("callback: %s - %s" % (key,data))

# callback commandtermination
def cmdTerm_cb(msg):
    async_msg.append(msg)

# callback report
def Rpt_cb(key, value):
    async_rpt[key] = value
    readvaluecallback(key,value)


def read_value(id):
    logger.debug("read value:" + str(id)  )
    return iecclient.ReadValue(id)


def write_value(id, value):
    global iecclient
    logger.debug("write value:" + str(value) + ", element:" + str(id) )
    retValue = iecclient.registerWriteValue(str(id),str(value))
    if retValue > 0:
        return retValue, libiec61850client.IedClientError(retValue).name
    if retValue == 0:
        return retValue, "no error"
    return retValue, "general error"



################################################################
if __name__ == '__main__':
    logger = logging.getLogger('iec61850_fep')
    logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        level=logging.INFO)

    logger.info("starting iec61850 fep")

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


    #connect redis, mongodb and influxdb
    try:
        mongodb_client = pymongo.MongoClient(host=mongodb_host, port=27017,  #'localhost', 27017, <- added mongodb to localhost for resolution of the replicaset, else there is a coonect error
            username=mongodb_username,
            password=mongodb_password, 
            authSource=mongodb_db, 
            authMechanism='SCRAM-SHA-256', 
            connect=True, 
            connectTimeoutMS=2000,
            socketTimeoutMS=2000)
        logger.info("connected to mongodb")
        scada_database = mongodb_client.scada
    except Exception as e:
        logger.error("mongodb: exception while initialising mongodb connection: " + str(e))
        mongodb_client = None
        exit(-1)

    try:
        rt_db = redis.Redis(host=redis_host, port=6379, password=redis_password)
        logger.info("connected to redis")
        #subscribe redis events for select/operate
        call_p = rt_db.pubsub()
        call_p.subscribe(**{ "ifs_status": fep_status })
        thread = call_p.run_in_thread(sleep_time=0.001)
    except:
        logger.error("there is an issue with redis db")
        rt_db = None
        exit(-1)

    try:
        influxdb_client = InfluxDBClient(url=influxdb_host, 
                token=influxdb_api, 
                org=influxdb_org)
        influxdb_write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    except:
        logger.error("there is an issue with influxdb")
        exit(-1)


    logger.info("init")


    iecclient = libiec61850client.iec61850client(readvaluecallback, logger, cmdTerm_cb, Rpt_cb)
    update_datapoint = update_datapoint_influxdb #update_datapoint_mongodb

    ied_list = get_IED_list() 
    logger.info("ieds:" + str(ied_list) )
    
    stream = scada_database.dataprovider_list.watch()

    #reset all IED's
    for ied in ied_list:
        rt_db.set("connections:"+ied+".active", b'0')
        set_data(ied,"status", 0) # set status datapoint to offline, if we initialise the IED

    logger.info("init done: %s" % str(ied_list))

    #########################################
    #########################################
    # query all data elements for this list of IED's
    #query(ied_list):
    #  for each ied, get_all_unique_datapoints_from_mongo_and_alarms() OR only enable RCB, and parse all reports as they come
    #    iecclient.registerReadValue(datpoint)
    #
    #ieds = iecclient.getRegisteredIEDs()
    #for key in ieds:
    #    tupl = key.split(':')
    #    hostname = tupl[0]

    #    port = None
    #    if len(tupl) > 1 and tupl[1] != "":
    #        port = int(tupl[1])
    #    #model = client.getDatamodel(hostname=hostname, port=port)
    ##########################################
    ##########################################


    while True:
        time.sleep(1)

        #iecclient.poll()
        #logger.debug("values polled")
        
        for key in list(async_rpt):
            val = async_rpt.pop(key)
            logger.debug("%s updated via report" % key)

        # watchdog signal
        rt_db.publish("fep_status_online",FEP_NAME)
        # watch datapoint table in mongo for additions/removals (add/remove IED on update)
        if mongo_watch_changes(stream) == True:
            new_ied_list = get_IED_list() 
            # check if new_list removed some connections, if so disconnect that IED
            remove = set(list(ied_list)) - set(list(new_ied_list))
            for rem_ied in remove:
                logger.info("removing IED:" + rem_ied)
                set_data(rem_ied,"status", 0) # set status datapoint to offline, if we remove the IED
                remove_IED(rem_ied)
                rem_oper = "operate:%s" % ("iec61850://" + rem_ied + "/*")
                rem_sel = "select:%s" % ("iec61850://" + rem_ied + "/*")
                rem_cnl = "cancel:%s" % ("iec61850://" + rem_ied + "/*")
                call_p.unsubscribe(rem_oper)
                call_p.unsubscribe(rem_sel)
                call_p.unsubscribe(rem_cnl)
            ied_list = new_ied_list

        for ied in ied_list:
            #found enabled datapoint, so connect to IED
            ied_on = rt_db.get("connections:"+ied+".active")
            if ied_on == b'1':
                # perform periodic testframe to check connection of all IED, set status in redis
                if get_IED(ied) == -1:
                    rt_db.set("connections:"+ied+".active", b'0') # reset status if testframe returns -1
                    set_data(ied,"status", 0) # set status datapoint to offline, if we were connected, and now are not
            else:
                if get_IED(ied) == 0: # register and connect IED's, set status in redis (0 is ok, -1 is fail)
                    logger.info("IED connected:"+ied)
                    rt_db.set('connections:'+ied+".active", b'1')
                    set_data(ied,"status", 1) # set status datapoint to online, if we were not connected, and now are
                    # register this FEP with IED
                    oper = "operate:%s" % ("iec61850://" + ied + "/*")
                    sel = "select:%s" % ("iec61850://" + ied + "/*")
                    cancl = "cancel:%s" % ("iec61850://" + ied + "/*")
                    call_p.psubscribe(**{
                            oper:operate_handler, 
                            sel:select_handler, 
                            cancl:cancel_handler, 
                        })
                else:
                    logger.debug("failed to connect IED:"+ied)
                    # retry periodically, set status in redis
                    rt_db.set("connections:"+ied+".active", b'0')


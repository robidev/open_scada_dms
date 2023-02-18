#!/usr/bin/env python3

import os
import time
import sys
import logging
import redis
import libiec60870client

import pymongo

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

IFS_NAME = "IFS_A"
LIMIT = 100
update_datapoint = None
value_bucket = "bucket_1"

# CP16Time2a - milisecond(int)
# CP24Time2a - milisecond(int), minute(int), invalid(bool), substitute(bool)
# CP32Time2a - milisecond(int), minute(int), hour(int), summertime(bool), invalid(bool), substitute(bool)
# CP56Time2a - milisecond(int), minute(int), hour(int), summertime(bool), dayofweek(int), (dayofmonth), year(int), invalid(bool), substitute(bool)
# only CP56Time2a should be used in IEC60870-5-104

def getAsduName(datatype):
    if datatype == 1:
        return "SinglePointInformation" # 	            M_SP_NA_1; 1 (bool)
    if datatype == 3:
        return "DoublePointInformation" #	            M_DP_NA_1; 3 (2 bits enum)
    if datatype == 7:
        return "BitString32" #                          M_BO_NA_1; 7 (bits, max 32 bits )
    if datatype == 9:
        return "MeasuredValueNormalized" #              M_ME_NA_1; 9 (float normalized value between -1 and 1)
    if datatype == 11:
        return "MeasuredValueScaled" #		            M_ME_NB_1; 11 (int between -32.768 and 32.767)
    if datatype == 13:
        return "MeasuredValueShort" #                   M_ME_NC_1; 13 (float value)
    if datatype == 35:
        return "MeasuredValueScaled_CP56Time2a" #       M_ME_TE_1; 35 (int between -32.768 and 32.767 with timestamp)
    if datatype == 45:
        return "SinglePointCommand" #		            C_SC_NA_1; 45 (bool)
    if datatype == 46:
        return "DoublePointCommand" #		            C_DC_NA_1; 46 (2 bits enum)
    if datatype == 47:        
        return "RegulatingStepCommand" #                C_RC_NA_1; 47 (0=invalid, 1=lower, 2=higher, 3=invalid)
    if datatype == 48:
        return "SetpointCommandNormalized" #            C_SE_NA_1; 48 (float normalized value between -1 and 1)
    if datatype == 49:
        return "SetpointCommandScaled" #                C_SE_NB_1; 49 (int between -32.768 and 32.767)
    if datatype == 50:
        return "SetpointCommandShort" #                 C_SE_NC_1; 50 (float value)
    if datatype == 51:
        return "BitstringCommand" #                     C_BO_NA_1; 51 (bits, max 32 bits )
    if datatype == 107:
        return "TestCommand_CP56Time2a" #	            C_TS_TA_1; 107
    if datatype == 256:
        return "status" #	                            RTU status type, not mapped in IEC60870 standard, used for device status datapoint in IFS

datatypes_match = {
    "SinglePointCommand": "SinglePointInformation",
    "DoublePointCommand": "DoublePointInformation",
    "SetpointCommandNormalized":"MeasuredValueNormalized",
    "SetpointCommandScaled":"MeasuredValueScaled",
    "SetpointCommandShort":"MeasuredValueShort",
    "BitstringCommand":"BitString32"
}

#def update_datapoint_mongodb(tupl, ioa, ASDU, value):
#    global scada_database
#    data = {
#        "id":           "iec60870-5-104://" + tupl + "/" + getAsduName(ASDU) + "/" + str(ioa),
#        "rtu":          tupl,
#        "ioa":          ioa,
#        "value":        int(value),
#        "ASDU":         ASDU,
#        "quality":      "good",
#        "timestamp":    int(time.time()*1000)
#    }
#    scada_database.data_timeseries.insert_one(data)

def update_datapoint_influxdb(rtu, ioa, ASDU, value):
    global influxdb_write_api
    id = "iec60870-5-104://" + rtu + "/" + getAsduName(ASDU) + "/" + str(ioa)

    p = Point("datapoint").tag("id", id).tag("quality", "good").field("value", int(value))
    influxdb_write_api.write(bucket=value_bucket, record=p)
    return


def callback(tupl, data):
    global rt_db
    logger.debug("RTU:" + tupl + " - update:" + str(data))
    for key, value in data.items():
        set_data(tupl,value['ASDU'],key, value['value'])

        
def set_data(rtu,ASDU,key,value):
    # push to realtime db
    rt_db.set("data:iec60870-5-104://"+rtu+"/"+getAsduName(ASDU)+"/"+str(key), int(value))# {rtu, type, ioa}{value, timestamp, quality}
    # push timeseries data to time series db 
    update_datapoint(rtu, key, ASDU, value)


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


def ifs_status(message):
    if message['data'].decode("utf-8") == IFS_NAME:
        logger.info("status ifs:"+str(message))


def get_RTU(rtu):
    global iecclient
    _rtu = rtu.split(":")
    ip = _rtu[0]
    if len(_rtu) > 1:
        port = int(_rtu[1])
    else:
        port = 2404

    return iecclient.getRTU(ip, port)


def remove_RTU(rtu):
    global iecclient
    _rtu = rtu.split(":")
    ip = _rtu[0]
    if len(_rtu) > 1:
        port = int(_rtu[1])
    else:
        port = 2404

    return iecclient.removeRTU(ip, port)


# send a testframe
def testframe(rtu):
    global iecclient
    _rtu = rtu.split(":")
    ip = _rtu[0]
    if len(_rtu) > 1:
        port = int(_rtu[1])
    else:
        port = 2404

    return iecclient.testframe(ip,port)


# retrieve RTU's from mongodb
def get_RTU_list():
    global scada_database
    cursor = scada_database.dataprovider_list.find({"enabled": 1, "IFS": IFS_NAME}).distinct('dataprovider') # dataprovider is for this type of IFS an RTU
    if len(cursor) > LIMIT:
        logger.error("too much RTU's for this IFS. limit: %i, found: %i" % (LIMIT, len(cursor)))
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



################################################################
if __name__ == '__main__':
    logger = logging.getLogger('ifs')
    logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        level=logging.INFO)

    logger.info("starting IFS")

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
        call_p.subscribe(**{ "ifs_status": ifs_status })
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
    iecclient = libiec60870client.IEC60870_5_104_client(callback)
    update_datapoint = update_datapoint_influxdb #update_datapoint_mongodb

    rtu_list = get_RTU_list() 
    logger.info("rtus:" + str(rtu_list) )
    
    stream = scada_database.dataprovider_list.watch()

    #reset all RTU's
    for rtu in rtu_list:
        rt_db.set("connections:"+rtu+".active", b'0')
        set_data(rtu,256,1, 0) # set status datapoint to offline, if we initialise the RTU

    logger.info("init done: %s" % str(rtu_list))

    while True:
        time.sleep(1)
        # watchdog signal
        rt_db.publish("ifs_status_online",IFS_NAME)
        # watch datapoint table in mongo for additions/removals (add/remove RTU on update)
        if mongo_watch_changes(stream) == True:
            new_rtu_list = get_RTU_list() 
            # check if new_list removed some connections, if so disconnect that RTU
            remove = set(list(rtu_list)) - set(list(new_rtu_list))
            for rem_rtu in remove:
                logger.info("removing RTU:" + rem_rtu)
                set_data(rem_rtu,256,1, 0) # set status datapoint to offline, if we remove the RTU
                remove_RTU(rem_rtu)
                rem_oper = "operate:%s" % ("iec60870-5-104://" + rem_rtu + "/*")
                rem_sel = "select:%s" % ("iec60870-5-104://" + rem_rtu + "/*")
                rem_cnl = "cancel:%s" % ("iec60870-5-104://" + rem_rtu + "/*")
                call_p.unsubscribe(rem_oper)
                call_p.unsubscribe(rem_sel)
                call_p.unsubscribe(rem_cnl)
            rtu_list = new_rtu_list

        for rtu in rtu_list:
            #found enabled datapoint, so connect to RTU
            rtu_on = rt_db.get("connections:"+rtu+".active")
            if rtu_on == b'1':
                # perform periodic testframe to check connection of all RTU, set status in redis
                if testframe(rtu) == -1:
                    rt_db.set("connections:"+rtu+".active", b'0') # reset status if testframe returns -1
                    set_data(rtu,256,1, 0) # set status datapoint to offline, if we were connected, and now are not
            else:
                if get_RTU(rtu) == 0: # register and connect RTU's, set status in redis (0 is ok, -1 is fail)
                    logger.info("RTU connected:"+rtu)
                    rt_db.set('connections:'+rtu+".active", b'1')
                    set_data(rtu,256,1, 1) # set status datapoint to online, if we were not connected, and now are
                    # register this IFS with RTU
                    oper = "operate:%s" % ("iec60870-5-104://" + rtu + "/*")
                    sel = "select:%s" % ("iec60870-5-104://" + rtu + "/*")
                    cancl = "cancel:%s" % ("iec60870-5-104://" + rtu + "/*")
                    call_p.psubscribe(**{
                            oper:operate_handler, 
                            sel:select_handler, 
                            cancl:cancel_handler, 
                        })
                else:
                    logger.debug("failed to connect RTU:"+rtu)
                    # retry periodically, set status in redis
                    rt_db.set("connections:"+rtu+".active", b'0')


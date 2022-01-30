#!/usr/bin/env python3

import os
import time
import sys
import redis
import libiec60870client

from pymongo import MongoClient

IFS_NAME = "IFS_A"
LIMIT = 100


def getAsduName(ASDU):
    if ASDU == 1:
        return "SinglePointInformation" # 	M_SP_NA_1; 1
    if ASDU == 3:
        return "DoublePointInformation" #	M_DP_NA_1; 3
    if ASDU == 11:
        return "MeasuredValueScaled" #		M_ME_NB_1; 11
    if ASDU == 35:
        return "MeasuredValueScaled_CP56Time2a" #M_ME_TE_1; 35
    if ASDU == 45:
        return "SinglePointCommand" #		C_SC_NA_1; 45
    if ASDU == 46:
        return "DoublePointCommand" #		C_DC_NA_1; 46
    if ASDU == 107:
        return "TestCommand_CP56Time2a" #	C_TS_TA_1; 107



def callback(tupl, data):
    global rt_db
    global db
    print("RTU:" + tupl + " - update:" + str(data))
    for key, value in data.items():
        rt_db.set("data:iec60870-5-104://"+tupl+"/"+getAsduName(value['ASDU'])+"/"+str(key), int(value['value']))# {rtu, type, ioa}{value, timestamp, quality}
        # push timeseries data to mongodb 
        data = {
            "id":           "iec60870-5-104://" + tupl + "/" + getAsduName(value['ASDU']) + "/" + str(key),
            "rtu":          tupl,
            "ioa":          key,
            "value":        int(value['value']),
            "ASDU":         value['ASDU'],
            "quality":      "good",
            "timestamp":    int(time.time()*1000)
        }
        db.data_timeseries.insert_one(data)


def operate_handler(message):
    global iecclient
    print("> operate:"+str(message))
    # TODO: try/catch for int conversion
    iecclient.operate(message['channel'][8:].decode("utf-8") , int(message['data'].decode("utf-8")) )


def select_handler(message):
    global iecclient
    print("> select:"+str(message))
    # TODO: try/catch for int conversion
    iecclient.select(message['channel'][7:].decode("utf-8") , int(message['data'].decode("utf-8")) )

def cancel_handler(message):
    global iecclient
    print("> cancel:"+str(message))


def ifs_status(message):
    print("ifs:"+str(message))


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
def get_RTU_list(db):
    cursor = db.rtu_list.find({"enabled": 1, "IFS": IFS_NAME}).distinct('RTU')
    if len(cursor) > LIMIT:
        print("too much RTU's for this IFS. limit: %i, found: %i" % (LIMIT, len(cursor)))
    return cursor[:LIMIT]


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



################################################################

iecclient = libiec60870client.IEC60870_5_104_client(callback)
print("start")

if len(sys.argv) == 1:
    print("localhost")
    #client = MongoClient('localhost', 27017)
    client = MongoClient('localhost', 27017, username="aaa",password="bbb", authSource='scada', authMechanism='SCRAM-SHA-256')
#    rt_db = redis.Redis(host='localhost', port=6379)
    rt_db = redis.Redis(host='localhost', port=6379, password="yourpassword")
else:
    print("remote")
    #client = MongoClient('mongo', 27017)
    client = MongoClient(os.environ['IFS_MONGODB_HOST'], 27017, username=os.environ['IFS_MONGODB_USERNAME'],password=os.environ['IFS_MONGODB_PASSWORD'], authSource='scada', authMechanism='SCRAM-SHA-256')
#    rt_db = redis.Redis(host='redis', port=6379)
    rt_db = redis.Redis(host=os.environ['IFS_REDIS_HOST'], port=6379, password=os.environ['IFS_REDIS_PASSWORD'])

db = client.scada
print("init")

#subscribe redis events for select/operate
call_p = rt_db.pubsub()
call_p.subscribe(**{ "ifs_status": ifs_status })
thread = call_p.run_in_thread(sleep_time=0.001)

rtu_list = get_RTU_list(db) 
stream = db.rtu_list.watch()

#reset all RTU's
for rtu in rtu_list:
    rt_db.set("connections:"+rtu+".active", b'0')

print("init done: %s" % str(rtu_list))

while True:
    time.sleep(1)
    # watch datapoint table in mongo for additions/removals (add/remove RTU on update)
    if mongo_watch_changes(stream) == True:
        new_rtu_list = get_RTU_list(db) 
        # check if new_list removed some connections, if so disconnect that RTU
        remove = set(list(rtu_list)) - set(list(new_rtu_list))
        for rem_rtu in remove:
            print("removing RTU:" + rem_rtu)
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
        else:
            if get_RTU(rtu) == 0: # register and connect RTU's, set status in redis
                print("RTU connected:"+rtu)
                rt_db.set('connections:'+rtu+".active", b'1')
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
                print("failed to connect RTU:"+rtu)
                # retry periodically, set status in redis
                rt_db.set("connections:"+rtu+".active", b'0')


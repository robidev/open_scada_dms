#!/usr/bin/env python3

#
# A very simple dataprovider. it will retrieve the latest datapoints from the historical database(influxdb)
# and publish them on the realtime db(redis)
# During operation, it will subscribe to any oper commands, and write its value to the historical database
# and the realtime db
# the format to address this dataprovider is static://local/, as it contains static data, and is a local dataprovider
# anything in the uri behind it, will work, but values send must be numerical for influxdb
#

import os
import time
import sys
import redis
import logging

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

update_datapoint = None
value_bucket = "bucket_1"


def update_datapoint_influxdb(channel, value):
    global influxdb_write_api
    global value_bucket
    id = channel
    #TODO: store quality and timestamp from 'value'. should be in format of: {'value':1, 'quality':'good', 'time':'2023/01/03 - 13:37:05.003'}
    p = Point("datapoint").tag("id", id).tag("quality", "good").field("value", int(value))
    influxdb_write_api.write(bucket=value_bucket, record=p)
    return


def influxdb_get_value(point):
  global influxdb_query_api
  global value_bucket
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


def influxdb_get_datapoints():
  global influxdb_query_api
  global value_bucket
  # query influxdb for possible update: static://local/
  query = ' from(bucket:"' + value_bucket + '")\
    |> range(start: 0)\
    |> sort(columns: ["_time"], desc: true) \
    |> filter(fn:(r) => r._measurement == "datapoint")\
    |> filter(fn: (r) => r.id =~ /static:\/\/local\// )\
    |> unique(column: "id") '

  result = influxdb_query_api.query(org="scada", query=query)
  if result and len(result) > 0:
    return result
  return None


def operate_handler(item):
    global rt_db
    logger.info("oper:" + str(item))
    ref = item['channel'].decode("utf-8") 
    if ref.startswith("operate:"):
        channel = ref[8:]
        data = item['data'].decode("utf-8") 
        rt_db.set("data:"+channel, data)
        # push timeseries data to time series db 
        update_datapoint(channel, data)
    else:
        logger.error("could not parse set request")


def dataprovider_status(message):
    logger.info("dataprovider OK:"+str(message))


################################################################
if __name__ == '__main__':
    logger = logging.getLogger('static_dataprovider')
    logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)

    update_datapoint = update_datapoint_influxdb
    logger.info("starting static_dataprovider")

    if len(sys.argv) == 1:
        logger.info("using localhost config")
        rt_db = redis.Redis(host='localhost', port=6379, password="yourpassword")

        influxdb_client = InfluxDBClient(url="http://127.0.0.1:8086", 
            token="iRiuItNtMZYMLQjbMhWYjPReKOe2PbIWzHVl98GHCwBN1WpVwYK_aKmRh99qvRTPg3pFc5CW97Y1QXEbmdtp0w==", #"_gJ3M3xVsoQKUFJTpFS4-OzEdGeNz2hKl_TJ2jXyfT4Tnf_QXTOWvS3z3sPfSqruhBEX0ztQkzJ8mmVQZpftzw==", 
            org="scada")
    else:
        logger.info("using docker config")
        rt_db = redis.Redis(host=os.environ['IFS_REDIS_HOST'], port=6379, password=os.environ['IFS_REDIS_PASSWORD'])

        influxdb_client = InfluxDBClient(url="http://influxdb:8086", 
            token="iRiuItNtMZYMLQjbMhWYjPReKOe2PbIWzHVl98GHCwBN1WpVwYK_aKmRh99qvRTPg3pFc5CW97Y1QXEbmdtp0w==", #"_gJ3M3xVsoQKUFJTpFS4-OzEdGeNz2hKl_TJ2jXyfT4Tnf_QXTOWvS3z3sPfSqruhBEX0ztQkzJ8mmVQZpftzw==", 
            org="scada")

    influxdb_write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    influxdb_query_api = influxdb_client.query_api()

    # subscribe redis events for operate
    call_p = rt_db.pubsub()
    call_p.subscribe(**{ "ifs_status": dataprovider_status })
    thread = call_p.run_in_thread(sleep_time=0.001)

    oper = "operate:%s" % ("static://local/*")
    call_p.psubscribe(**{ oper:operate_handler })

    # update redis with historic influxdb data
    result = influxdb_get_datapoints()
    if result != None:
        for table in result:
            for record in table.records:
                value = record.get_value() # return first result
                point = record.values.get("id")
                logger.info("set redis item:"+str(point)+" with value:"+str(value))
                rt_db.set("data:"+point, int(value))#

    logger.info("init done")

    while True:
        time.sleep(1)

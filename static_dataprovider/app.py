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
import pickle

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

    logger.info("starting static_dataprovider")

    redis_host = 'localhost'
    redis_password = "redis_secret"

    influxdb_host = "http://127.0.0.1:8086"
    influxdb_api = "influxdb_secret"
    influxdb_org = "scada"

    export_file = "./saved_static_datapoints.pkl"

    if len(sys.argv) > 1:
        if sys.argv[1] == "remote":
            logger.info("remote host parameters (for inside docker-compose network)")
            redis_host = os.environ['IFS_REDIS_HOST']
            redis_password = os.environ['IFS_REDIS_PASSWORD']

            influxdb_host = os.environ['IFS_INFLUXDB_HOST'] #"http://influxdb:8086"
            influxdb_api = os.environ['IFS_INFLUXDB_API']
            influxdb_org = os.environ['IFS_INFLUXDB_ORG']

    try:
        rt_db = redis.Redis(host=redis_host, port=6379, password=redis_password)
        logger.info("connected to redis")
          # subscribe redis events for operate
        call_p = rt_db.pubsub()
        call_p.subscribe(**{ "ifs_status": dataprovider_status })
        thread = call_p.run_in_thread(sleep_time=0.001)

        oper = "operate:%s" % ("static://local/*")
        call_p.psubscribe(**{ oper:operate_handler })
    except:
        logger.error("there is an issue with redis db")
        rt_db = None
        exit(-1)

    try:
        influxdb_client = InfluxDBClient(url=influxdb_host, 
                token=influxdb_api, 
                org=influxdb_org)
        influxdb_write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
        influxdb_query_api = influxdb_client.query_api()
    except:
        logger.error("there is an issue with influxdb")
        exit(-1)


    update_datapoint = update_datapoint_influxdb

    # import/export default values
    if len(sys.argv) > 2:
        if sys.argv[2] == "export":
            logger.info("exporting static values to:" + export_file)
            result = influxdb_get_datapoints()
            if result != None:
                dictionary = {}
                for table in result:
                    for record in table.records:
                        value = record.get_value() # return first result
                        point = record.values.get("id")
                        dictionary[point] = value
                with open(export_file, 'wb') as f:
                    pickle.dump(dictionary, f)
                    f.close()
            logger.info("export done")
            del influxdb_client
            del rt_db
            os._exit(0) # hard exit

        if sys.argv[2] == "import":
            logger.info("importing file:" + export_file)
            with open(export_file, 'rb') as f:
                loaded_dict = pickle.load(f)
                for item in loaded_dict:
                    logger.info("importing:" + str(item) + ", with value:" + str(loaded_dict[item]))
                    update_datapoint(item, loaded_dict[item] )
                f.close()
            logger.info("import done")
            del influxdb_client
            del rt_db
            os._exit(0) # hard exit

        if sys.argv[2] == "init":
            check_values = influxdb_get_datapoints()
            if check_values != None and len(check_values) > 0 and len(check_values[0].records) > 0:
                logger.info("static dataprovider value database has been initialised")
            else:
                logger.info("static dataprovider value database has not been initialised, importing defaults")
                logger.info("importing file:" + export_file)
                with open(export_file, 'rb') as f:
                    loaded_dict = pickle.load(f)
                    for item in loaded_dict:
                        logger.info("importing:" + str(item) + ", with value:" + str(loaded_dict[item]))
                        update_datapoint(item, loaded_dict[item] )
                    f.close()
                logger.info("import done, continuing execution")


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

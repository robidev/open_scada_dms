# This is a work in progress

# Open SCADA EMS/DMS
This is an open source project for a basic ems/dms scada system. It contains a HMI with vector graphics taylored towards power-scada, and supports an IEC60870-5-104 based IFS. 

## schema and gis
schema shows a schematic view of a power grid, with scroll and zoom capability. gis is data overlayed on a gographic map

data is live updated, and the view is animated. 


### editing schema and gis
SVG objects can be imported or chosen from a library. basic shapes can be drawn and styled based on datapoint values
the editor bars allow objects to be added, edited and removed. 
clicking an object allows to edit data regarding the coupling to datapoints

## alarms and events
alarms are shown in the alarms tab. alarm logic can be added, edited and removed via the edit button
alarms can be open or closed, and acknowledged and unacknowledged. only closed alarms are hidden from the view, but can be seen in the event log.
events are static, and can be viewed and sorted. more advanced analysis can be done in grafana 


## Inner workings
The backend is powered by mongodb for persistence, influxdb for time-series and historic data, and redis for the real-time database. 

The project is a collection of containers, and tries to mainly rely on actively developed projects that are fairly self contained.

The following containers are included:

container		purpose				port		username	password
scada			main application		http/5000	-		-
grafana			for historical data analysis	https/3000	-		-
admin-mongo 		for mongodb administation 	http/8081	admin		admin
redis-commander 	for redis administration  	http/8082	admin		admin
influxdb 		for influxdb administration	https/8086	admin		administrator
portainer		for docker administration	https/9443	admin		Administrator
ifs			for connection to RTU's		-		-		-


# Testing
##ifs:
IFS can be run on localhost or in a container. no argument means localhost, an argument(such as "remote") will assume it is run from a container

##test-gateway:
test_gateway can be used to simulate a gateway/RTU, and will open port 2404 to allow an IEC60870-5-104 connection from the IFS


# Databases
##redis
  does not need a schema. it needs a password: yourpassword

##mongodb 
  username=aaa, password=bbb, database=scada
  has multiple schemas:
    db.createCollection("rtu_list");		- list of rtu's for IFS
    db.createCollection("alarm_table");		- stored alarm data
    db.createCollection("alarm_logic");		- logic for triggering alarms
    db.createCollection("data_timeseries");	- legacy, stored values
    db.createCollection("svg_templates");	- svg templates to be used for schema and gis
    db.createCollection("schema_objects");	- svg objects for schematic
    db.createCollection("schema_geojson");	- geo objects for schematic
    db.createCollection("gis_objects");		- geo and svg objects for gis map


##influxdb 
  token: _gJ3M3xVsoQKUFJTpFS4-OzEdGeNz2hKl_TJ2jXyfT4Tnf_QXTOWvS3z3sPfSqruhBEX0ztQkzJ8mmVQZpftzw==
  has 2 buckets:
    bucket_1 - for timeseries data from IFS
    bucket_2 - for event data
  

# This is a work in progress

# Open SCADA EMS/DMS
This is an open source project for a basic ems/dms scada system. It contains a HMI(human-machine-interface) with vector graphics tailored towards power-scada, and supports an IEC60870-5-104 based IFS(the connection between the field devices and the central scada). 

## schema and gis
schema shows a schematic view of a power grid, with scroll and zoom capability. gis is data overlayed on a geographic map

data is live updated, and the view is animated. 


### editing schema and gis
SVG objects can be imported or chosen from a library. basic shapes can be drawn and styled based on datapoint values
the editor bars allow objects to be added, edited and removed. 
clicking an object allows to edit data regarding the coupling to datapoints

objects can have values overwritten during initialisation, using javascript entities. e.g. to overwrite svg tekst, use an array of dicts: `"overrides" : [{ "element_id": "svg_text", "property":"textContent", "value": "substation 1" }]`, 
```  "overrides": [
    {
      "element_id": "msr",
      "property": "style",
      "value": "stroke:blue;fill:blue"
    }
```
check the svg file for the id to use.

svg objects allow datapoints to be attached to control animations. based on the defined class in the svg element, certain animation id's are assumed. e.g. and XCBR and XSWI class element have an 'open' and 'close' animation. example:
```
  "datapoints": [
    {
      "static://local/DoublePointInformation/300": "datapoint_1"
    },
    {
      "static://local/DoublePointInformation/300": "datapoint_2"
    }
  ]

    "datapoints": [
    {
      "static://local/DoublePointInformation/300": "datapoint_1"
    },
    {
      "static://local/DoublePointCommand/6000": "datapoint_3"
    },
    {
      "static://local/DoublePointInformation/300": "datapoint_2"
    }
  ]
  ```
the "datapoint_*" element is defined as the (parent) element_id of the element that has the animation. it is found in the svg

all schema network elements have a 'normal' and 'fail' mode animation. normal is the normal color. fail turns the item white.

geojson objects can have logic attached to modify properties based on datapoints. example:
```
  "datapoints": [
    {
      "static://local/DoublePointInformation/300": [
        "color",
        ">",
        "1",
        "#00ffff"
      ]
    },
    {
      "static://local/DoublePointInformation/300": [
        "color",
        "<",
        "2",
        "#0000ff"
      ]
    }
  ]
```
datapoints contain lists of dicts regarding the modifications that should occur. the key is the datapoint reference to use as input. Then the following list is used:
template_item = {"datapoint":['<element-id>','<comparisson>','<value>',<value to assing to element-id>]} 
e.g. {"1":["color","gt","10","#00ff00"]}; ->  if(value > 10){color = '#00ff00';}

each object can be viewed or hidden at a certain zoom level. use z_min and z_max to define the zoom level the object should be
visible/hidden. the zoom level can be viewed in the url bar as part of the coordinate hash


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
static_dataprovider   for static datapoints
solver    for solving power flow in the network


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
  
# Solver

The solver can provide information about the network. By adding network information to the elements in the schema, it will resolve the unknown elements based on simple flow logic and the network topology. E.g. if a known voltage is on a wire, and a switch is connected, when the switch is closed, the other connected wire is set to the same voltage. coupling(such as Transformers) are also seen as connections. connected wires are seen as one.

you add network information by adding a v_node_list:[] as a property. example:

  "v_node_list": [
    {
      "type": "ext/link",
      "uri": "<datapoint>"
    },
    {
      "type": "coupling",
      "link1": "<datapoint>",
      "link2": "<datapoint>"
    },
    {
      "type": "switch",
      "link1": "<datapoint>",
      "link2": "<datapoint>",
      "input": "<datapoint>"
    }
  ]

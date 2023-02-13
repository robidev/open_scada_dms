# This is a work in progress

# Open SCADA EMS/DMS
This is an open source project for a basic ems/dms scada system. It contains a HMI(human-machine-interface) with vector graphics tailored towards power-scada, and supports an IEC60870-5-104 based IFS(the connection between the field devices and the central scada). 

[screenshot.png]

## TL;DR; I just want to start it

```
$ git clone https://github.com/robidev/open_scada_dms.git
$ cd open_scada_dms
$ sudo docker-compose up```

browse to http://127.0.0.1:5000

It might be that due to initialisation of the databases, some containers fail due to connection timeouts. Have a look in portainer (username: admin, password: administrator), and restart the stopped containers. Additionally, you can attempt another `$ sudo docker-compose up`

The system will start with an example configuration, and a simulated gateway. 

[diagram_test.drawio.png]

If you configure an additional dataprovider, such as an RTU, and connect it to
your system, it can connect to it.

[diagram_rtu.drawio.png]

if you wish a fully simulated environment, from physical process, to IED, to RTU and all the way up to DMS, you should do the following;

```
$ git clone https://github.com/robidev/iec61850_open_server.git
$ git clone https://github.com/robidev/iec61850_open_client.git
$ git clone https://github.com/robidev/iec61850_open_gateway.git
$ git clone https://github.com/robidev/open_scada_dms.git
```
then you define the gateway.yml in iec61850_open_gateway:
```
version: "3.3"
services:
  gateway:
    build:
      context: .
      dockerfile: Dockerfile.libiec61850_gateway
    hostname: gateway
    networks:
      subnetwork1:
        ipv4_address: 10.0.0.250
      scada_wannetwork:
        ipv4_address: 10.1.0.10
    privileged: true
    depends_on:
      - "ied1_xcbr"
      - "ied2_ptoc"
      - "ied3_smv"
      - "ied4_smv"

# networks should not be defined twice, or you get an error regarding missing subnet
networks:
  scada_wannetwork:
    driver: bridge
    external: true
```
and build the gateway by following the readme

then follow the readme of iec61850_open_server to build the substation and client.

next we start all containers regarding the substation from the iec61850_open_server directory:

`$ sudo docker-compose -f substation.yml -f substation.simulator.yml -f ../iec61850_open_gateway/gateway.yml up`

and finally, we start the open_scada_dms from the open_scada_dms directory:

`$ sudo docker-compose up mongodb influxdb redis grafana static_dataprovider ifs solver portainer scada_client`
(so omit the test_gateway, as you will be using the simulated one instead, and they sit on the same WAN IP; 10.1.0.10)

when you start the simulation on the iec61850_open_client via the web-interface, you should see values update on the open_scada_dms web interface.

[diagram_sim.drawio.png]


# usage

## schema and gis
schema shows a schematic view of a power grid, with scroll and zoom capability. gis is data overlayed on a geographic map

data is live updated, and the view is animated. 

### control
TODO

### grafana for historic analysis
TODO

## alarms and events
alarms are shown in the alarms tab. alarm logic can be added, edited and removed via the edit button
alarms can be open or closed, and acknowledged and unacknowledged. only closed alarms are hidden from the view, but can be seen in the event log.
events are static, and can be viewed and sorted. more advanced analysis can be done in grafana 

## dataproviders


# Editing

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

all schema network elements in the example have a 'normal' and 'fail' mode animation. normal is the normal color. fail turns the item white.

the operate dialog is triggered by making an svg element clickable, and calling the open_control(event, datapoint) function via onclick. the event is passed from the svg element. the datapoint should contain the element to operate on. the id of the svg element that is clicked is used as the associated status element. by convention it is easy to consider all interactive switches to contain 2 datapoint, e.g. swi_status and swi_oper. the oper element can be the same datapoint as the status. but with some protocols sich as iec60870-5-104 and modbus, it is common to write to a different point, than what reads the status.

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

## editing alarms




# general architecture

[scada.drawio.png]

The open_scada_dms attempts to approach some of the main functions of a real SCADA DMS system. However, it should probably not be used in production ,as I
provide no guarantee about its reliability. It is purely educational. That being said, the system shoul be able to scale, and supports a fully scalable,
redundant setup.

The main components and its ports are listed as follows;

[diagram_detail.drawio.png]


## Inner workings
portainer is the container orchestration

The backend is powered by mongodb for persistence, influxdb for time-series and historic data, and redis for the real-time database. 

The project is a collection of containers, and tries to mainly rely on actively developed projects that are fairly self contained.

The following containers are included:

container		purpose				port		username	password
scada_client			main application		http/5000	-		-
grafana			for historical data analysis	https/3000	-		-
admin-mongo 		for mongodb administation 	http/8081	admin		admin
redis-commander 	for redis administration  	http/8082	admin		admin
influxdb 		for influxdb administration	https/8086	admin		administrator
portainer		for docker administration	https/9443	admin		Administrator

ifs			for connection to RTU's		-		-		-
static_dataprovider   for static datapoints
solver    for solving power flow in the network

value initialisation is done on startup, and redis, influxdb and mongodb are persistent regarding data storage
.env stores all keys, credentials and other project specific environment variables


## Testing
### ifs:
IFS can be run on localhost or in a container. no argument means localhost, an argument(such as "remote") will assume it is run from a container

### test-gateway:
test_gateway can be used to simulate a gateway/RTU, and will open port 2404 to allow an IEC60870-5-104 connection from the IFS


## Databases
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
  
## Solver

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


## static_dataprovider

static:// for static values


## grafana
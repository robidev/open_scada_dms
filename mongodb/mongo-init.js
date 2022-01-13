db.createUser(
        {
            user: "aaa",
            pwd: "bbb",
            roles: [
                {
                    role: "readWrite",
                    db: "scada"
                }
            ]
        }
);
db = new Mongo().getDB("scada");

db.createCollection("rtu_list");
db.rtu_list.insert([
    { "RTU": "127.0.0.1:2404", "enabled":1, "IFS":"IFS_A" },
    { "RTU": "127.0.0.1:2405", "enabled":0, "IFS":"IFS_A" },
    { "RTU": "127.0.0.1:2406", "enabled":1, "IFS":"IFS_B" },
    { "RTU": "172.17.0.1:2404", "enabled":1, "IFS":"IFS_A" },
]);

db.createCollection("data_timeseries");

db.createCollection("svg_templates");
db.svg_templates.insert([
    { 
        "name": "rect", 
	"viewBox":"0 0 552 512",
        "datapoint_amount":0,
        "svg": "<rect fill=\"#000000\" id=\"canvas_background\" height=\"512\" width=\"552\" y=\"0\" x=\"0\"/>"
    },
]);

db.createCollection("schema_objects");
db.schema_objects.insert([
    { 
	"svg": "rect", 
	"w":0, 
	"n":0, 
	"e":552, 
	"s":512, 
	"datapoints": { "datapoint_1":"iec60870://111", "datapoint_2":"iec60870://222", "datapoint_3":"iec60870://333" }
    },
]);

db.createCollection("schema_geojson");
db.schema_geojson.insert([
    {
      "type": "Feature",
      "properties": {
        "id": "gis_1",
        "stroke": "#ad7fa8",
        "stroke-width": 2,
        "stroke-opacity": 1
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            5.842629075050354,
            51.980789872371176
          ],
          [
            5.841186046600342,
            51.98081300094364
          ],
          [
            5.841400623321533,
            51.97933605242088
          ]
        ]
      }
    },
]);


db.createCollection("gis_objects");
db.gis_objects.insert([
    { 
        "type": "Feature",
        "properties": {
	  "type":"Svg",
	  "svg": "rect", 
          "dataPoints": { "datapoint_1":"iec60870://111", "datapoint_2":"iec60870://222", "datapoint_3":"iec60870://333" }, 
        },
	"geometry": { 
	  "type": "Point", 
	  "coordinates": [ 5.84366, 51.978708 ], 
	  "height": 0.001, 
	  "width": 0.001 
        }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Coors Field",
        "id": "gis_1",
        "stroke": "#ad7fa8",
        "stroke-width": 2,
        "stroke-opacity": 1
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            5.842629075050354,
            51.980789872371176
          ],
          [
            5.841186046600342,
            51.98081300094364
          ],
          [
            5.841400623321533,
            51.97933605242088
          ],
          [
            5.843364000320434,
            51.9789891111414
          ],
          [
            5.8451128005981445,
            51.97930631470222
          ],
          [
            5.845075249671936,
            51.979986973095556
          ],
          [
            5.843181610107422,
            51.98002001450193
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": "gis_1",
        "stroke": "#729fcf",
        "stroke-width": 2,
        "stroke-opacity": 1,
        "fill": "#ef2929",
        "fill-opacity": 0.5
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              5.843503475189209,
              51.979742465930954
            ],
            [
              5.84347128868103,
              51.979303010510016
            ],
            [
              5.844458341598511,
              51.97937570268175
            ],
            [
              5.84447979927063,
              51.97972594512847
            ],
            [
              5.843911170959473,
              51.979887848730215
            ],
            [
              5.843503475189209,
              51.979742465930954
            ]
          ]
        ]
      }
    }
]);

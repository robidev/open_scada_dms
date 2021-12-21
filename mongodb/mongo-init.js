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
        "name": "ct", 
        "datapoint_amount":1,
        "svg": "<g id=\"S12/D1/Q1/I1\">\n<title>CTR</title>\n<text id=\"$datapoint_1\" class=\"MEAS\" data-text=\"Current: \\{value\\} A\" fill=\"#ffffff\" stroke=\"#ffffff\" x=\"291.851085\" y=\"125.166792\" font-size=\"12\" font-family=\"Helvetica, Arial, sans-serif\" text-anchor=\"start\" xml:space=\"preserve\" font-weight=\"normal\" font-style=\"normal\">current: {value} A</text>\n</g>" 
    },
    { 
        "name": "vt", 
        "datapoint_amount":1,
        "svg": "<g id=\"S12/E1/Q1/U1\">\n<title>VTR</title>\n<text id=\"$datapoint_1\" class=\"MEAS\" data-text=\"Voltage: \\{value\\} V\" fill=\"#ffffff\" stroke=\"#ffffff\" x=\"296\" y=\"244.499945\" font-size=\"12\" font-family=\"Helvetica, Arial, sans-serif\" text-anchor=\"start\" xml:space=\"preserve\" font-weight=\"normal\" font-style=\"normal\">voltage: {value} V</text>\n</g>"
    },
    { 
        "name": "cbr", 
        "datapoint_amount":3,
        "svg": "<g id=\"S12/E1/Q1/QA1\" class=\"draggable-group\">\n<title>CBR</title>\n<text id=\"$datapoint_1\"     class=\"MEAS\" data-text=\"CBR: QA1=\\{value\\}\" fill=\"#ffffff\" stroke=\"#ffffff\" x=\"296\" y=\"272.166593\" font-size=\"12\" font-family=\"Helvetica, Arial, sans-serif\" text-anchor=\"start\" xml:space=\"preserve\" font-weight=\"normal\" font-style=\"normal\"></text>\n<rect id=\"$datapoint_2\"     class=\"XCBR\" height=\"22.553162\" width=\"19.999974\" y=\"257.946454\" x=\"256.364398\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"#ffffff\">\n  <animate id=\"open\" attributeName=\"fill\" attributeType=\"XML\" to=\"black\" dur=\"100ms\" fill=\"freeze\" />\n  <animate id=\"transition\" attributeName=\"fill\" attributeType=\"XML\" to=\"green\" dur=\"10ms\" fill=\"freeze\" />\n  <animate id=\"close\" attributeName=\"fill\" attributeType=\"XML\"  to=\"white\" dur=\"100ms\" fill=\"freeze\" /> \n  <animate id=\"error\" attributeName=\"fill\" attributeType=\"XML\"  to=\"red\" dur=\"10ms\" fill=\"freeze\" />           \n</rect>\n<rect id=\"$datapoint_3\"     class=\"CSWI\" height=\"22.553162\" width=\"19.999974\" y=\"257.946454\" x=\"256.364398\" stroke-width=\"1.5\" stroke=\"none\" fill=\"none\"/>\n</g>"
    },
    { 
        "name": "swi", 
        "datapoint_amount":3,
        "svg": "<g id=\"S12/E1/Q1/QB1\" class=\"draggable-group\">\n<title>SWI</title>\n<text id=\"$datapoint_1\"     class=\"MEAS\" data-text=\"DIS: QB1=\\{value\\}\" fill=\"#ffffff\" stroke=\"#ffffff\" x=\"296\" y=\"314.666538\" font-size=\"12\" font-family=\"Helvetica, Arial, sans-serif\" text-anchor=\"start\" xml:space=\"preserve\" font-weight=\"normal\" font-style=\"normal\"></text>\n<rect id=\"$datapoint_2\"    class=\"CSWI\" height=\"19\" width=\"19\" y=\"300.49959\" x=\"256.864387\" stroke=\"#ffffff\" fill=\"#000000\"/> \n<line id=\"$datapoint_3\"     class=\"XSWI\" stroke=\"#ffffff\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"320\" x2=\"266\" y1=\"300\" x1=\"266\" stroke-width=\"4\" fill=\"none\">\n    <animateTransform id=\"open\" attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" to=\"90 266 310 \" dur=\"100ms\" fill=\"freeze\" />\n    <animateTransform id=\"close\" attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" to=\"0 266 310 \" dur=\"100ms\" fill=\"freeze\" />\n    <animateTransform id=\"transition\" attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" to=\"45 266 310 \" dur=\"100ms\" fill=\"freeze\" />\n    <animateTransform id=\"error\" attributeName=\"stroke\" attributeType=\"XML\" to=\"red\" dur=\"100ms\" fill=\"freeze\" />\n</line>\n</g>"
    },
    { 
        "name": "ptr", 
        "datapoint_amount":0,
        "svg": "<line id=\"S12/D1/Q1/L1\" class=\"LINE\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"153.934719\" x2=\"266\" y1=\"93.434721\" x1=\"266\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"none\"/>\n\n<g id=\"S12/D1/T1\">\n<title>PTR</title>\n<ellipse id=\"svg_T1_a\" ry=\"18\" rx=\"18\" cy=\"171.753014\" cx=\"266\" fill-opacity=\"null\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"none\"/>\n<text    id=\"svg_T1_name\" stroke=\"#ffffff\"  xml:space=\"preserve\" text-anchor=\"start\" font-family=\"Helvetica, Arial, sans-serif\" font-size=\"24\" y=\"186.66199\" x=\"296\" stroke-width=\"null\" fill=\"#ffffff\">T1</text>\n<ellipse id=\"svg_T1_b\" ry=\"18\" rx=\"18\" cy=\"196.290907\" cx=\"266\" fill-opacity=\"null\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"none\"/>\n</g>\n\n<line id=\"S12/E1/Q1/L2\" class=\"LINE\" stroke=\"#ffffff\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"256.43483\" x2=\"266\" y1=\"214.934859\" x1=\"266\" stroke-width=\"1.5\" fill=\"none\"/>\n"
    },
    { 
        "name": "feed", 
        "datapoint_amount":0,
        "svg": "<title>Bay 1</title>\n<text id=\"IFL\" class=\"IFL\" stroke=\"#ffffff\" xml:space=\"preserve\" text-anchor=\"middle\" font-family=\"Helvetica, Arial, sans-serif\" font-size=\"24\" y=\"80\" x=\"266\" fill=\"#ffffff\">220KV Feed</text>\n<ellipse id=\"svg_top\" stroke=\"#ffffff\" ry=\"2.424242\" rx=\"2.121212\" cy=\"91.858974\" cx=\"266\" fill-opacity=\"null\" stroke-width=\"1.5\" fill=\"none\"/>\n"
    },
    { 
        "name": "load", 
        "datapoint_amount":0,
        "svg": "<line id=\"S12/E1/W1/BB1\" class=\"LINE\" stroke=\"#ffffff\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"360\" x2=\"266\" y1=\"320.436511\" x1=\"266\" stroke-width=\"1.5\" fill=\"none\"/>\n<text id=\"LOAD\" class=\"LOAD\" stroke=\"#ffffff\"  xml:space=\"preserve\" text-anchor=\"middle\" font-family=\"Helvetica, Arial, sans-serif\" font-size=\"24\" y=\"380\" x=\"266\" fill=\"#ffffff\">Load</text>\n"
    },
    { 
        "name": "rect", 
        "datapoint_amount":0,
        "svg": "<rect fill=\"#000000\" id=\"canvas_background\" height=\"512\" width=\"552\" y=\"0\" x=\"0\"/>"
    },
]);

db.createCollection("schema_objects");
db.schema_objects.insert([
    { "svg": "rect", "x":0, "y":0, "x2":552, "y2":512, "datapoints": {} },
    { "svg": "feed", "x":0, "y":0, "x2":552, "y2":512, "datapoints": {} },
    { "svg": "ct",   "x":0, "y":0, "x2":552, "y2":512, "datapoints": { "datapoint_1":"aa" } },
    { "svg": "ptr",  "x":0, "y":0, "x2":552, "y2":512, "datapoints": {} },
    { "svg": "ct",   "x":0, "y":0, "x2":552, "y2":512, "datapoints": { "datapoint_1":"bb" } },
    { "svg": "vt",   "x":0, "y":0, "x2":552, "y2":512, "datapoints": { "datapoint_1":"cc" } },
    { "svg": "cbr",  "x":0, "y":0, "x2":552, "y2":512, "datapoints": { "datapoint_1":"111", "datapoint_2":"222", "datapoint_3":"333" } },
    { "svg": "swi",  "x":0, "y":0, "x2":552, "y2":512, "datapoints": { "datapoint_1":"444", "datapoint_2":"555", "datapoint_3":"666" } },
    { "svg": "load", "x":0, "y":0, "x2":552, "y2":512, "datapoints": {} },
]);

db.createCollection("gis_objects");
db.gis_objects.insert([
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

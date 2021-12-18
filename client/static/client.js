var socket, schema_panzoomcontrol, schema_svgRoot, schema_in_view, schema_svgElementData, gis_svgRoot, gis_in_view, gis_map, geojsonlayer;

function init_gis(){
  geojsonlayer = {};
  gis_svgRoot = {};
  gis_in_view = [];
  var gis_div = document.getElementById("gis_map");
  gis_div.style.display = "block";

  gis_map = L.map('gis_map', { renderer: L.svg()}).setView([51.980, 5.842], 17);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'openstreetmap',
    maxZoom: 20,
    id: 'openstreetmap',
    tileSize: 512,
    zoomOffset: -1,
  }).addTo(gis_map);
  geojsonlayer = L.geoJSON().addTo(gis_map);
  //register svg events
  gis_map.on('moveend', update_gis);
  gis_map.on('zoomend', update_gis);
  gis_map.setZoom(18);
}

function init_schema(){
  schema_svgElementData = {};
  schema_svgRoot = {};
  schema_in_view = [];
  //register data for svg
  var schema_map = document.getElementById("mmi_svg");
  schema_map.style.display = "block";
  //it's important to add an load event listener to the object, as it will load the svg doc asynchronously
  //but sometimes the svg loads before this event listener is created
  if(schema_map.getSVGDocument() == null){//normal situation where svg is loaded later
    schema_map.addEventListener("load",function(){ 
      var svgDoc = schema_map.contentDocument; //get the inner DOM of mmi.svg
      schema_svgRoot  = svgDoc.documentElement;
      schema_panzoomcontrol = svgPanZoom(schema_map, { 
        zoomEnabled: true, 
        controlIconsEnabled: true, 
        minZoom: 0.1, 
        onZoom: update_schema, 
        onPan: update_schema ,
        preventMouseEventsDefault: false,
        fit: false,
      });
      schema_panzoomcontrol.pan({x:75,y:20});
    },false);
  }
  else {//race condition, where svg is allready loaded from cache
    var svgDoc = schema_map.contentDocument; //get the inner DOM of mmi.svg
    schema_svgRoot  = svgDoc.documentElement;
    schema_panzoomcontrol = svgPanZoom(schema_map, { 
      zoomEnabled: true, 
      controlIconsEnabled: true, 
      minZoom: 0.1, 
      onZoom: update_schema, 
      onPan: update_schema ,
      preventMouseEventsDefault: false,
      fit: false,
    });
    schema_panzoomcontrol.pan({x:75,y:20});
  }
}

function deinit_schema(){
  var schema_map = document.getElementById("mmi_svg");
  schema_map.style.display = "none";
  schema_panzoomcontrol.destroy();
  schema_svgRoot.innerHTML = "";

  delete schema_panzoomcontrol;
  delete schema_svgElementData;
  delete schema_svgRoot;
  delete schema_in_view;
}

function deinit_gis(){
  var gis_div = document.getElementById("gis_map");
  gis_div.style.display = "none";
  gis_map.remove();
  gis_svgRoot.innerHTML = "";

  delete gis_svgRoot;
  delete gis_in_view;
  delete gis_map;
  delete geojsonlayer;
}

function toggle_view() {
  var gis = document.getElementById("gis_map");
  var schema = document.getElementById("mmi_svg");
  if (gis.style.display === "none") {
    deinit_schema();
    init_gis();
  } else {
    deinit_gis();
    init_schema();
  }
} 

$(document).ready(function() {
  namespace = '';


  socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

  init_schema();
  //init_gis();
  //deinit_gis();
  //deinit_schema();

  //add info to the ied/datamodel tab
  socket.on('svg_value_update_event_on_schema', function (data) {
    //event gets called from server when svg data is updated, so update the svg
    var element = data['element'];
    var value = data['data']['value'];
    var type = data['data']['type'];

    if(schema_svgRoot != null){//if the svg is loaded
      //check for each occurence of id, there can be multiple instances of the same id, with different classes
      $("#" + $.escapeSelector(element),schema_svgRoot).each(function(idx, el){
        var cl = el.classList.toString();


        if( cl == "MEAS"){
          if(el.dataset.size > 0 || typeof(el.dataset.text) === "undefined"){
            var desc = el.innerHTML;
            el.textContent = value;
          }
          else{
            var val = abbreviate_number(parseFloat(value),0)
            el.textContent = el.dataset.text.replace("{value}",val);
          }

        }
        if(cl == "XCBR" || cl == "XSWI"){
          if(type == 'boolean'){
            if(value=='True'){
              if(schema_svgElementData[el.id]['position'] != true) {
                $("#open",el)[0].beginElement();
                schema_svgElementData[el.id]['position'] = true;

                var ref = el.id;
                var sibling = $(el).siblings(".CSWI");//find a CSWI sibling, and operate on that instead
                if(sibling.length > 0){
                  ref = sibling[0].id;
                }
                schema_svgElementData[ref]['position'] = true;
              }
            }
            else{
              if(schema_svgElementData[el.id]['position'] != false){
                $("#close",el)[0].beginElement();
                schema_svgElementData[el.id]['position'] = false;

                var ref = el.id;
                var sibling = $(el).siblings(".CSWI");//find a CSWI sibling, and operate on that instead
                if(sibling.length > 0){
                  ref = sibling[0].id;
                }
                schema_svgElementData[ref]['position'] = false;
              }
            }
          }
          if(type == 'bit-string'){
            if(value == '1'){
              if(schema_svgElementData[el.id]['position'] != false) {
                $("#close",el)[0].beginElement();
                schema_svgElementData[el.id]['position'] = false;

                var ref = el.id;
                var sibling = $(el).siblings(".CSWI");//find a CSWI sibling, and operate on that instead
                if(sibling.length > 0){
                  ref = sibling[0].id;
                }
                schema_svgElementData[ref]['position'] = false;
              }
            }
            else if(value == '2'){
              if(schema_svgElementData[el.id]['position'] != true){
                $("#open",el)[0].beginElement();
                schema_svgElementData[el.id]['position'] = true;

                var ref = el.id;
                var sibling = $(el).siblings(".CSWI");//find a CSWI sibling, and operate on that instead
                if(sibling.length > 0){
                  ref = sibling[0].id;
                }
                schema_svgElementData[ref]['position'] = true;
              }
            }
            else if(value == '0'){
              $("#transition",el)[0].beginElement();
            }
            else{
              $("#error",el)[0].beginElement();
            }
          }
        }
      })
    }
  });

  socket.on('svg_object_add_to_schema', function (data) {
    //add svg to object
    node = svg_add_to_schema(data['x'],data['y'],data['svg'],data['id']);
    if(node == null){
      return;
    }

    schema_in_view.push(data['id']);
    //register values in this svg for reporting
      //register for all values in loaded svg
    $("g",node).find("*").each(function(idx, el){
      var cl = el.classList.toString();
      console.log("node:" + node.id + ", id:" + el.id + ", class:" + cl);
      //elements that can be interacted with by the IEC61850 client
      if(el.id.startsWith("iec60870://") == true){    
        schema_svgElementData[el.id] = {};
        if(cl == "XCBR"){
          //socket.emit('register_datapoint', {id : el.id, class : cl});
          console.log("XCBR");
          $("#close",el)[0].beginElement();
        }
        if(cl == "XSWI"){
          //socket.emit('register_datapoint', {id : el.id, class : cl});
          console.log("XCBR");
          $("#open",el)[0].beginElement();
        }
        if(cl == "MEAS"){
          //socket.emit('register_datapoint', {id : el.id, class : cl});
        }
      }
      else
      {
        //if(cl == "EXT"){
        //  el.onclick = extLink;
        //}
      }
    });
  });

  socket.on('svg_object_remove_from_schema', function (data) {
    //remove svg from object
    var obj = schema_svgRoot.firstChild.querySelector("#"+data);
    if(obj != null){
      //unregister values in this svg
      $("g",node).find("*").each(function(idx, el){
        console.log("node:" + node.id + ", id:" + el.id );
        var cl = el.classList.toString();
        //elements that can be interacted with by the IEC60870 client
        if(el.id.startsWith("iec60870://") == true){    
          schema_svgElementData[el.id] = {};
          if(cl == "XCBR"){
            //socket.emit('unregister_datapoint', {id : el.id, class : cl});
          }
          if(cl == "XSWI"){
            //socket.emit('unregister_datapoint', {id : el.id, class : cl});
          }
          if(cl == "MEAS"){
            //socket.emit('unregister_datapoint', {id : el.id, class : cl});
          }
        }
      });
      //svg_unload(svg)
      obj.remove();

      var index = schema_in_view.indexOf(data);
      if (index > -1) {
        schema_in_view.splice(index, 1);
      }
    }
  });

  socket.on('svg_object_add_to_gis', function (data) {
    //add svg to object
    var node = svg_add_to_gis(data['x'],data['y'],data['x2'],data['y2'],data['svg'],data['id']);
    if(node == null){
      return;
    }
    gis_in_view.push(data['id']);
      //register for all values in loaded svg
    $("g",node).find("*").each(function(idx, el){
      var cl = el.classList.toString();
      //console.log("el.id:" + el.id + " cl:"+cl);
      if(el.id.startsWith("iec60870://") == true){    
        if(cl == "XCBR"){ $("#close",el)[0].beginElementAt(1.0); }
        if(cl == "XSWI"){ $("#open",el)[0].beginElementAt(1.0); }
      }
    });
  });

  socket.on('svg_object_remove_from_gis', function (data) {
    //remove svg from object
    var obj = gis_svgRoot.querySelector("#"+data);
    if(obj != null){
      //unregister values in this svg
      $("g",obj).find("*").each(function(idx, el){
        var cl = el.classList.toString();
        if(el.id.startsWith("iec60870://") == true){    
          //unregister
        }
      });
      obj.remove();
      var index = gis_in_view.indexOf(data);
      if (index > -1) {
        gis_in_view.splice(index, 1);
      }
    }
  });

  socket.on('geojson_object_add_to_gis', function (json) {
    //add geojson to object
    if (json) {
      gis_map.removeLayer(geojsonlayer);
      geojsonlayer = L.geoJSON().addTo(gis_map);
      // Add the data to the layer
      geojsonlayer.addData(json);

      geojsonlayer.setStyle(geoStyle);
		}
  });

  socket.on('geojson_object_update_gis', function () {
    //add geojson to object
    geojsonlayer.setStyle(geoStyle);
  });

});


var update_schema = function(){ 
  pos = this.getPan();
  zoom = this.getZoom();
  socket.emit('get_svg_for_schema', {'x': pos.x, 'y': pos.y, 'z': zoom, 'in_view': schema_in_view});
  //socket.emit('get_svg', {data: ''} );
  console.log(zoom + " - " + pos.x + ", " + pos.y + ", in_view:" + schema_in_view); 
} 

function svg_add_to_schema(x, y, svgString, svgId) {
  var parser = new DOMParser();
  var doc = parser.parseFromString(svgString, "image/svg+xml");
  var svgNode = doc.documentElement;

  schema_svgRoot.firstChild.appendChild(svgNode);//firstchild is svg, as pan/zoom adds a parent
  var newNode = schema_svgRoot.firstChild.lastChild;//firstchild is svg, as pan/zoom adds a parent
  newNode.id = svgId;
  newNode.setAttribute("x", x.toString());
  newNode.setAttribute("y", y.toString());
  return newNode;
}

var update_gis = function(){ 
  pos = gis_map.getCenter();
  zoom = gis_map.getZoom();
  socket.emit('get_svg_for_gis', {'x': pos.lat, 'y': pos.lng, 'z': zoom, 'in_view': gis_in_view});
} 

function svg_add_to_gis(x, y, x2, y2, svgString, svgId) {
  gis_svgRoot[svgId] = new DOMParser().parseFromString(svgString, "image/svg+xml").documentElement;
  gis_svgRoot[svgId].setAttribute('viewBox', "0 0 1000 1000");

  L.svgOverlay(gis_svgRoot[svgId], [ [ y,x], [ y2, x2 ] ]).addTo(gis_map);

  gis_svgRoot[svgId].id = svgId;
  return gis_svgRoot[svgId];
}

var geoStyle = function(feature){
  color = "#ff7800";
  //retrieve color from real-time database
  if(feature.properties.id == "one"){ color = "#ffff00"; }
  return {
    "color": color,
    "weight": 5,
    "opacity": 0.65
  };
}

var socket;
var schema_leafletmap, schema_sidebar, schema_geojsonlayer, schema_in_view, schema_editableLayers; 
var gis_leafletmap, gis_sidebar, gis_geojsonlayer,gis_in_view, gis_editableLayers;
var local_data_cache;

//https://stackoverflow.com/questions/62305306/invert-y-axis-of-lcrs-simple-map-on-vue2-leaflet
var CRSPixel = L.Util.extend(L.CRS.Simple, {
	transformation: new L.Transformation(1,0,1,0)
});

function init_schema(){
  schema_in_view = [];

  document.getElementById("mmi_svg").style.display = "block";
  
  schema_leafletmap = L.map('mmi_svg', { 
    renderer: L.svg(), 
    crs: CRSPixel,
    minZoom: 0,//-5
    maxZoom: 20,
    mapType: "schema"
  }).setView([0, 0], 17);//setView([0,0], 1);

  schema_editableLayers = new L.FeatureGroup();
  schema_leafletmap.addLayer(schema_editableLayers);

  schema_geojsonlayer = L.geoJSON().addTo(schema_leafletmap);

  let schema_options = {
    position: 'topleft',
    draw: {
      polyline: true,
      polygon: {
        allowIntersection: false, // Restricts shapes to simple polygons 
        drawError: {
          color: '#e1e100', // Color the shape will turn when intersects 
          message: '<strong>Error: line intersects!<strong> intersecting polygons are not allowed' // Message that will show when intersect 
        }
      },
      circle: false, // Turns off this drawing tool 
      rectangle: true,
      marker: false,
      circlemarker: false
    },
    edit: {
      featureGroup: schema_editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  
  var schema_drawControl = new L.Control.Draw(schema_options);
  var isEditEnabled = false;
  L.easyButton('fa-globe', function(btn, map){
    if(isEditEnabled == true){
      schema_leafletmap.removeControl(schema_drawControl);
      isEditEnabled = false;
    }else{
      schema_leafletmap.addControl(schema_drawControl);
      isEditEnabled = true;
    }  
  }).addTo( schema_leafletmap );
  //schema_leafletmap.addControl(schema_drawControl);

  schema_sidebar = L.control.sidebar('schema_sidebar', {
    position: 'right',
    autoPan: false,
    closeButton: true,
  });
  schema_leafletmap.addControl(schema_sidebar);
  L.DomEvent.on(schema_sidebar.getCloseButton(), 'click', function () {
    schema_sidebar.hide();
  });


  schema_leafletmap.on(L.Draw.Event.CREATED, schema_addItem);
  schema_leafletmap.on(L.Draw.Event.EDITED, schema_editedItems);
  schema_leafletmap.on(L.Draw.Event.DELETED, schema_removeItems);
  schema_leafletmap.on('moveend', update_schema);
  schema_leafletmap.on('zoomend', update_schema);

  //do not update map when editing, to prevent layer modification from database during editing
  schema_leafletmap.on('draw:editstart', function(){ schema_leafletmap.off('moveend', update_schema);  schema_leafletmap.off('zoomend', update_schema);} );
  schema_leafletmap.on('draw:editstop', function(){schema_leafletmap.on('moveend', update_schema);  schema_leafletmap.on('zoomend', update_schema);} );
  schema_leafletmap.on('draw:deletestart', function(){schema_leafletmap.off('moveend', update_schema);  schema_leafletmap.off('zoomend', update_schema);} );
  schema_leafletmap.on('draw:deletestop', function(){schema_leafletmap.on('moveend', update_schema);  schema_leafletmap.on('zoomend', update_schema);} );
  schema_leafletmap.setZoom(18);//-5
}


function init_gis(){
  gis_in_view = [];

  document.getElementById("gis_map").style.display = "block";

  gis_leafletmap = L.map('gis_map', { 
    renderer: L.svg(),
    mapType: "gis"
  }).setView([51.980, 5.842], 17);
  //gis_map = new L.Map('gis_map').setView([51.980, 5.842], 17);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'openstreetmap',
    maxZoom: 20,
    id: 'openstreetmap',
    tileSize: 512,
    zoomOffset: -1,
  }).addTo(gis_leafletmap);//*/

  gis_geojsonlayer = L.geoJSON().addTo(gis_leafletmap);

  
  //https://codepen.io/mochaNate/pen/bWNveg
  gis_editableLayers = new L.FeatureGroup();
  gis_leafletmap.addLayer(gis_editableLayers);

  let gis_options = {
    position: 'topright',
    draw: {
      polyline: true,
      polygon: {
        allowIntersection: false, // Restricts shapes to simple polygons 
        drawError: {
          color: '#e1e100', // Color the shape will turn when intersects 
          message: '<strong>Oh snap!<strong> you can\'t draw that!' // Message that will show when intersect 
        }
      },
      circle: false, // Turns off this drawing tool 
      rectangle: true,
      marker: false,
      circlemarker: false
    },
    edit: {
      featureGroup: gis_editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  let gis_drawControl = new L.Control.Draw(gis_options);
  gis_leafletmap.addControl(gis_drawControl);


  gis_sidebar = L.control.sidebar('gis_sidebar', {
    position: 'right',
    autoPan: false,
    closeButton: true,
  });
  gis_leafletmap.addControl(gis_sidebar);
  L.DomEvent.on(gis_sidebar.getCloseButton(), 'click', function () {
    gis_sidebar.hide();
  });


  //register svg events
  gis_leafletmap.on(L.Draw.Event.CREATED, gis_addItem);//*/
  gis_leafletmap.on(L.Draw.Event.EDITED, gis_editedItems);
  gis_leafletmap.on(L.Draw.Event.DELETED, gis_removeItems);
  gis_leafletmap.on('moveend', update_gis);
  gis_leafletmap.on('zoomend', update_gis);

  //ensure layers are not updated from database during editing or removing
  gis_leafletmap.on('draw:editstart', function(){ gis_leafletmap.off('moveend', update_schema);  gis_leafletmap.off('zoomend', update_schema);} );
  gis_leafletmap.on('draw:editstop', function(){gis_leafletmap.on('moveend', update_schema);  gis_leafletmap.on('zoomend', update_schema);} );
  gis_leafletmap.on('draw:deletestart', function(){gis_leafletmap.off('moveend', update_schema);  gis_leafletmap.off('zoomend', update_schema);} );
  gis_leafletmap.on('draw:deletestop', function(){gis_leafletmap.on('moveend', update_schema);  gis_leafletmap.on('zoomend', update_schema);} );
  gis_leafletmap.setZoom(18);
}


function schema_addItem(e) {
  let type = e.layerType, layer = e.layer;

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }

  if (type === 'svg') {
    layer.type = "Svg";
    layer.on("click", schema_show_Sidebar);
    
    if(layer._newTemplate == true){
      socket.emit('svg_addTemplate', {
        'name':layer._templateName,
        'viewBox': layer._svgViewBox,
        'svg': layer._url.innerHTML,
        'datapoint_amount':layer._dataPoints.length
      });
    }

    let bounds = layer.getBounds();
    socket.emit('schema_addItems', {
      'w':bounds._northEast.lng,
      'n':bounds._northEast.lat,
      'e':bounds._southWest.lng,
      's':bounds._southWest.lat,
      'svg':layer._templateName, 
      'dataPoints': layer._dataPoints }, 
      function(ret){
        if (!layer.uuid){
          layer.uuid = ret;
        }
      }
    );
  }
  else if (layer.toGeoJSON){ //geojson item
    layer.type = "Feature";
    layer._dataPoints = {};
    layer.on("click", schema_show_Sidebar);

    layer.feature = {"properties":{}};
    setGeojsonStyle(layer, layer.feature);
    let geojson = layer.toGeoJSON();
    geojson["properties"]['datapoints'] = layer._dataPoints;
    geojson['type'] = layer.type;
    socket.emit('schema_addGeojsonItem', geojson ,
    function(ret){
      if (!layer.uuid){
        layer.uuid = ret;
      }
    });
  }
  schema_editableLayers.addLayer(layer);
}


function gis_addItem(e) {
  let type = e.layerType, layer = e.layer;

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }
  if (type === 'svg') {
    layer.type = "Svg";
    layer.on("click", gis_show_Sidebar);

    if(layer._newTemplate == true){
      socket.emit('svg_addTemplate', {
        'name':layer._templateName,
        'viewBox': layer._svgViewBox,
        'svg': layer._url.innerHTML,
        'datapoint_amount':layer._dataPoints.length
      });
    }
    let latlng = layer.getLatLng();
    let bounds = layer.getBounds();
    socket.emit('gis_addItem', {
      'type': "Svg",
      "location": { "type": "Point", 
                    "coordinates": [ latlng.lng, latlng.lat ], //coords are switched position from leaflet in geojson
                    "height": bounds._northEast.lat - bounds._southWest.lat, 
                    "width": bounds._northEast.lng - bounds._southWest.lng
                  },
      "properties": {
                    'svg':layer._templateName, 
                    'datapoints': layer._dataPoints
                  }
      },
      function(ret){
        if (!layer.uuid){
          layer.uuid = ret;
        }
      }
    );
  }
  else if (layer.toGeoJSON){ //geojson item
    layer.type = "Feature";
    layer.on("click", gis_show_Sidebar);
    layer._dataPoints = {};

    layer.feature = {"properties":{}};
    setGeojsonStyle(layer, layer.feature);
    let geojson = layer.toGeoJSON();

    geojson["properties"]['datapoints'] = layer._dataPoints;
    geojson['type'] = layer.type;
    socket.emit('gis_addItem', geojson ,
    function(ret){
      if (!layer.uuid){
        layer.uuid = ret;
      }
    });
  }
  gis_editableLayers.addLayer(layer);
}


function schema_editedItems(e){
  for (const [key, layer] of Object.entries(e.layers._layers)) {
    if(layer.type && layer.type === "Feature"){
      let geojson = layer.toGeoJSON();
      geojson["properties"]['datapoints'] = layer._dataPoints;
      //setGeojsonStyle(layer, geojson);

      socket.emit('schema_editedGeojsonItems', {
        '_id':layer.uuid,
        'type': layer.type,
        'geometry':geojson['geometry'],
        'properties':geojson['properties'],
      });
    }
    else if(layer.type && layer.type === "Svg"){
      let bounds = layer.getBounds();
      socket.emit('schema_editedItems', {
        '_id':layer.uuid,
        'w':bounds._northEast.lng,
        'n':bounds._northEast.lat,
        'e':bounds._southWest.lng,
        's':bounds._southWest.lat,
        'dataPoints': layer._dataPoints
      });
    }
  }
}



function gis_editedItems(e){
  for (const [key, layer] of Object.entries(e.layers._layers)) {
    if(layer.type && layer.type === "Feature"){
      let geojson = layer.toGeoJSON();
      geojson["properties"]['datapoints'] = layer._dataPoints;
      //setGeojsonStyle(layer, geojson);

      socket.emit('gis_editedItems', {
        '_id':layer.uuid,
        'type': layer.type,
        'geometry':geojson['geometry'],
        'properties':geojson['properties'],
      });
    }
    else if(layer.type && layer.type === "Svg"){
      let latlng = layer.getLatLng();
      let bounds = layer.getBounds();
      socket.emit('gis_editedItems', {
        '_id':layer.uuid,
        'type': layer.type,
        "location": { "type": "Point", 
                      "coordinates": [ latlng.lng, latlng.lat ], //coords are switched position from leaflet in geojson
                      "height": bounds._northEast.lat - bounds._southWest.lat, 
                      "width": bounds._northEast.lng - bounds._southWest.lng, 
                    },
        "properties": {
          'datapoints': layer._dataPoints
        } 
      });
    }
  }
}



function schema_removeItems(e){
  for (const [key, layer] of Object.entries(e.layers._layers)) {
    if(layer.type && layer.type === "Feature"){
      socket.emit('schema_removeGeojsonItems', layer.uuid);
    }
    else if(layer.type && layer.type === "Svg"){
      socket.emit('schema_removeItems', layer.uuid);
    }
  }
}


function gis_removeItems(e){
  for (const [key, layer] of Object.entries(e.layers._layers)) {
    socket.emit('gis_removeItems', layer.uuid);
  }
}


$(document).ready(function() {
  namespace = '';
  socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
  local_data_cache = {};
  init_gis();
  init_schema();
  if(document.getElementById("focus").value === "1"){
    document.getElementById("mmi_svg").style.display = "none";
    document.getElementById("gis_map").style.display = "block";
  }
  else{
    document.getElementById("mmi_svg").style.display = "block";
    document.getElementById("gis_map").style.display = "none";
  }


  //////////////////////////////////////////////////////////////////////////


  socket.on('updateDataPoint', function (data) { 
    //console.log("called:" + data.toString());
    let key = data['key'];
    let value = data['value'];
    //console.log("key:" + key.toString() + " value:" + value.toString());
    // update svg items and geojson in schema
    updateLayers(schema_editableLayers._layers, key, value);
    // update svg items and geojson in gis
    updateLayers(gis_editableLayers._layers, key, value);
  });

  var updateLayers = function(layers,key, value){
    if(local_data_cache[key] == value){
      return;
    }
    local_data_cache[key] = value;
    for(let layer_id in layers){
      let layer = layers[layer_id]
      for (const [d_key, point] of Object.entries(layer._dataPoints)) {

        if (!(key in point)){
          continue;
        }
        template_item = point[key];
        //update
        if(layer.type === "Svg"){
          //template_item is id of svg element. class is used for type of display
          $("g",layer._image).find("*").each(function(idx, el){
            let cl = el.classList.toString();
            if(el.id == template_item){ 
              //register  
              if(cl == "XCBR" || cl == "XSWI"){ 
                if(value == 1) {
                  $("#close",el)[0].beginElementAt(0.1); 
                }
                else {
                  $("#open",el)[0].beginElementAt(0.1);
                }
              }
              if(cl == "MEAS"){ 
                if(el.dataset.size > 0 || typeof(el.dataset.text) === "undefined"){
                  var desc = el.innerHTML;
                  el.textContent = value;
                }
                else{
                  var val = abbreviate_number(parseFloat(value),0)
                  el.textContent = el.dataset.text.replace("{value}",val);
                }
              }
            }
          });
        }
        if(layer.type === "Feature"){
          //template_item is property modification of geojson element. class is used for type of display
          //template_item = {"1":["color","gt","10","#00ff00"]};
          let result = null;
          if(template_item[1] == ">" && value > template_item[2]){ // greater then
            result = template_item[3];
          }
          if(template_item[1] == "<" && value < template_item[2]){ // less then
            result = template_item[3];
          }
          if(template_item[1] == "==" && value == template_item[2]){ // equal
            result = template_item[3];
          }
          if(template_item[1] == "!=" && value != template_item[2] ){ // not equal
            result = template_item[3];
          }
          if(template_item[1] == "><" && value > template_item[2] && value < template_item[3]){ // within range (invert order for outside range)
            result = template_item[4];
          }
          if(result !== null){
            layer.options[template_item[0]] = result;
            layer.setStyle();//update the layer style
          }        
        }
      }
    }
  }

  //////////////////////////////////////////////////////////////////////////


  socket.on('svg_object_add_to_schema', function (data) {
    //add svg to object
    if(schema_in_view.includes(data['id'])){
      return;
    }
    node = svg_add_to_schema(data['w'],data['n'],data['e'],data['s'],data['svg'],data['id']);
    if(node == null){
      return;
    }
    node._dataPoints = data['datapoints'];
    node.on("click", schema_show_Sidebar);
    for (const [key, point] of Object.entries(node._dataPoints)) {
      for (const [child_key, child_point] of Object.entries(point)) {
        socket.emit('register_datapoint', child_key);
      }
    }

    schema_in_view.push(data['id']);
  });

  socket.on('svg_object_remove_from_schema', function (data) {
    //remove svg from object
    let obj = null
    for(let item in schema_editableLayers._layers){
      if(schema_editableLayers._layers[item].uuid === data){
          obj = schema_editableLayers._layers[item];
          break; 
      }
    }
    if(obj != null){
      //unregister values in this svg
      for (const [key, point] of Object.entries(obj._dataPoints)) {
        for (const [child_key, child_point] of Object.entries(point)) {
          socket.emit('unregister_datapoint', child_key);
        }
      }
      schema_editableLayers.removeLayer(obj);
      let index = schema_in_view.indexOf(data);
      if (index > -1) {
        schema_in_view.splice(index, 1);
      }
    }

  });

  socket.on('geojson_object_add_to_schema', function (json) {
    //add geojson to object
    if (json) {
      let local_geojsonlayer = L.geoJSON();

      // parse the json into leaflet layers
      local_geojsonlayer.addData(json);
      //find what layer allready exist
      for(let local_geoitem in local_geojsonlayer._layers){
        let found = false;
        for(let edititem in schema_editableLayers._layers){
          if(schema_editableLayers._layers[edititem].feature && 
            schema_editableLayers._layers[edititem].feature._id === local_geojsonlayer._layers[local_geoitem].feature._id){
            found = true;
            break;
          }
        }
        if(found == false){// if geojson is not found,
          // add geojson objects to edit and geojson-layer
          local_geojsonlayer._layers[local_geoitem].uuid = local_geojsonlayer._layers[local_geoitem]['feature']['_id'];
          local_geojsonlayer._layers[local_geoitem].type = "Feature";
          local_geojsonlayer._layers[local_geoitem].on("click", schema_show_Sidebar);
          local_geojsonlayer._layers[local_geoitem]._dataPoints = local_geojsonlayer._layers[local_geoitem]['feature']["properties"]['datapoints'];
          for (const [key, point] of Object.entries(local_geojsonlayer._layers[local_geoitem]._dataPoints)) {
            for (const [child_key, child_point] of Object.entries(point)) {
              socket.emit('register_datapoint', child_key);
            }
          }
          getGeojsonStyle(local_geojsonlayer._layers[local_geoitem]);
          //for (const [key, point] of Object.entries(local_geojsonlayer._layers[local_geoitem]._dataPoints)) {
          //  socket.emit('register_datapoint', point);
          //}

          schema_editableLayers.addLayer(local_geojsonlayer._layers[local_geoitem]);
          schema_geojsonlayer.addLayer(local_geojsonlayer._layers[local_geoitem]);
        }
      }
		}
  });

  socket.on('svg_object_add_to_gis', function (data) {
    //add svg to object
    if(gis_in_view.includes(data['id'])){
      return;
    }
    let node = svg_add_to_gis(data['svg'],data['id'],data['location']);
    if(node == null){
      return;
    }
    node.on("click", gis_show_Sidebar);
    node._dataPoints = data["properties"]['datapoints'];
    for (const [key, point] of Object.entries(node._dataPoints)) {
      for (const [child_key, child_point] of Object.entries(point)) {
        socket.emit('register_datapoint', child_key);
      }
    }
    
    gis_in_view.push(data['id']);
  });

  socket.on('svg_object_remove_from_gis', function (data) {
    //remove svg from object
    let obj = null
    for(let item in gis_editableLayers._layers){
      if(gis_editableLayers._layers[item].uuid === data){
          obj = gis_editableLayers._layers[item];
          break; // If you want to break out of the loop once you've found a match
      }
    }
    if(obj != null){
      for (const [key, point] of Object.entries(obj._dataPoints)) {
        for (const [child_key, child_point] of Object.entries(point)) {
          socket.emit('unregister_datapoint', child_key);
        }
      }

      gis_editableLayers.removeLayer(obj);
      let index = gis_in_view.indexOf(data);
      if (index > -1) {
        gis_in_view.splice(index, 1);
      }
    }
  });

  socket.on('geojson_object_add_to_gis', function (json) {
    //add geojson to object
    if (json) {
      let local_geojsonlayer = L.geoJSON();

      // parse the json into leaflet layers
      local_geojsonlayer.addData(json);
      //find what layer allready exist
      for(let local_geoitem in local_geojsonlayer._layers){
        let found = false;
        for(let edititem in gis_editableLayers._layers){
          if(gis_editableLayers._layers[edititem].feature && 
              gis_editableLayers._layers[edititem].feature._id === local_geojsonlayer._layers[local_geoitem].feature._id){
            found = true;
            break;
          }
        }
        if(found == false){// if geojson is not found,
          // add geojson objects to edit and geojson-layer
          local_geojsonlayer._layers[local_geoitem].uuid = local_geojsonlayer._layers[local_geoitem]['feature']['_id'];
          local_geojsonlayer._layers[local_geoitem].type = "Feature";
          local_geojsonlayer._layers[local_geoitem].on("click", gis_show_Sidebar);
          local_geojsonlayer._layers[local_geoitem]._dataPoints = local_geojsonlayer._layers[local_geoitem]['feature']["properties"]['datapoints'];
          for (const [key, point] of Object.entries(local_geojsonlayer._layers[local_geoitem]._dataPoints)) {
            for (const [child_key, child_point] of Object.entries(point)) {
              socket.emit('register_datapoint', child_key);
            }
          }
          getGeojsonStyle(local_geojsonlayer._layers[local_geoitem]);
          //for (const [key, point] of Object.entries(local_geojsonlayer._layers[local_geoitem]._dataPoints)) {
          //  socket.emit('register_datapoint', point);
          //}

          gis_editableLayers.addLayer(local_geojsonlayer._layers[local_geoitem]);
          gis_geojsonlayer.addLayer(local_geojsonlayer._layers[local_geoitem]);
        }
      }
		}
  });


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


});

var update_schema = function(){ 
  zoom = schema_leafletmap.getZoom();
  bounds = schema_leafletmap.getBounds();
  socket.emit('get_svg_for_schema', {'w': bounds.getWest(), 'n': bounds.getSouth(), 'z': zoom, 'in_view': schema_in_view, 'e': bounds.getEast(), 's': bounds.getNorth()});
} 

var update_gis = function(){ 
  zoom = gis_leafletmap.getZoom();
  bounds = gis_leafletmap.getBounds();
  socket.emit('get_svg_for_gis', {'w': bounds.getWest(), 'n': bounds.getNorth(), 'e': bounds.getEast(), 's': bounds.getSouth(), 'z': zoom, 'in_view': gis_in_view});
} 


function svg_add_to_schema(w, n, e, s, svgString, svgId) {
  let svg = new L.SvgObject(svgString, L.latLngBounds([[n,w],[s,e]]), svgId,{ svgViewBox:{ viewBox: "calculate", fitBounds: false, scaleBounds:  0.000005/*1.0*/ }});
  svg.type = "Svg";
  schema_editableLayers.addLayer(svg);
  return svg;
}

function svg_add_to_gis(svgString, svgId, location) {
  // correct leaflet size+latlng based on gis coordinate system (by ajusting bounds)
  let hheight = location['height']/2;
  let hwidth = location['width']/2;
  let longtitude = location['coordinates'][0];
  let latitude = location['coordinates'][1];

  // set svg viewbox with x,y,x2,y2 (i.e. 0,0,512,512). as a side-effect, the leaflet bounds on map are also set to this by default
  let svg = new L.SvgObject(
    svgString, 
    L.latLngBounds([ [ latitude-hheight,longtitude-hwidth], [ latitude+hheight,longtitude+hwidth ] ]), 
    svgId,  
    { svgViewBox:{ viewBox: "calculate", fitBounds: false, scaleBounds: 0.000005 }}
  );
  svg.type = "Svg";
  // add to gis layer
  gis_editableLayers.addLayer(svg);
  return svg;
}

/////////////////////////////////////////////////////////////////////////////


function setGeojsonStyle(layer, geojson){
  //console.log(e);
  geojson.properties['fillEnabled'] = layer.options.fill;//true/false
  geojson.properties['fill'] = layer.options.fillColor;
  geojson.properties['fill-opacity'] = layer.options.fillOpacity;
  geojson.properties["fillRule"] = layer.options.fillRule;

  geojson.properties['strokeEnabled' ] = layer.options.stroke;//true/false
  geojson.properties['stroke'] = layer.options.color;
  geojson.properties['stroke-width'] = layer.options.weight;
  geojson.properties['stroke-opacity'] = layer.options.opacity;
  
  geojson.properties['stroke-cap'] = layer.options.lineCap;// "round",
  geojson.properties['stroke-join'] = layer.options.lineJoin;// "round",
  geojson.properties['stroke-dashArray'] = layer.options.dashArray;// null,
  geojson.properties['stroke-dashOffset'] = layer.options.dashOffset;// null,

  geojson.properties['smoothFactor'] = layer.options.smoothFactor;//": 1,
  geojson.properties['noClip'] = layer.options.noClip;// false,
  geojson = JSON.stringify(geojson);//make sure it is all valid geojson
}

function getGeojsonStyle(layer){
  //console.log(e);
  layer.options.fill = layer.feature.properties['fillEnabled'];//true/false
  layer.options.fillColor = layer.feature.properties['fill']; 
  layer.options.fillOpacity = layer.feature.properties['fill-opacity'];//"fillOpacity": 0.1,
  layer.options.fillRule = layer.feature.properties["fillRule"]; //"evenodd",

  layer.options.stroke = layer.feature.properties['strokeEnabled' ];//true/false
  layer.options.color = layer.feature.properties['stroke']; 
  layer.options.weight = layer.feature.properties['stroke-width'];//  "weight": 3,
  layer.options.opacity = layer.feature.properties['stroke-opacity']; //  "opacity": 0.5,

  layer.options.lineCap = layer.feature.properties['stroke-cap'];// "round",
  layer.options.lineJoin = layer.feature.properties['stroke-join'];// "round",
  layer.options.dashArray = layer.feature.properties['stroke-dashArray'];// null,
  layer.options.dashOffset = layer.feature.properties['stroke-dashOffset'];// null,

  layer.options.smoothFactor = layer.feature.properties['smoothFactor'];//": 1,
  layer.options.noClip = layer.feature.properties['noClip'];// false,

  layer.setStyle();
}


//////////////////////////////////////////////////////////////////////////
	//.leaflet-modal
L.Draw.Svg.include({
	  enable: function(){
      let drawsvg = this;
      socket.emit('svg_getTemplates',{},function(result){
        templates = result;

        let options = "";
        for(let i = 0; i < templates.length; i++){
          options += '<option value="'+i.toString()+'"> '+ templates[i]['name'] +' </option>';
        }
        
        drawsvg._map.fire('modal', {
          title: 'Select SVG template',

          content: [
            '<table cellpadding="1" cellspacing="1">',
            '  <tr>',
            '    <td width="50%">',
            '      <select name="SVG-templates" style="width:150px;">',
                    options,
            '      </select>',
            '    </td>',
            '    <td>',
            '      <svg id="preview" width="250" height="250" xmlns=\'http://www.w3.org/2000/svg\'></svg>',
            '    </td>',
            '  </tr>',
            '</table>',
            '<br><br>'].join(''),

          template: ['<div class="modal-header"><h2>{title}</h2></div>',
            '<hr>',
            '<div class="modal-body">{content}</div>',
            '<div class="modal-footer">',
            '<label for="file-input">Import:</label><input type="file" id="file-input" /><br>',
            '<label for="template_name">Template name:</label><input type="text" id="template_name" /><br>',
            '<button class="topcoat-button--large {OK_CLS}">{okText}</button>',
            '<button class="topcoat-button--large {CANCEL_CLS}">{cancelText}</button>',
            '</div>'
          ].join(''),
        
          okText: 'Ok',
          cancelText: 'Cancel',
          OK_CLS: 'modal-ok',
          CANCEL_CLS: 'modal-cancel',
        
          width: 700,
        
          onShow: function(evt) {
            let modal = evt.modal;
            let imported = null;

            fitSvg(templates[0]['svg'], modal._container.querySelector('#preview'));

            L.DomEvent
            .on(modal._container.querySelector('.modal-ok'), 'click', function() {
              let sel = modal._container.querySelector('select[name="SVG-templates"]');

              if(imported == null){
                let bbox = fitSvg(templates[sel.value]['svg'], modal._container.querySelector('#preview'));//to retrieve the bounds, and write to current_bbox
                drawsvg._svgViewBox = (bbox.x).toString() + " " + (bbox.y).toString() + " " + (bbox.width).toString() + " " + (bbox.height).toString();
                drawsvg._svgFitBounds = true;
                drawsvg._newTemplate = false;
                if(drawsvg._map.options.mapType === "schema"){
                  drawsvg._scale =  0.000005;//1.0;
                }
                if(drawsvg._map.options.mapType === "gis"){
                  drawsvg._scale = 0.000005;
                }
                drawsvg._templateName = templates[sel.value]['name'];
                drawsvg._template = templates[sel.value]['svg'];
              } else {
                let bbox = fitSvg(imported, modal._container.querySelector('#preview'));//to retrieve the bounds, and write to current_bbox
                drawsvg._svgViewBox = (bbox.x).toString() + " " + (bbox.y).toString() + " " + (bbox.width).toString() + " " + (bbox.height).toString();
                drawsvg._svgFitBounds = true;
                drawsvg._newTemplate = true;
                drawsvg._templateName =  modal._container.querySelector('#template_name').value;
                if(drawsvg._map.options.mapType === "schema"){
                  drawsvg._scale =  0.000005;//1.0;
                }
                if(drawsvg._map.options.mapType === "gis"){
                  drawsvg._scale = 0.000005;
                }
                drawsvg._template = imported;
              }

              L.Draw.SimpleShape.prototype.enable.call(drawsvg);
              modal.hide();
            })
            .on(modal._container.querySelector('.modal-cancel'), 'click', function() {
              modal.hide();
            })
            .on(modal._container.querySelector('select[name="SVG-templates"]'), 'change', function() {
              imported = null;
              fitSvg(templates[parseInt(this.value)]['svg'],  modal._container.querySelector('#preview'));
              modal._container.querySelector('#template_name').value = "";
            })
            .on(modal._container.querySelector('#file-input'), 'change', function(e) {
              let file = e.target.files[0];
              if (!file) {
                return;
              }
              let reader = new FileReader();
              reader.onload = function(e) {
                let contents = e.target.result;
                fitSvg(contents,  modal._container.querySelector('#preview'));
                imported = contents;
              };
              reader.readAsText(file);
            });
          }
        });
      });
	}
});

function fitSvg(contents, preview){
  let element = new DOMParser().parseFromString("<svg xmlns=\"http://www.w3.org/2000/svg\">" + contents + "</svg>", "image/svg+xml").documentElement;
  preview.innerHTML = "";
  preview.appendChild(element);
  // get bounding box of svg
  let bbox = preview.getBBox();
  // set viewbox to fit bounding box
  preview.firstChild.setAttribute('viewBox',
    (bbox.x - 4).toString() + " " + (bbox.y - 4).toString() + " " + (bbox.width + 8).toString() + " " + (bbox.height + 8).toString());
  // set parent viewbox to x=0,y=0 and width/heigth to match child
  preview.setAttribute('viewBox',
    (0).toString() + " " + (0).toString() + " " + (bbox.width + 8).toString() + " " + (bbox.height + 8).toString());
  //set black background
  preview.innerHTML = "<rect x=\'"+ (0).toString() +"\' y=\'"+ (0).toString() +"\' width=\'"+(bbox.width + 8).toString()+"\' height=\'"+(bbox.height + 8).toString()+"\'/>" + preview.innerHTML;
  return bbox;
}



function schema_show_Sidebar(e){
  let layer = e.target;
  schema_sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.options, null, 2);
  schema_sidebar._container.querySelector('#datapoints_field').value = JSON.stringify(layer._dataPoints, null, 2);
  schema_sidebar.show();
  let schema_save_fnc_wrap = function(){schema_save_fnc(layer);};

  let save_btn = schema_sidebar._container.querySelector('#sidebar-save');
  let new_save_btn = save_btn.cloneNode(true);
  save_btn.parentNode.replaceChild(new_save_btn, save_btn);

  L.DomEvent.on(new_save_btn, 'click', schema_save_fnc_wrap);
}

var schema_save_fnc = function(layer){ 
  layer._dataPoints = JSON.parse(schema_sidebar._container.querySelector('#datapoints_field').value);
  if(layer.type==="Feature"){
    layer.options = JSON.parse(schema_sidebar._container.querySelector('#options_field').value);
    layer.setStyle();
    setGeojsonStyle(layer, layer.feature);
  }
  schema_editedItems({"layers":{"_layers":{"0":layer}}});

  schema_sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.options, null, 2);
  schema_sidebar._container.querySelector('#datapoints_field').value = JSON.stringify(layer._dataPoints, null, 2);
};

function gis_show_Sidebar(e){
  let layer = e.target;
  gis_sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.options, null, 2);
  gis_sidebar._container.querySelector('#datapoints_field').value = JSON.stringify(layer._dataPoints, null, 2);
  gis_sidebar.show();
  let gis_save_fnc_wrap = function(){gis_save_fnc(layer);};

  let save_btn = gis_sidebar._container.querySelector('#sidebar-save');
  let new_save_btn = save_btn.cloneNode(true);
  save_btn.parentNode.replaceChild(new_save_btn, save_btn);

  L.DomEvent.on(new_save_btn, 'click', gis_save_fnc_wrap);
}

var gis_save_fnc = function(layer){ 
  layer._dataPoints = JSON.parse(gis_sidebar._container.querySelector('#datapoints_field').value);
  if(layer.type==="Feature"){
    layer.options = JSON.parse(gis_sidebar._container.querySelector('#options_field').value);
    layer.setStyle();
    setGeojsonStyle(layer, layer.feature);
  }
  gis_editedItems({"layers":{"_layers":{"0":layer}}});

  gis_sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.options, null, 2);
  gis_sidebar._container.querySelector('#datapoints_field').value = JSON.stringify(layer._dataPoints, null, 2);
};

function abbreviate_number(num, fixed) {
  if (num === null) { return null; } // terminate early
  if (num === 0) { return '0'; } // terminate early
  fixed = (!fixed || fixed < 0) ? 0 : fixed; // number of decimal places to show
  var b = (num).toPrecision(2).split("e"), // get power
      k = b.length === 1 ? 0 : Math.floor(Math.min(b[1].slice(1), 14) / 3), // floor at decimals, ceiling at trillions
      c = k < 1 ? num.toFixed(0 + fixed) : (num / Math.pow(10, k * 3) ).toFixed(1 + fixed), // divide by power
      d = c < 0 ? c : Math.abs(c), // enforce -0 is 0
      e = d + ['', 'K', 'M', 'B', 'T'][k]; // append power
  return e;
}
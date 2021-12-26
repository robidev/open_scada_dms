var socket, schema_leafletmap, schema_svgRoot, schema_in_view, svglayer, gis_svgRoot, gis_in_view, gis_map, geojsonlayer, editableLayers;

function init_gis(){
  geojsonlayer = {};
  gis_svgRoot = {};
  gis_in_view = [];
  var gis_div = document.getElementById("gis_map");
  gis_div.style.display = "block";

  gis_map = L.map('gis_map', { renderer: L.svg()}).setView([51.980, 5.842], 17);
  //gis_map = new L.Map('gis_map').setView([51.980, 5.842], 17);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'openstreetmap',
    maxZoom: 20,
    id: 'openstreetmap',
    tileSize: 512,
    zoomOffset: -1,
  }).addTo(gis_map);//*/


  //https://codepen.io/mochaNate/pen/bWNveg
  editableLayers = new L.FeatureGroup();
  gis_map.addLayer(editableLayers);

  var options = {
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
      circle: true, // Turns off this drawing tool 
      rectangle: true,
      marker: true
    },
    edit: {
      featureGroup: editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  
  var drawControl = new L.Control.Draw(options);
  gis_map.addControl(drawControl);


  
  geojsonlayer = L.geoJSON().addTo(gis_map);
  //register svg events
  gis_map.on(L.Draw.Event.CREATED, addItem);//*/
  gis_map.on('moveend', update_gis);
  gis_map.on('zoomend', update_gis);
  gis_map.setZoom(18);
}

function exportGeoJSON(featureGroup) {
  // Extract GeoJson from featureGroup
  var data = featureGroup.toGeoJSON();
  // Stringify the GeoJson
  var convertedData = 'text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(data));
  // Create export
  let linkElement = document.createElement('a');
  linkElement.setAttribute('href', 'data:' + convertedData);
  linkElement.setAttribute('download','data.geojson');
  linkElement.click();
}

//https://stackoverflow.com/questions/62305306/invert-y-axis-of-lcrs-simple-map-on-vue2-leaflet
var CRSPixel = L.Util.extend(L.CRS.Simple, {
	transformation: new L.Transformation(1,0,1,0)
});

function init_schema(){
  svglayer = {};
  schema_svgRoot = {};
  schema_in_view = [];
  document.getElementById("mmi_svg").style.display = "block";
  
  schema_leafletmap = L.map('mmi_svg', { 
    renderer: L.svg(), 
    crs: CRSPixel,
    minZoom: -5,
    maxZoom: 10
  }).setView([0,0], 1);

  editableLayers = new L.FeatureGroup();
  schema_leafletmap.addLayer(editableLayers);

  var options = {
    position: 'topright',
    draw: {
      polyline: true,
      polygon: {
        allowIntersection: false, // Restricts shapes to simple polygons 
        drawError: {
          color: '#e1e100', // Color the shape will turn when intersects 
          message: '<strong>Error: line intersects!<strong> intersecting polygons are not allowed' // Message that will show when intersect 
        }
      },
      circle: true, // Turns off this drawing tool 
      rectangle: true,
      marker: true
    },
    edit: {
      featureGroup: editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  
  var drawControl = new L.Control.Draw(options);
  schema_leafletmap.addControl(drawControl);

  geojsonlayer = L.geoJSON().addTo(schema_leafletmap);

  schema_leafletmap.on(L.Draw.Event.CREATED, addItem);
  schema_leafletmap.on(L.Draw.Event.EDITED, function(e){
    console.log(e);
  });
  schema_leafletmap.on(L.Draw.Event.DRAWSTART, function(e){
    console.log(e);
  });
  schema_leafletmap.on(L.Draw.Event.EDITMOVE, function(e){
    console.log(e);
  });
  schema_leafletmap.on('moveend', update_schema);
  schema_leafletmap.on('zoomend', update_schema);
  schema_leafletmap.setZoom(0);
  //schema_leafletmap.fitBounds(bounds);
}

function addItem(e) {
  //gis_map.on(L.Draw.Event.CREATED, function(e) {
  var type = e.layerType, layer = e.layer;

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }
  //svg_add_to_schema(0,0,100,100,"<>","aaa");
  editableLayers.addLayer(layer);
}

function deinit_schema(){

  schema_leafletmap.off('draw:created',addItem)
  schema_leafletmap.off('moveend', update_schema);
  schema_leafletmap.off('zoomend', update_schema);

  var schema_map = document.getElementById("mmi_svg");
  schema_map.style.display = "none";
  schema_leafletmap.remove();
  schema_svgRoot.innerHTML = "";
  schema_map.innerHTML = "";

  delete svglayer;
  delete schema_leafletmap;
  delete schema_svgRoot;
  delete schema_in_view;

  svglayer = null;
  schema_leafletmap = null;
  schema_svgRoot = null;
  schema_in_view = null;
}

function deinit_gis(){
  gis_map.off('draw:created', addItem);//*/
  gis_map.off('moveend', update_gis);
  gis_map.off('zoomend', update_gis);

  var gis_div = document.getElementById("gis_map");
  gis_div.style.display = "none";
  gis_map.remove();
  gis_svgRoot.innerHTML = "";
  gis_div.innerHTML = "";

  delete gis_svgRoot;
  delete gis_in_view;
  delete gis_map;
  delete geojsonlayer;

  gis_svgRoot = null;
  gis_in_view = null;
  gis_map = null;
  geojsonlayer = null;
}

function toggle_view() {
  var gis = document.getElementById("gis_map");
  var schema_div = document.getElementById("mmi_svg");
  if (gis.style.display === "none") {
    document.getElementById("mmi_svg").style.display = "none";
    document.getElementById("gis_map").style.display = "block";
    //deinit_schema();
    //init_gis();
  } else {
    document.getElementById("mmi_svg").style.display = "block";
    document.getElementById("gis_map").style.display = "none";
    //deinit_gis();
    //init_schema();
  }
} 

$(document).ready(function() {
  namespace = '';


  socket = io.connect('http://' + document.domain + ':' + location.port + namespace);


  init_gis();
  init_schema();
  document.getElementById("mmi_svg").style.display = "block";
  document.getElementById("gis_map").style.display = "none";

  //add info to the ied/datamodel tab
  socket.on('svg_value_update_event_on_schema', function (data) {
    //event gets called from server when svg data is updated, so update the svg
    var element = data['element'];
    var value = data['data']['value'];
    var type = data['data']['type'];
  });

  socket.on('svg_object_add_to_schema', function (data) {
    //add svg to object
    node = svg_add_to_schema(data['x'],data['y'],data['x2'],data['y2'],data['svg'],data['id']);
    if(node == null){
      return;
    }

    schema_in_view.push(data['id']);

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

  socket.on('svg_object_remove_from_schema', function (data) {
    //remove svg from object
    var obj = schema_svgRoot[data];
    if(obj != null){
      //unregister values in this svg
      $("g",obj).find("*").each(function(idx, el){
        var cl = el.classList.toString();
        if(el.id.startsWith("iec60870://") == true){    
          //unregister
        }
      });
      obj.remove();
      var index = schema_in_view.indexOf(data);
      if (index > -1) {
        schema_in_view.splice(index, 1);
      }
    }

  });

  socket.on('svg_object_add_to_gis', function (data) {
    //add svg to object
    var node = svg_add_to_gis(data['x'],data['y'],data['x2'],data['y2'],data['svg'],data['id'],data['location']);
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
    var obj = gis_svgRoot[data];
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
  //pos = schema_leafletmap.getCenter();
  zoom = schema_leafletmap.getZoom();
  bounds = schema_leafletmap.getBounds();
  socket.emit('get_svg_for_schema', {'x': bounds.getWest(), 'y': bounds.getSouth(), 'z': zoom, 'in_view': schema_in_view, 'x2': bounds.getEast(), 'y2': bounds.getNorth()});
  //console.log('w:' + bounds.getWest() + ' n:' + bounds.getNorth() + ' e:' + bounds.getEast() + ' s:' + bounds.getSouth() + ' z:' + schema_leafletmap.getZoom());
} 

function svg_add_to_schema(x, y, x2, y2, svgString, svgId) {
  schema_svgRoot[svgId] = new DOMParser().parseFromString(svgString, "image/svg+xml").documentElement;
  var dimension = "0 0 " + (x2-x).toString() + " " + (y2-y).toString();// dimension matches svgOverlay size, to create 1-to-1 pixel mapping
  schema_svgRoot[svgId].setAttribute('viewBox', dimension );
  L.svgOverlay(schema_svgRoot[svgId], [ [ y,x], [ y2,x2 ] ]).addTo(schema_leafletmap);
  //console.log("x:" + x + " y:" + y + " x2:" + x2 + " y2:" + y2); 
  schema_svgRoot[svgId].id = svgId;
  return schema_svgRoot[svgId];
}

var update_gis = function(){ 
  //pos = gis_map.getCenter();
  zoom = gis_map.getZoom();
  bounds = gis_map.getBounds();
  socket.emit('get_svg_for_gis', {'w': bounds.getWest(), 'n': bounds.getNorth(), 'e': bounds.getEast(), 's': bounds.getSouth(), 'z': zoom, 'in_view': gis_in_view});
  //console.log('w:' + bounds.getWest() + ' n:' + bounds.getNorth() + ' e:' + bounds.getEast() + ' s:' + bounds.getSouth());
} 

function svg_add_to_gis(x, y, x2, y2, svgString, svgId, location) {
  gis_svgRoot[svgId] = new DOMParser().parseFromString(svgString, "image/svg+xml").documentElement;
  var dimension = "0 0 " + (x2-x).toString() + " " + (y2-y).toString();
  gis_svgRoot[svgId].setAttribute('viewBox', dimension );
  var la = location['height']/2;
  var lo = location['width']/2;
  var longtitude = location['coordinates'][0];
  var latitude = location['coordinates'][1];
  L.svgOverlay(gis_svgRoot[svgId], [ [ latitude-la,longtitude-lo], [ latitude+la,longtitude+lo ] ]).addTo(gis_map);

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

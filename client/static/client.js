var socket;
var schema_leafletmap, schema_geojsonlayer, schema_in_view, schema_editableLayers; 
var gis_leafletmap, gis_geojsonlayer,gis_in_view, gis_editableLayers;

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

  L.easyButton('<span style="font-size: 1.5em;">&starf;</span>', toggle_view ).addTo( schema_leafletmap );

  schema_editableLayers = new L.FeatureGroup();
  schema_leafletmap.addLayer(schema_editableLayers);

  schema_geojsonlayer = L.geoJSON().addTo(schema_leafletmap);

  let schema_options = {
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
      marker: true,
      svg: true
    },
    edit: {
      featureGroup: schema_editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  
  let schema_drawControl = new L.Control.Draw(schema_options);
  schema_leafletmap.addControl(schema_drawControl);

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

  L.easyButton('<span style="font-size: 1.5em;">&starf;</span>', toggle_view ).addTo( gis_leafletmap );

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
      circle: true, // Turns off this drawing tool 
      rectangle: true,
      marker: true
    },
    edit: {
      featureGroup: gis_editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  let gis_drawControl = new L.Control.Draw(gis_options);
  gis_leafletmap.addControl(gis_drawControl);

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
        if (layer.uuid === null){
          layer.uuid = ret;
        }
      }
    );
  }
  else if (layer.toGeoJSON){ //geojson item
    layer.type = "Feature";
    let geojson = layer.toGeoJSON();
    geojson["properties"]['type'] = "geojson";
    geojson["properties"]['datapoints'] = {};

    socket.emit('schema_addGeojsonItem', geojson ,
    function(ret){
      if (layer.uuid === null){
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
        if (layer.uuid === null){
          layer.uuid = ret;
        }
      }
    );
  }
  else if (layer.toGeoJSON){ //geojson item
    layer.type = "Feature";
    let geojson = layer.toGeoJSON();
    geojson["properties"]['type'] = "geojson";
    geojson["properties"]['datapoints'] = {};
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
      geojson["properties"]['datapoints'] = {};

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
      geojson["properties"]['datapoints'] = {};

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








function toggle_view() {
  let gis = document.getElementById("gis_map");
  let schema_div = document.getElementById("mmi_svg");
  if (gis.style.display === "none") {
    document.getElementById("mmi_svg").style.display = "none";
    document.getElementById("gis_map").style.display = "block";
  } else {
    document.getElementById("mmi_svg").style.display = "block";
    document.getElementById("gis_map").style.display = "none";
  }
} 

$(document).ready(function() {
  namespace = '';
  socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
  init_gis();
  init_schema();
  document.getElementById("mmi_svg").style.display = "block";
  document.getElementById("gis_map").style.display = "none";

  //////////////////////////////////////////////////////////////////////////

  socket.on('svg_value_update_event_on_schema', function (data) {
    //event gets called from server when svg data is updated, so update the svg
    let element = data['element'];
    let value = data['data']['value'];
    let type = data['data']['type'];
  });

  socket.on('updateDataPoint', function (data) { 
    console.log("called:" + data.toString());
  });

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

    schema_in_view.push(data['id']);

      //register for all values in loaded svg
    $("g",node._image).find("*").each(function(idx, el){
      let cl = el.classList.toString();
      //console.log("el.id:" + el.id + " cl:"+cl);
      if(el.id.startsWith("iec60870://") == true){ 
        //register  
        socket.emit('register_datapoint', el.id); 
        if(cl == "XCBR"){ $("#close",el)[0].beginElementAt(1.0); }
        if(cl == "XSWI"){ $("#open",el)[0].beginElementAt(1.0); }
      }
    });
  });

  socket.on('svg_object_remove_from_schema', function (data) {
    //remove svg from object
    let obj = null
    for(let item in schema_editableLayers._layers){
      if(schema_editableLayers._layers[item].uuid === data){
          obj = schema_editableLayers._layers[item];
          break; // If you want to break out of the loop once you've found a match
      }
    }
    if(obj != null){
      //unregister values in this svg
      $("g",obj._image).find("*").each(function(idx, el){
        let cl = el.classList.toString();
        if(el.id.startsWith("iec60870://") == true){    
          //unregister
          socket.emit('unregister_datapoint', el.id);
        }
      });
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
      local_geojsonlayer.setStyle(geoStyle);

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

          schema_editableLayers.addLayer(local_geojsonlayer._layers[local_geoitem]);
          schema_geojsonlayer.addLayer(local_geojsonlayer._layers[local_geoitem]);
        }
      }
		}
  });

  socket.on('geojson_object_update_schema', function () {
    //add geojson to object
    schema_geojsonlayer.setStyle(geoStyle);
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
    gis_in_view.push(data['id']);
      //register for all values in loaded svg
    $("g",node._image).find("*").each(function(idx, el){
      let cl = el.classList.toString();
      //console.log("el.id:" + el.id + " cl:"+cl);
      if(el.id.startsWith("iec60870://") == true){    
        if(cl == "XCBR"){ $("#close",el)[0].beginElementAt(1.0); }
        if(cl == "XSWI"){ $("#open",el)[0].beginElementAt(1.0); }
      }
    });
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
      //unregister values in this svg
      $("g",obj).find("*").each(function(idx, el){
        let cl = el.classList.toString();
        if(el.id.startsWith("iec60870://") == true){    
          //unregister
        }
      });
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
      local_geojsonlayer.setStyle(geoStyle);

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

          gis_editableLayers.addLayer(local_geojsonlayer._layers[local_geoitem]);
          gis_geojsonlayer.addLayer(local_geojsonlayer._layers[local_geoitem]);
        }
      }
		}
  });

  socket.on('geojson_object_update_gis', function () {
    //add geojson to object
    gis_geojsonlayer.setStyle(geoStyle);
  });

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
  // add to gis layer
  gis_editableLayers.addLayer(svg);
  return svg;
}

/////////////////////////////////////////////////////////////////////////////

//https://github.com/orfon/Leaflet.SLD/blob/master/leaflet.sld.js ????
var geoStyle = function(feature){
  color = "#ff7800";
  //retrieve color from real-time database
  if(feature.properties.id == "one"){ color = "#ffff00"; }
  if(!feature.properties.stroke){
    return {
      "color": color,
      "weight": 5,
      "opacity": 0.65
    };
  }

  return {
    fillColor: feature.properties['fill'],
    fillOpacity: feature.properties['fill-opacity'],
    color: feature.properties['stroke'],
    width: feature.properties['stroke-width'],
    opacity: feature.properties['stroke-opacity']
  };//*/
}

function setGeojsonStyle(layer){
  //console.log(e);
  layer.feature.properties['fill'] = layer.options.fillColor;
  layer.feature.properties['fill-opacity'] = layer.options.fillOpacity;
  layer.feature.properties['stroke'] = layer.options.color;
  layer.feature.properties['stroke-width'] = layer.options.width;
  layer.feature.properties['stroke-opacity'] = layer.options.opacity;
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
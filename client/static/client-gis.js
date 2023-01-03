var gis_in_view;
 
function init_gis(){
  gis_in_view = [];

  leafletmap = L.map('mmi_svg', { 
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
  }).addTo(leafletmap);//*/

  //register svg events
  leafletmap.on(L.Draw.Event.CREATED, gis_addItem);//*/
  leafletmap.on(L.Draw.Event.EDITED, gis_editedItems);
  leafletmap.on(L.Draw.Event.DELETED, gis_removeItems);
  leafletmap.on('moveend', update_gis);
  leafletmap.on('zoomend', update_gis);

  //ensure layers are not updated from database during editing or removing
  leafletmap.on('draw:editstart', function(){ leafletmap.off('moveend', update_gis); leafletmap.off('zoomend', update_gis);} );
  leafletmap.on('draw:editstop', function(){leafletmap.on('moveend', update_gis);  leafletmap.on('zoomend', update_gis);} );
  leafletmap.on('draw:deletestart', function(){leafletmap.off('moveend', update_gis);  leafletmap.off('zoomend', update_gis);} );
  leafletmap.on('draw:deletestop', function(){leafletmap.on('moveend', update_gis);  leafletmap.on('zoomend', update_gis);} );

  if(location.hash === ""){ //ensure were not setting a location in the url
    leafletmap.setZoom(18);
  }



  socket.on('svg_object_add_to_gis', function (data) {
    //add svg to object
    if(gis_in_view.includes(data['id'])){
      return;
    }
    let node = svg_add_to_gis(data['svg'],data['id'],data['location']);
    if(node == null){
      return;
    }
    node.on("click", show_Sidebar);

    if('properties' in data){
      node._dataPoints = data["properties"]['datapoints'];
      node.options.svg = data["properties"]['svg'];
      if('z_min' in data['properties']){
        node.options.z_min = data['properties']['z_min'];
      }
      if('z_max' in data['properties']){
        node.options.z_max = data['properties']['z_max'];
      }
    }

    for (const [key, point] of Object.entries(node._dataPoints)) {
      for (const [child_key, child_point] of Object.entries(point)) {
        socket.emit('register_datapoint', child_key);
        local_data_cache_norefresh[child_key] = false;
      }
    }
    node._image.layerNode = node;//for onclick events in svg, to find the node back

    gis_in_view.push(data['id']);
  });

  socket.on('svg_object_remove_from_gis', function (data) {
    //remove svg from object
    let obj = null
    for(let item in editableLayers._layers){
      if(editableLayers._layers[item].uuid === data){
          obj = editableLayers._layers[item];
          break; // If you want to break out of the loop once you've found a match
      }
    }
    if(obj != null){
      for (const [key, point] of Object.entries(obj._dataPoints)) {
        for (const [child_key, child_point] of Object.entries(point)) {
          socket.emit('unregister_datapoint', child_key);
        }
      }

      editableLayers.removeLayer(obj);
      let index = gis_in_view.indexOf(data);
      if (index > -1) {
        gis_in_view.splice(index, 1);
      }
    }
  });

}


function gis_addItem(e) {
  let type = e.layerType, layer = e.layer;

  if (type === 'svg') {
    layer.type = "Svg";
    layer.on("click", show_Sidebar);

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
    layer._dataPoints = {};
    layer.on("click", show_Sidebar);

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
  editableLayers.addLayer(layer);
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

      let properties = Object.assign({},layer.options);//EDIT
      properties['datapoints'] = layer._dataPoints;
      properties['svg'] = layer.options.svg;

      socket.emit('gis_editedItems', {
        '_id':layer.uuid,
        'type': layer.type,
        "location": { "type": "Point", 
                      "coordinates": [ latlng.lng, latlng.lat ], //coords are switched position from leaflet in geojson
                      "height": bounds._northEast.lat - bounds._southWest.lat, 
                      "width": bounds._northEast.lng - bounds._southWest.lng, 
                    },
        "properties": properties,
        //{
          //'datapoints': layer._dataPoints,
          //'z_min': properties.z_min,
          //'z_max': properties.z_max,
        //} 
      });
    }
  }
}



function gis_removeItems(e){
  for (const [key, layer] of Object.entries(e.layers._layers)) {
    socket.emit('gis_removeItems', layer.uuid);
  }
}


var update_gis = function(){ 
  zoom = leafletmap.getZoom();
  bounds = leafletmap.getBounds();
  socket.emit('get_objects_for_gis', {'w': bounds.getWest(), 'n': bounds.getNorth(), 'e': bounds.getEast(), 's': bounds.getSouth(), 'z': zoom, 'in_view': gis_in_view});
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
  editableLayers.addLayer(svg);
  return svg;
}






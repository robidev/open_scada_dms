var schema_in_view; 

//https://stackoverflow.com/questions/62305306/invert-y-axis-of-lcrs-simple-map-on-vue2-leaflet
var CRSPixel = L.Util.extend(L.CRS.Simple, {
	transformation: new L.Transformation(1,0,1,0)
});

function init_schema(){
  schema_in_view = [];

  leafletmap = L.map('mmi_svg', { 
    renderer: L.svg(), 
    crs: CRSPixel,
    minZoom: 0,//-5
    maxZoom: 20,
    mapType: "schema"
  }).setView([0, 0], 17);//setView([0,0], 1);

  leafletmap.on(L.Draw.Event.CREATED, schema_addItem);
  leafletmap.on(L.Draw.Event.EDITED, schema_editedItems);
  leafletmap.on(L.Draw.Event.DELETED, schema_removeItems);
  leafletmap.on('moveend', update_schema);
  leafletmap.on('zoomend', update_schema);

  //do not update map when editing, to prevent layer modification from database during editing
  leafletmap.on('draw:editstart', function(){ leafletmap.off('moveend', update_schema); leafletmap.off('zoomend', update_schema);} );
  leafletmap.on('draw:editstop', function(){leafletmap.on('moveend', update_schema); leafletmap.on('zoomend', update_schema);} );
  leafletmap.on('draw:deletestart', function(){leafletmap.off('moveend', update_schema); leafletmap.off('zoomend', update_schema);} );
  leafletmap.on('draw:deletestop', function(){leafletmap.on('moveend', update_schema); leafletmap.on('zoomend', update_schema);} );

  if(location.hash === ""){ //ensure were not setting a location in the url
    leafletmap.setZoom(18);
  }


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
    node.on("click", show_Sidebar);
    for (const [key, point] of Object.entries(node._dataPoints)) {
      for (const [child_key, child_point] of Object.entries(point)) {
        socket.emit('register_datapoint', child_key);
        local_data_cache_norefresh[child_key] = false;
      }
    }
    node._image.layerNode = node;//for onclick events in svg, to find the node back

    schema_in_view.push(data['id']);
  });

  socket.on('svg_object_remove_from_schema', function (data) {
    //remove svg from object
    let obj = null
    for(let item in editableLayers._layers){
      if(editableLayers._layers[item].uuid === data){
          obj = editableLayers._layers[item];
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
      editableLayers.removeLayer(obj);
      let index = schema_in_view.indexOf(data);
      if (index > -1) {
        schema_in_view.splice(index, 1);
      }
    }
  });
}



function schema_addItem(e) {
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
    layer.on("click", show_Sidebar);

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
  editableLayers.addLayer(layer);
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

var update_schema = function(){ 
  zoom = leafletmap.getZoom();
  bounds = leafletmap.getBounds();
  socket.emit('get_svg_for_schema', {'w': bounds.getWest(), 'n': bounds.getSouth(), 'z': zoom, 'in_view': schema_in_view, 'e': bounds.getEast(), 's': bounds.getNorth()});
} 


function svg_add_to_schema(w, n, e, s, svgString, svgId) {
  let svg = new L.SvgObject(svgString, L.latLngBounds([[n,w],[s,e]]), svgId,{ svgViewBox:{ viewBox: "calculate", fitBounds: false, scaleBounds:  0.000005/*1.0*/ }});
  svg.type = "Svg";
  editableLayers.addLayer(svg);
  return svg;
}





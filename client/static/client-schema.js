var schema_in_view; 

//we use an inverted Y axis for this non geographic coordinate reference system
//https://stackoverflow.com/questions/62305306/invert-y-axis-of-lcrs-simple-map-on-vue2-leaflet
var CRSPixel = L.Util.extend(L.CRS.Simple, {
	transformation: new L.Transformation(1,0,1,0)
});

function init_schema(){
  schema_in_view = [];

  leafletmap = L.map('mmi_svg', { 
    renderer: L.svg(), 
    crs: CRSPixel, //non geographic map with inverted Y axis
    minZoom: 0,//-5
    maxZoom: 22,
    mapType: "schema"
  }).setView([0, 0], 17);//setView([0,0], 1);

  //register events for map display and edits
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

  if(location.hash === ""){ //ensure we're not setting a location in the url
    leafletmap.setZoom(18);
  }

    //add svg to object
  socket.on('svg_object_add_to_schema', function (data) {
    //bail if object already in view
    if(schema_in_view.includes(data['id'])){
      return;
    }
    //add svg to leaflet map
    let layer = svg_add_to_schema(data['w'],data['n'],data['e'],data['s'],data['svg'],data['id']);
    if(layer == null){ //dont continue if object could not be added
      return;
    }

    if('properties' in data){
      layer.properties = data["properties"];
      layer._dataPoints = data["properties"]['datapoints'];
          //find svg elements that need instantiation in list of overrides
      try {
        if("overrides" in data["properties"]){
          data["properties"]['overrides'].forEach((override) => {
            overridable_instance = override["element_id"];
            overridable_property = override["property"];
            instance_value = override["value"];
            $(layer._image).find("*").each(function(idx, el){
              if(el.id == overridable_instance){ 
                el[overridable_property] = instance_value;
              }
            });
          });
        }
      } 
      catch (error) {
        console.log("error processing overrides:" + error)
      }

    }

    //register click event
    layer.on("click", show_Sidebar);
    layer._image.layerNode = layer;//reference for onclick events in svg, to find the node back
    schema_in_view.push(data['id']);//maintain a list of existing objects in view
    //register datapoints for updating from server
    for (const [key, point] of Object.entries(layer._dataPoints)) {
      for (const [child_key, child_point] of Object.entries(point)) {
        socket.emit('register_datapoint', child_key);
        local_data_cache_norefresh[child_key] = false;
      }
    }
  });

  socket.on('svg_object_remove_from_schema', function (data) {
    //remove svg from object
    let layer = null
    for(let item in editableLayers._layers){
      if(editableLayers._layers[item].uuid === data){
        layer = editableLayers._layers[item];
        break; 
      }
    }
    if(layer != null){
      //unregister values in this svg
      for (const [key, point] of Object.entries(layer._dataPoints)) {
        for (const [child_key, child_point] of Object.entries(point)) {
          socket.emit('unregister_datapoint', child_key);
        }
      }
      editableLayers.removeLayer(layer);
      let index = schema_in_view.indexOf(data);
      if (index > -1) {
        schema_in_view.splice(index, 1);
      }
    }
  });
}


//function if item(svg/geojson) is added via the editor
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
        'datapoint_amount':layer._dataPoints.length //TODO: is this even used?
      });
    }

    let bounds = layer.getBounds();
    layer.properties = layer.options;

    layer.properties['datapoints'] = layer._dataPoints;
    socket.emit('schema_addItems', {
      'w':bounds._northEast.lng,
      'n':bounds._northEast.lat,
      'e':bounds._southWest.lng,
      's':bounds._southWest.lat,
      'svg':layer._templateName, 
      "properties": layer.properties,
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
    layer.feature.properties['fillEnabled'] = layer.options.fill;//true/false
    layer.feature.properties['fill'] = layer.options.fillColor;
    layer.feature.properties['fill-opacity'] = layer.options.fillOpacity;
    layer.feature.properties["fillRule"] = layer.options.fillRule;
    layer.feature.properties['strokeEnabled' ] = layer.options.stroke;//true/false
    layer.feature.properties['stroke'] = layer.options.color;
    layer.feature.properties['stroke-width'] = layer.options.weight;
    layer.feature.properties['stroke-opacity'] = layer.options.opacity;
    layer.feature.properties['stroke-cap'] = layer.options.lineCap;// "round",
    layer.feature.properties['stroke-join'] = layer.options.lineJoin;// "round",
    layer.feature.properties['stroke-dashArray'] = layer.options.dashArray;// null,
    layer.feature.properties['stroke-dashOffset'] = layer.options.dashOffset;// null,
    layer.feature.properties['smoothFactor'] = layer.options.smoothFactor;//": 1,
    layer.feature.properties['noClip'] = layer.options.noClip;// false,

    layer.feature.properties['datapoints'] = layer._dataPoints;

    let geojson = layer.toGeoJSON();
    if (layer instanceof L.Circle) { //add circles to geojson
      geojson.properties.radius = layer.getRadius();
    }
    
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
      if (layer instanceof L.Circle) { //add circles to geojson
        geojson.properties.radius = layer.getRadius();
      }

      geojson["properties"]['datapoints'] = layer._dataPoints;

      socket.emit('schema_editedGeojsonItems', {
        '_id':layer.uuid,
        'type': layer.type,
        'geometry':geojson['geometry'],
        'properties':geojson['properties'],
      });
    }
    else if(layer.type && layer.type === "Svg"){
      let bounds = layer.getBounds();
      layer.properties['datapoints'] = layer._dataPoints;

      socket.emit('schema_editedItems', {
        '_id':layer.uuid,
        'w':bounds._northEast.lng,
        'n':bounds._northEast.lat,
        'e':bounds._southWest.lng,
        's':bounds._southWest.lat,
        "properties": layer.properties,
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
  //warning, due to different coordinate system, north and south are reversed
  socket.emit('get_objects_for_schema', {'w': bounds.getWest(), 'n': bounds.getSouth(), 'z': zoom, 'in_view': schema_in_view, 'e': bounds.getEast(), 's': bounds.getNorth()});
} 


function svg_add_to_schema(w, n, e, s, svgString, svgId) {
  let svg = new L.SvgObject(svgString, L.latLngBounds([[n,w],[s,e]]), svgId,{ svgViewBox:{ viewBox: "calculate", fitBounds: false, scaleBounds:  0.000005/*1.0*/ }});
  svg.type = "Svg";
  editableLayers.addLayer(svg);
  return svg;
}





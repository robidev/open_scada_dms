var gis_in_view;
 
function init_gis(){
  gis_in_view = [];

  leafletmap = L.map('mmi_svg', { 
    renderer: L.svg(),
    mapType: "gis"
  }).setView([51.99461, 5.82955], 17);
  //gis_map = new L.Map('gis_map').setView([51.980, 5.842], 17);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'openstreetmap',
    maxZoom: 24,
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
    let layer = svg_add_to_gis(data['svg'],data['id'],data['location']);
    if(layer == null){
      return;
    }
    layer.on("click", show_Sidebar);

    if('properties' in data){
      layer._dataPoints = data["properties"]['datapoints'];
      layer.properties = data["properties"];
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

    layer._image.layerNode = layer;//for onclick events in svg, to find the node back
    gis_in_view.push(data['id']);
    for (const [key, point] of Object.entries(layer._dataPoints)) {
      for (const [child_key, child_point] of Object.entries(point)) {
        socket.emit('register_datapoint', child_key);
        local_data_cache_norefresh[child_key] = false;
      }
    }
  });

  socket.on('svg_object_remove_from_gis', function (data) {
    //remove svg from object
    let layer = null
    for(let item in editableLayers._layers){
      if(editableLayers._layers[item].uuid === data){
        layer = editableLayers._layers[item];
        break; // If you want to break out of the loop once you've found a match
      }
    }
    if(layer != null){
      for (const [key, point] of Object.entries(layer._dataPoints)) {
        for (const [child_key, child_point] of Object.entries(point)) {
          socket.emit('unregister_datapoint', child_key);
        }
      }

      editableLayers.removeLayer(layer);
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

    layer.feature["properties"]['datapoints'] = layer._dataPoints;

    let geojson = layer.toGeoJSON();
    if (layer instanceof L.Circle) { //add circles to geojson
      geojson.properties.radius = layer.getRadius();
    }

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
      if (layer instanceof L.Circle) { //add circles to geojson
        geojson.properties.radius = layer.getRadius();
      }

      geojson["properties"]['datapoints'] = layer._dataPoints;

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
      layer.properties['datapoints'] = layer._dataPoints;

      socket.emit('gis_editedItems', {
        '_id':layer.uuid,
        'type': layer.type,
        "location": { "type": "Point", 
                      "coordinates": [ latlng.lng, latlng.lat ], //coords are switched position from leaflet in geojson
                      "height": bounds._northEast.lat - bounds._southWest.lat, 
                      "width": bounds._northEast.lng - bounds._southWest.lng, 
                    },
        "properties": layer.properties,
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






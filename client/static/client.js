var socket;
var schema_leafletmap, schema_in_view, schema_editableLayers; 
var gis_leafletmap, geojsonlayer,gis_in_view, gis_editableLayers;

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

  geojsonlayer = L.geoJSON().addTo(gis_leafletmap);

  
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
  gis_leafletmap.setZoom(18);
}

function exportGeoJSON(featureGroup) {
  // Extract GeoJson from featureGroup
  let data = featureGroup.toGeoJSON();
  // Stringify the GeoJson
  let convertedData = 'text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(data));
  // Create export
  let linkElement = document.createElement('a');
  linkElement.setAttribute('href', 'data:' + convertedData);
  linkElement.setAttribute('download','data.geojson');
  linkElement.click();
}

function gis_addItem(e) {
  //gis_map.on(L.Draw.Event.CREATED, function(e) {
  let type = e.layerType, layer = e.layer;

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }
  if (type === 'svg') {
    if (layer.uuid === null){
      layer.uuid = "_123";
    }
  }
  gis_editableLayers.addLayer(layer);
}

function gis_editedItems(items){
    //items.layers.{}
    //check feature._id->geojson or uuid->svg
}

function gis_removeItems(items){
  //items.layers.{}
  //check feature._id->geojson or uuid->svg
  //result = mongo.db.xxx.delete_one({'_id': ObjectId(_id)})
}



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
    minZoom: -5,
    maxZoom: 10,
    mapType: "schema"
  }).setView([0,0], 1);

  schema_editableLayers = new L.FeatureGroup();
  schema_leafletmap.addLayer(schema_editableLayers);

    //geojsonlayer = L.geoJSON().addTo(schema_leafletmap);

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
  schema_leafletmap.setZoom(0);
}





function schema_addItem(e) {
  //gis_map.on(L.Draw.Event.CREATED, function(e) {
  let type = e.layerType, layer = e.layer;

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }
  if (type === 'svg') {
    if (layer.uuid === null){
      layer.uuid = "_123";
    }
  }
  schema_editableLayers.addLayer(layer);
  //mydict = { "name": "Peter", "address": "Lowstreet 27" }
  //x = mycol.insert_one(mydict)
}

function schema_editedItems(items){
  //items.layers.{}
  //mycollection.update({'_id':mongo_id}, {"$set": post}, upsert=False)
}

function schema_removeItems(items){
  //items.layers.{}
  //result = mongo.db.xxx.delete_one({'_id': ObjectId(_id)})
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
    node = svg_add_to_schema(data['x'],data['y'],data['x2'],data['y2'],data['svg'],data['id']);
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

  socket.on('svg_object_add_to_gis', function (data) {
    //add svg to object
    if(gis_in_view.includes(data['id'])){
      return;
    }
    let node = svg_add_to_gis(data['x'],data['y'],data['x2'],data['y2'],data['svg'],data['id'],data['location']);
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
          gis_editableLayers.addLayer(local_geojsonlayer._layers[local_geoitem]);
          geojsonlayer.addLayer(local_geojsonlayer._layers[local_geoitem]);
        }
      }
		}
  });

  socket.on('geojson_object_update_gis', function () {
    //add geojson to object
    geojsonlayer.setStyle(geoStyle);
  });

});


var update_schema = function(){ 
  zoom = schema_leafletmap.getZoom();
  bounds = schema_leafletmap.getBounds();
  socket.emit('get_svg_for_schema', {'x': bounds.getWest(), 'y': bounds.getSouth(), 'z': zoom, 'in_view': schema_in_view, 'x2': bounds.getEast(), 'y2': bounds.getNorth()});
} 

var update_gis = function(){ 
  zoom = gis_leafletmap.getZoom();
  bounds = gis_leafletmap.getBounds();
  socket.emit('get_svg_for_gis', {'w': bounds.getWest(), 'n': bounds.getNorth(), 'e': bounds.getEast(), 's': bounds.getSouth(), 'z': zoom, 'in_view': gis_in_view});
} 

function svg_add_to_schema(x, y, x2, y2, svgString, svgId) {
  let svg = new L.SvgObject(svgString, L.latLngBounds([[y,x],[y2,x2]]), svgId,{ svgViewBox:{ viewBox: "calculate", fitBounds: true, scaleBounds: 1.0 }});
  schema_editableLayers.addLayer(svg);
  return svg;
}

function svg_add_to_gis(x, y, x2, y2, svgString, svgId, location) {
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
    { svgViewBox:{ viewBox: "calculate", fitBounds: true, scaleBounds: 0.000005 }}
  );

  //svg.setBounds([ [ latitude-hheight,longtitude-hwidth], [ latitude+hheight,longtitude+hwidth ] ]);

  // add to gis layer
  gis_editableLayers.addLayer(svg);
  return svg;
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


////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
var get_svg_templates = function()
{
  return [["PTR",[[0,0],[550,514]],"<line id=\"S12/D1/Q1/L1\" class=\"LINE\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"153.934719\" x2=\"266\" y1=\"93.434721\" x1=\"266\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"none\"/>\n\n<g id=\"S12/D1/T1\">\n<title>PTR</title>\n<ellipse id=\"svg_T1_a\" ry=\"18\" rx=\"18\" cy=\"171.753014\" cx=\"266\" fill-opacity=\"null\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"none\"/>\n<text    id=\"svg_T1_name\" stroke=\"#ffffff\"  xml:space=\"preserve\" text-anchor=\"start\" font-family=\"Helvetica, Arial, sans-serif\" font-size=\"24\" y=\"186.66199\" x=\"296\" stroke-width=\"null\" fill=\"#ffffff\">T1</text>\n<ellipse id=\"svg_T1_b\" ry=\"18\" rx=\"18\" cy=\"196.290907\" cx=\"266\" fill-opacity=\"null\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"none\"/>\n</g>\n\n<line id=\"S12/E1/Q1/L2\" class=\"LINE\" stroke=\"#ffffff\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"256.43483\" x2=\"266\" y1=\"214.934859\" x1=\"266\" stroke-width=\"1.5\" fill=\"none\"/>\n"],
          ["CBR",[[0,0],[550,514]],"<g id=\"S12/E1/Q1/QA1\" class=\"draggable-group\">\n<title>CBR</title>\n<text id=\"$datapoint_1\"     class=\"MEAS\" data-text=\"CBR: QA1=\\{value\\}\" fill=\"#ffffff\" stroke=\"#ffffff\" x=\"296\" y=\"272.166593\" font-size=\"12\" font-family=\"Helvetica, Arial, sans-serif\" text-anchor=\"start\" xml:space=\"preserve\" font-weight=\"normal\" font-style=\"normal\"></text>\n<rect id=\"$datapoint_2\"     class=\"XCBR\" height=\"22.553162\" width=\"19.999974\" y=\"257.946454\" x=\"256.364398\" stroke-width=\"1.5\" stroke=\"#ffffff\" fill=\"#ffffff\">\n  <animate id=\"open\" attributeName=\"fill\" attributeType=\"XML\" to=\"black\" dur=\"100ms\" fill=\"freeze\" />\n  <animate id=\"transition\" attributeName=\"fill\" attributeType=\"XML\" to=\"green\" dur=\"10ms\" fill=\"freeze\" />\n  <animate id=\"close\" attributeName=\"fill\" attributeType=\"XML\"  to=\"white\" dur=\"100ms\" fill=\"freeze\" /> \n  <animate id=\"error\" attributeName=\"fill\" attributeType=\"XML\"  to=\"red\" dur=\"10ms\" fill=\"freeze\" />           \n</rect>\n<rect id=\"$datapoint_3\"     class=\"CSWI\" height=\"22.553162\" width=\"19.999974\" y=\"257.946454\" x=\"256.364398\" stroke-width=\"1.5\" stroke=\"none\" fill=\"none\"/>\n</g>"],
          ["SWI",[[0,0],[550,514]],"<g id=\"S12/E1/Q1/QB1\" class=\"draggable-group\">\n<title>SWI</title>\n<text id=\"$datapoint_1\"     class=\"MEAS\" data-text=\"DIS: QB1=\\{value\\}\" fill=\"#ffffff\" stroke=\"#ffffff\" x=\"296\" y=\"314.666538\" font-size=\"12\" font-family=\"Helvetica, Arial, sans-serif\" text-anchor=\"start\" xml:space=\"preserve\" font-weight=\"normal\" font-style=\"normal\"></text>\n<rect id=\"$datapoint_2\"    class=\"CSWI\" height=\"19\" width=\"19\" y=\"300.49959\" x=\"256.864387\" stroke=\"#ffffff\" fill=\"#000000\"/> \n<line id=\"$datapoint_3\"     class=\"XSWI\" stroke=\"#ffffff\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"320\" x2=\"266\" y1=\"300\" x1=\"266\" stroke-width=\"4\" fill=\"none\">\n    <animateTransform id=\"open\" attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" to=\"90 266 310 \" dur=\"100ms\" fill=\"freeze\" />\n    <animateTransform id=\"close\" attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" to=\"0 266 310 \" dur=\"100ms\" fill=\"freeze\" />\n    <animateTransform id=\"transition\" attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" to=\"45 266 310 \" dur=\"100ms\" fill=\"freeze\" />\n    <animateTransform id=\"error\" attributeName=\"stroke\" attributeType=\"XML\" to=\"red\" dur=\"100ms\" fill=\"freeze\" />\n</line>\n</g>"],
          ["Load",[[0,0],[550,514]],"<line id=\"S12/E1/W1/BB1\" class=\"LINE\" stroke=\"#ffffff\" stroke-linecap=\"undefined\" stroke-linejoin=\"undefined\" y2=\"360\" x2=\"266\" y1=\"320.436511\" x1=\"266\" stroke-width=\"1.5\" fill=\"none\"/>\n<text id=\"LOAD\" class=\"LOAD\" stroke=\"#ffffff\"  xml:space=\"preserve\" text-anchor=\"middle\" font-family=\"Helvetica, Arial, sans-serif\" font-size=\"24\" y=\"380\" x=\"266\" fill=\"#ffffff\">Load</text>\n"],
          ["Feed",[[0,0],[550,514]],"<title>Bay 1</title>\n<text id=\"IFL\" class=\"IFL\" stroke=\"#ffffff\" xml:space=\"preserve\" text-anchor=\"middle\" font-family=\"Helvetica, Arial, sans-serif\" font-size=\"24\" y=\"80\" x=\"266\" fill=\"#ffffff\">220KV Feed</text>\n<ellipse id=\"svg_top\" stroke=\"#ffffff\" ry=\"2.424242\" rx=\"2.121212\" cy=\"91.858974\" cx=\"266\" fill-opacity=\"null\" stroke-width=\"1.5\" fill=\"none\"/>\n"]];
}

	//.leaflet-modal
L.Draw.Svg.include({
	  enable: function(){
      let drawsvg = this;
      let templates = get_svg_templates();

      let options = "";
      for(let i = 0; i < templates.length; i++){
        options += '<option value="'+i.toString()+'"> '+ templates[i][0] +' </option>';
      }
      
      this._map.fire('modal', {
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
          '<input type="file" id="file-input" />',
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

          fitSvg(templates[0][2], modal._container.querySelector('#preview'));

          L.DomEvent
          .on(modal._container.querySelector('.modal-ok'), 'click', function() {
            let sel = modal._container.querySelector('select[name="SVG-templates"]');

            if(imported == null){
              let bbox = fitSvg(templates[sel.value][2], modal._container.querySelector('#preview'));//to retrieve the bounds, and write to current_bbox
              drawsvg._svgViewBox = (bbox.x).toString() + " " + (bbox.y).toString() + " " + (bbox.width).toString() + " " + (bbox.height).toString();
              drawsvg._svgFitBounds = true;
              if(drawsvg._map.options.mapType === "schema"){
                drawsvg._scale = 1.0;
              }
              if(drawsvg._map.options.mapType === "gis"){
                drawsvg._scale = 0.000005;
              }

              drawsvg._template = templates[sel.value][2];
            } else {
              let bbox = fitSvg(imported, modal._container.querySelector('#preview'));//to retrieve the bounds, and write to current_bbox
              drawsvg._svgViewBox = (bbox.x).toString() + " " + (bbox.y).toString() + " " + (bbox.width).toString() + " " + (bbox.height).toString();
              drawsvg._svgFitBounds = true;
              if(drawsvg._map.options.mapType === "schema"){
                drawsvg._scale = 1.0;
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
            fitSvg(templates[parseInt(this.value)][2],  modal._container.querySelector('#preview'));
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
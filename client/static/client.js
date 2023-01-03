var socket;
var local_data_cache, local_data_cache_norefresh;
var sidebar, leafletmap, isEditEnabled, editableLayers, geojsonlayer;


$(document).ready(function() {
  local_data_cache = {};
  local_data_cache_norefresh = {};
  namespace = '';

  socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

  let focus = document.getElementById("focus").value
  if(focus === "1"){ // gis view
    init_gis();
    init_mapelements();
  }
  else if(focus === "2"){ // alarm view
    init_alarm();
  }
  else if(focus === "3"){ // event view
    init_events();
  }
  else if(focus === "4"){ // event view
    init_dataproviders();
  }
  else{ //default is schema view
    init_schema();
    init_mapelements();
  }

});



//////////////////////////////////////////////////////////////////////////////
//leaflet maps

function init_mapelements(){
  geojsonlayer = L.geoJSON().addTo(leafletmap);

  //https://codepen.io/mochaNate/pen/bWNveg
  editableLayers = new L.FeatureGroup();
  leafletmap.addLayer(editableLayers);

  let options = {
    position: 'topleft',
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
      featureGroup: editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  let drawControl = new L.Control.Draw(options);
  var isEditEnabled = false;
  document.getElementById("info_panel").style.display = "block";
  document.getElementById("edit_panel").style.display = "none";

  L.easyButton('fa-globe', function(){
    if(isEditEnabled == true){
      leafletmap.removeControl(drawControl);
      document.getElementById("info_panel").style.display = "block";
      document.getElementById("edit_panel").style.display = "none";
      isEditEnabled = false;
    }else{
      leafletmap.addControl(drawControl);
      document.getElementById("info_panel").style.display = "none";
      document.getElementById("edit_panel").style.display = "block";
      isEditEnabled = true;
    }  
  }).addTo( leafletmap );

  document.getElementById("sidebar").style.display = "block";
  sidebar = L.control.sidebar('sidebar', {
    position: 'right',
    autoPan: false,
    closeButton: true,
  });
  leafletmap.addControl(sidebar);
  L.DomEvent.on(sidebar.getCloseButton(), 'click', function () {
    sidebar.hide();
  });

  leafletmap.on('draw:editstart',   function() { sidebar.hide(); sidebar.removeFrom(leafletmap); } );
  leafletmap.on('draw:editstop',    function() { sidebar.hide(); sidebar.addTo(leafletmap); } );
  leafletmap.on('draw:deletestart', function() { sidebar.hide(); sidebar.removeFrom(leafletmap); } );
  leafletmap.on('draw:deletestop',  function() { sidebar.hide(); sidebar.addTo(leafletmap); } );

  // Set up the hash
  var hash = new L.Hash(leafletmap);

  socket.on('geojson_object_add_to_map', function (json) {
    //add geojson to object
    if (json) {
      let local_geojsonlayer = L.geoJSON();

      // parse the json into leaflet layers
      local_geojsonlayer.addData(json);

      for(let edititem in editableLayers._layers){
        if('feature' in editableLayers._layers[edititem]){
          let found = false;
          for(let local_geoitem in local_geojsonlayer._layers){
            if(editableLayers._layers[edititem].feature && 
              editableLayers._layers[edititem].feature._id === local_geojsonlayer._layers[local_geoitem].feature._id){
              found = true;
              break;
            }
          }
          if(found == false){
            editableLayers.removeLayer(editableLayers._layers[edititem]);
            geojsonlayer.removeLayer(editableLayers._layers[edititem]);
          }
        }
      }

      //find what layer allready exist
      for(let local_geoitem in local_geojsonlayer._layers){
        let found = false;
        for(let edititem in editableLayers._layers){
          if(editableLayers._layers[edititem].feature && 
              editableLayers._layers[edititem].feature._id === local_geojsonlayer._layers[local_geoitem].feature._id){
            found = true;
            break;
          }
        }
        if(found == false){// if geojson is not found,
          // add geojson objects to edit and geojson-layer
          local_geojsonlayer._layers[local_geoitem].uuid = local_geojsonlayer._layers[local_geoitem]['feature']['_id'];
          local_geojsonlayer._layers[local_geoitem].type = "Feature";
          local_geojsonlayer._layers[local_geoitem].on("click", show_Sidebar);
          local_geojsonlayer._layers[local_geoitem]._dataPoints = local_geojsonlayer._layers[local_geoitem]['feature']["properties"]['datapoints'];
          for (const [key, point] of Object.entries(local_geojsonlayer._layers[local_geoitem]._dataPoints)) {
            for (const [child_key, child_point] of Object.entries(point)) {
              socket.emit('register_datapoint', child_key);
              local_data_cache_norefresh[child_key] = false;
            }
          }
          getGeojsonStyle(local_geojsonlayer._layers[local_geoitem]);
          //for (const [key, point] of Object.entries(local_geojsonlayer._layers[local_geoitem]._dataPoints)) {
          //  socket.emit('register_datapoint', point);
          //}

          editableLayers.addLayer(local_geojsonlayer._layers[local_geoitem]);
          geojsonlayer.addLayer(local_geojsonlayer._layers[local_geoitem]);
        }
      }
    }
  });

  socket.on('updateDataPoint', function (data) { 
    //console.log("called:" + data.toString());
    let key = data['key'];
    let value = data['value'];

    if(local_data_cache[key] == value && local_data_cache_norefresh[key] == true){
      return;
    }
    local_data_cache[key] = value;
    local_data_cache_norefresh[key] = true;
    //console.log("key:" + key.toString() + " value:" + value.toString());
    // update svg items and geojson
    updateLayers(editableLayers._layers, key, value);
  });

}


function updateLayers(layers,key, value){
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


function show_Sidebar(e){
  let layer = e.target;
  sidebar._container.querySelector('#info_control').style.display = "none";
  sidebar._container.querySelector('#control_element').value = "";
  sidebar._container.querySelector('#control_value').value = "";
  sidebar._container.querySelector('#info_items').innerHTML = "Name: " + layer.options.name + "<br>";;
  sidebar._container.querySelector('#info_items').innerHTML += "Description: " + layer.options.description + "<br>";;

  sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.options, null, 2);
  sidebar._container.querySelector('#datapoints_field').value = JSON.stringify(layer._dataPoints, null, 2);
  sidebar.show();

  let save_btn = sidebar._container.querySelector('#sidebar-save');
  let new_save_btn = save_btn.cloneNode(true);
  save_btn.parentNode.replaceChild(new_save_btn, save_btn);

  L.DomEvent.on(new_save_btn, 'click', function(e){ 
    let layer = this;
    layer._dataPoints = JSON.parse(sidebar._container.querySelector('#datapoints_field').value);
    layer.options = JSON.parse(sidebar._container.querySelector('#options_field').value); //EDIT FIX
    if(layer.type==="Feature"){
      layer.setStyle();
      setGeojsonStyle(layer, layer.feature);
    }
  
    if(layer._map.options.mapType === "schema"){
      schema_editedItems({"layers":{"_layers":{"0":layer}}});
    }
    else{
      gis_editedItems({"layers":{"_layers":{"0":layer}}});
    }
  
    sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.options, null, 2);
    sidebar._container.querySelector('#datapoints_field').value = JSON.stringify(layer._dataPoints, null, 2);
  }, layer);
}



/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// operate functions


function open_control(event,datapoint){
  let id = datapoint;

  let i = 0;
  let node = null;
  object = event.target;
  while(i < 20 && object){
    if(object['layerNode']){
      node = object['layerNode'];
      break;
    }
    object = object.parentNode;
    i++;
  }
  //let nod = this.template_item;
  let status_point = "";
  let control_element = "";
  for (const [key, point] of Object.entries(node._dataPoints)) {
    for (const [child_key, child_point] of Object.entries(point)) {
      if(child_point == datapoint){
        control_element = child_key;
      }
      if(child_point == event.target.id){
        status_point = child_key;
      }
    }
  }
  event.preventDefault();
  event.stopPropagation();

  show_Sidebar({target:node});
  sidebar._container.querySelector('#info_control').style.display = "block";
  sidebar._container.querySelector('#control_element').value = control_element;
  sidebar._container.querySelector('#control_value').value = local_data_cache[status_point];
  sidebar._container.querySelector('#info_items').innerHTML = "Name: " + event.target.parentNode.id + "<br>";


}

function select(element, value) {
  socket.emit('publish', {'operation': 'select', 'element': element, 'value': value});
}

function operate(element, value) {
  socket.emit('publish', {'operation': 'operate', 'element': element, 'value': value});
}

function cancel(element) {
  socket.emit('publish', {'operation': 'cancel', 'element': element, 'value': ""});
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//generic functions

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

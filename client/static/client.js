var socket;
var local_data_cache, local_data_cache_norefresh;
var sidebar, leafletmap, isEditEnabled,isGridEnabled, editableLayers, geojsonlayer;


$(document).ready(function() {
  local_data_cache = {};
  local_data_cache_norefresh = {};
  namespace = '';

  socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

  let focus = document.getElementById("focus").value
  if(focus === "1"){ // gis view
    init_gis();
    init_mapelements('gis');
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
    init_mapelements('schema');
  }

});



//////////////////////////////////////////////////////////////////////////////
//leaflet maps

function init_mapelements(type){
  geojsonlayer = L.geoJSON().addTo(leafletmap);

  //draw grid
  var GridOptions = {
		xticks: 55,
		yticks: 25,
		lineStyle: {
			stroke: false,
			color: 'white',
			opacity: 0.6,
			weight: 1
		},
	};
  var grid = L.grid(GridOptions).addTo(leafletmap);

  isGridEnabled = false;
  L.easyButton('fa-table-cells', function(){
    if(isGridEnabled == true){
      GridOptions.lineStyle.stroke = false;
      L.Util.setOptions(grid, GridOptions);
      grid.redraw();
      isGridEnabled = false;
      //console.log("off");
    }else{
      GridOptions.lineStyle.stroke = true;
      L.Util.setOptions(grid, GridOptions);
      grid.redraw();
      isGridEnabled = true;
      //console.log("on");
    }  
  }).addTo( leafletmap );


  //draw edit controls
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
      circle: true, 
      rectangle: true,
      marker: false, // Turns off this drawing tool 
      circlemarker: false
    },
    edit: {
      featureGroup: editableLayers, //REQUIRED!! 
      remove: true
    }
  };
  let drawControl = new L.Control.Draw(options);

  //set default sidebar to info, and hide edit
  isEditEnabled = false;
  document.getElementById("info_panel").style.display = "block";
  document.getElementById("edit_panel").style.display = "none";

  //toggle the sidebar of the edit/info with the edit-button
  L.easyButton('fa-pen-to-square', function(){
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

  //attach the sidebar for info/editing to leaflet
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

  //register edit callbacks
  leafletmap.on('draw:editstart',   function() { sidebar.hide(); sidebar.removeFrom(leafletmap); } );
  leafletmap.on('draw:editstop',    function() { sidebar.hide(); sidebar.addTo(leafletmap); } );
  leafletmap.on('draw:deletestart', function() { sidebar.hide(); sidebar.removeFrom(leafletmap); } );
  leafletmap.on('draw:deletestop',  function() { sidebar.hide(); sidebar.addTo(leafletmap); } );

  // Set up the hash
  var hash = new L.Hash(leafletmap);

  // END OF INIT VIEW CODE

  //event to draw all visible geojson objets to a gis or schema map(i.e not svg, but geojson object such as polygon or polyline)
  let socket_endpoint = 'geojson_object_add_to_map_' + type;
  socket.on(socket_endpoint, function (json) {
    //add geojson to object
    if (json) {
      //let local_geojsonlayer = L.geoJSON();
      // parse the json into leaflet layers
      //local_geojsonlayer.addData(json);
      let local_geojsonlayer = createLayersFromJson(json); //function that also adds circle

      //remove invisible layers
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
            //remove key for updating
            for (const [key, point] of Object.entries(editableLayers._layers[edititem]._dataPoints)) {
              for (const [child_key, child_point] of Object.entries(point)) {
                socket.emit('unregister_datapoint', child_key); //register all datapoints, so updates for these points are sent to the browser
              }
            }
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
          let layer = local_geojsonlayer._layers[local_geoitem];
          // add geojson objects to edit and geojson-layer
          layer.uuid = layer['feature']['_id'];//set uud, needed for deletion/editing
          layer.type = "Feature"; // ensure type is set to Feature(i.e not svg, but geojson object such as polygon or polyline)
          layer.on("click", show_Sidebar); //register event
          layer._dataPoints = layer['feature']["properties"]['datapoints'];//set the datapoints related for this object

          getGeojsonStyle(layer);// copy properties over to the geojsonstyle object, to apply them

          //finally add the layer to the maps
          editableLayers.addLayer(layer); //the layer used when editing
          geojsonlayer.addLayer(layer); // the normal view layer

          for (const [key, point] of Object.entries(layer._dataPoints)) {
            for (const [child_key, child_point] of Object.entries(point)) {
              socket.emit('register_datapoint', child_key); //register all datapoints, so updates for these points are sent to the browser
              local_data_cache_norefresh[child_key] = false;// this seems needed to prevent multiple updates??
            }
          }
        }
      }
    }
  });

  //receive data from scada, and update items to display it(svg or geojson)
  socket.on('updateDataPoint', function (data) { 
    //console.log("called:" + data.toString());
    let key = data['key'];
    let value = data['value'];

    //check if cached data is still accurate, and if an update is forced (norefresh=false)
    if(local_data_cache[key] == value && local_data_cache_norefresh[key] == true){
      return;
    }
    local_data_cache[key] = value;
    local_data_cache_norefresh[key] = true;
    //console.log("key:" + key.toString() + " value:" + value.toString());
    // update svg items and geojson
    try{
      updateLayers(editableLayers._layers, key, value);
    }catch (ex){
      console.log(ex);
    }
    
    updateEditDialog(key, value);
  });

}


function updateLayers(layers,key, value){
  for(let layer_id in layers){
    let layer = layers[layer_id]
    for (const [d_key, point] of Object.entries(layer._dataPoints)) {

      if (!(key in point)){ // check if the update value identifier(key) is part of the datapoints for this object
        continue; // if key is not this datapoint, try next
      }
      template_item = point[key]; // retrieve the element-id related to this datapoint, for updating

      // update the element id if object type is svg
      if(layer.type === "Svg"){
        //template_item is id of svg element. class is used for type of display
        $(layer._image).find("*").each(function(idx, el){
          if(el.id == template_item){ 
            let cl = el.classList.toString();
            //register  
            if(cl == "XCBR" || cl == "XSWI"){ 
              if(value == 1 && !('lastAnim' in el && el['lastAnim'] == 'close')) {
                $("#close",el)[0].beginElementAt(0.1); 
                el['lastAnim'] = 'close';
                //$("#close",el)[0].beginElement(); 
              }
              if(value != 1 && !('lastAnim' in el && el['lastAnim'] == 'open')) {
                $("#open",el)[0].beginElementAt(0.1);
                el['lastAnim'] = 'open';
                //$("#open",el)[0].beginElement();
              }
            }
            else if(cl == "MEAS"){ 
              if(el.dataset.size > 0 || typeof(el.dataset.text) === "undefined"){
                var desc = el.innerHTML;
                el.textContent = value;
              }
              else{
                var val = abbreviate_number(parseFloat(value),0)
                el.textContent = el.dataset.text.replace("{value}",val);
              }
            }
            else { //if no class defined, assume normal/fail state
              if(value > 1 && !('lastAnim' in el && el['lastAnim'] == 'normal')) {
                try{
                  $("#normal",el)[0].beginElementAt(0.1); 
                  el['lastAnim'] = 'normal';
                  $("#normal2",el)[0].beginElementAt(0.1); 
                  $("#normal3",el)[0].beginElementAt(0.1); 
                }
                catch(ex){
                  //fail silently
                }
              }
              if(( value <= 1 || value == 0 || value == "UNKNOWN") && !('lastAnim' in el && el['lastAnim'] == 'fail')) {
                try{
                  $("#fail",el)[0].beginElementAt(0.1);
                  el['lastAnim'] = 'fail';
                  $("#fail2",el)[0].beginElementAt(0.1);
                  $("#fail3",el)[0].beginElementAt(0.1);
                }
                catch(ex){
                  //fail silently
                }
              }
            }
          }
        });
      }

      // update the element id if object type is svg
      if(layer.type === "Feature"){
        //template_item is property modification of geojson element. class is used for type of display
        //template_item = {"datapoint":['<element-id>','<comparisson>','<value>',<value to assing to element-id>]} 
        // e.g. {"1":["color","gt","10","#00ff00"]}; ->  if(value > 10){color = '#00ff00';}
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
          layer.options[template_item[0]] = result; //assign the result if a comparisson was made succesfull
          layer.setStyle();//update the layer style
        }        
      }
    }
  }
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
//.leaflet-modal item for displaying the svg template window
// this window allows to select existing svg templates, or upload a new one

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
        
          //init event
          onShow: function(evt) {
            let modal = evt.modal;
            let imported = null;
            
            //fit the svg in the preview window
            fitSvg(templates[0]['svg'], modal._container.querySelector('#preview'));

            //register several Dom events
            L.DomEvent
            .on(modal._container.querySelector('.modal-ok'), 'click', function() { //pressed ok, so create a new svg object on the map
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
            .on(modal._container.querySelector('.modal-cancel'), 'click', function() { //dont create an svg object on the map
              modal.hide();
            })
            .on(modal._container.querySelector('select[name="SVG-templates"]'), 'change', function() {// select a different template from dropdown
              imported = null;
              fitSvg(templates[parseInt(this.value)]['svg'],  modal._container.querySelector('#preview'));
              modal._container.querySelector('#template_name').value = "";
            })
            .on(modal._container.querySelector('#file-input'), 'change', function(e) { // select svg from file
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

//calculate a fitting boundingbox around an svg, and set a preview window
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

//display of the info/edit sidebar
function show_Sidebar(e){
  let layer = e.target;
  sidebar._container.querySelector('#info_control').style.display = "none";
  sidebar._container.querySelector('#info_status').style.display = "none";
  sidebar._container.querySelector('#edit_panel_error-message').innerHTML = "";
  sidebar._container.querySelector('#edit_panel_error-message').style = "color:black";

  if(layer.type==="Feature"){
    sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.feature.properties, null, 2);
    layerPropertyName = "nameplate" in layer.feature.properties ? layer.feature.properties.nameplate : "?";
    layerPropertyDescription = "description" in layer.feature.properties ? layer.feature.properties.description : "";
  }
  else{ //svg
    sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.properties, null, 2);
    layerPropertyName = "nameplate" in layer.properties ? layer.properties.nameplate : "?";
    layerPropertyDescription = "description" in layer.properties ? layer.properties.description : "";
  }
  
  sidebar._container.querySelector('#info_items').innerHTML = "<b>Name:</b> " + layerPropertyName + "<br>";;
  sidebar._container.querySelector('#info_items').innerHTML += "<b>Description:</b> " + layerPropertyDescription + "<br>";;

  //set save button context
  let save_btn = sidebar._container.querySelector('#sidebar-save');
  let new_save_btn = save_btn.cloneNode(true);//deep clone of the save button, to ensure the layer passed is correct
  save_btn.parentNode.replaceChild(new_save_btn, save_btn);//replace the old button with this one

  L.DomEvent.on(new_save_btn, 'click', saveEditField, layer);

  sidebar.show();
}

function saveEditField(e)
{ 
  let layer = this;
  let error_msg = sidebar._container.querySelector('#edit_panel_error-message');
  //parse json, assign values to object and update
  if(layer.type==="Feature"){
    try{
      layer.feature.properties = JSON.parse(sidebar._container.querySelector('#options_field').value);
      //assign modified values
      layer._dataPoints = layer.feature.properties.datapoints;
      getGeojsonStyle(layer);

      sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.feature.properties, null, 2);

      error_msg.innerHTML = "Saved";
      error_msg.style = "color:green";
    } catch(err) {
      error_msg.innerHTML = err.message;
      error_msg.style = "color:red";
    }
  }
  else{
    try{
      layer.properties = JSON.parse(sidebar._container.querySelector('#options_field').value); 
      //assesing modified values
      layer._dataPoints = layer.properties.datapoints;

      sidebar._container.querySelector('#options_field').value = JSON.stringify(layer.properties, null, 2);

      error_msg.innerHTML = "Saved";
      error_msg.style = "color:green";
    } catch(err) {
      error_msg.innerHTML = err.message;
      error_msg.style = "color:red";
    }
  }
  //update database
  if(layer._map.options.mapType === "schema"){ //schema view
    schema_editedItems({"layers":{"_layers":{"0":layer}}});
  }
  else{ //gis view
    gis_editedItems({"layers":{"_layers":{"0":layer}}});
  }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// operate functions


function open_control(event,datapoint){
  //find the main layer-node for this object from its child-node
  //we need this to find the associated leaflet layer object, as what we click might be a (sub)child-object of the layer
  let i = 0;
  let layer = null;
  object = event.target;
  while(i < 20 && object){ //go to parent node, max 20 items deep
    if(object['layerNode']){
      layer = object['layerNode'];
      break;
    }
    object = object.parentNode;
    i++;
  }
  if(layer === null){
    return
  }
  //find the child-node that is related to the datapoint element-id
  let status_point = "";
  let control_element = "";
  let type = "undefined";
  let nameplate = "?";
  let description = "";

  if('properties' in layer){
    if('nameplate' in layer.properties){
      nameplate = layer.properties.nameplate;
    }
    if('description' in layer.properties){
      description = layer.properties.description;
    }
  }

  for (const [key, point] of Object.entries(layer._dataPoints)) {
    for (const [child_key, child_point] of Object.entries(point)) {
      if(child_point == datapoint){ //the control element (this is modified when operate is set)
        control_element = child_key;
        if('type' in point){ // if type is set, ajust control dialog for this type
          type = point.type;
        }
        if('nameplate' in point){ // if type is set, ajust control dialog for this type
          nameplate = point.nameplate;
        }
        if('description' in point){ // if type is set, ajust control dialog for this type
          description = point.description;
        }        
      }
      if(child_point == event.target.id){ // the status element (this is read, and updated after a control action)
        status_point = child_key;
      }
    }
  }
  if(!isEditEnabled){ //else delete click is not caught
    event.preventDefault();
    event.stopPropagation(); 
  }

  show_Sidebar({target:layer});
  sidebar._container.querySelector('#info_items').innerHTML = "<b>Name:</b> " + nameplate;
  sidebar._container.querySelector('#info_items').innerHTML += "<br>" + " <b>Description:</b> " +  description;

  sidebar._container.querySelector('#info_status').style.display = "block";
  sidebar._container.querySelector('#hidden_type').value = type;
  sidebar._container.querySelector('#status_element').value = status_point;
  sidebar._container.querySelector('#status_element').title = status_point;

  sidebar._container.querySelector('#info_control_bool').style.display = "none";
  sidebar._container.querySelector('#info_control_doublepos').style.display = "none";
  sidebar._container.querySelector('#info_control_int').style.display = "none";

  sidebar._container.querySelector('#info_control').style.display = "block";
  sidebar._container.querySelector('#control_element').value = control_element;
  sidebar._container.querySelector('#control_element').title = control_element;
  if(type == "bool_SBO"){
    //status = true/false
    //oper   = true/false (suggest inverse)
    sidebar._container.querySelector('#info_control_bool').style.display = "block";
    sidebar._container.querySelector('#info_control_bool_SBO').style.display = "block";
    sidebar._container.querySelector('#status_value').value = local_data_cache[status_point] == 1? "CLOSE" : "OPEN";
    sidebar._container.querySelector('#control_value_bool').value = local_data_cache[status_point]==1? 0:1;

  } else if(type == "doublepos_SBO"){
    //status = 01/10
    //oper   =  0/1 (suggest inverse)
    sidebar._container.querySelector('#info_control_doublepos').style.display = "block";
    sidebar._container.querySelector('#info_control_doublepos_SBO').style.display = "block";
    sidebar._container.querySelector('#status_value').value = local_data_cache[status_point] == 1? "CLOSE" : "OPEN";
    sidebar._container.querySelector('#control_value_doublepos').value = local_data_cache[status_point]==1? 2:1;

  } else if(type == "int_SBO"){
    //status is value
    //oper is value, +1, -1
    sidebar._container.querySelector('#info_control_int').style.display = "block";
    sidebar._container.querySelector('#info_control_int_SBO').style.display = "block";
    sidebar._container.querySelector('#status_value').value = local_data_cache[status_point];
    sidebar._container.querySelector('#control_value_int').value = local_data_cache[status_point];

  } else if(type == "bool_direct"){
    //status = true/false
    //oper   = true/false (suggest inverse)
    sidebar._container.querySelector('#info_control_bool').style.display = "block";
    sidebar._container.querySelector('#info_control_bool_SBO').style.display = "none";
    sidebar._container.querySelector('#status_value').value = local_data_cache[status_point] == 1? "CLOSE" : "OPEN";
    sidebar._container.querySelector('#control_value_bool').value = local_data_cache[status_point]==1? 0:1;

  } else if(type == "doublepos_direct"){
    //status = 01/10
    //oper   =  0/1 (suggest inverse)
    sidebar._container.querySelector('#info_control_doublepos').style.display = "block";
    sidebar._container.querySelector('#info_control_doublepos_SBO').style.display = "none";
    sidebar._container.querySelector('#status_value').value = local_data_cache[status_point] == 1? "CLOSE" : "OPEN";
    sidebar._container.querySelector('#control_value_doublepos').value = local_data_cache[status_point]==1? 2:1;

  } else if(type == "int_direct"){
    //status is value
    //oper is value, +1, -1
    sidebar._container.querySelector('#info_control_int').style.display = "block";
    sidebar._container.querySelector('#info_control_int_SBO').style.display = "none";
    sidebar._container.querySelector('#status_value').value = local_data_cache[status_point];
    sidebar._container.querySelector('#control_value_int').value = local_data_cache[status_point];

  } else {
    //simple info dialog
    sidebar._container.querySelector('#info_control').style.display = "none";
  } 
}

//the actual operate functions
function select(element, value) {
  socket.emit('publish', {'operation': 'select', 'element': element, 'value': value});
}

function operate(element, value) {
  socket.emit('publish', {'operation': 'operate', 'element': element, 'value': value});
}

function cancel(element) {
  socket.emit('publish', {'operation': 'cancel', 'element': element, 'value': ""});
}

function updateEditDialog(key, value) {
  if(key != sidebar._container.querySelector('#status_element').value){
    return;
  }
  let type = sidebar._container.querySelector('#hidden_type').value;
  if(type == "bool_SBO"){
    sidebar._container.querySelector('#status_value').value = value == 1? "CLOSE" : "OPEN";
  } else if(type == "doublepos_SBO"){
    sidebar._container.querySelector('#status_value').value = value == 1? "CLOSE" : "OPEN";
  } else if(type == "int_SBO"){
    sidebar._container.querySelector('#status_value').value = value;
  } else if(type == "bool_direct"){
    sidebar._container.querySelector('#status_value').value = value == 1? "CLOSE" : "OPEN";
  } else if(type == "doublepos_direct"){
    sidebar._container.querySelector('#status_value').value = value == 1? "CLOSE" : "OPEN";
  } else if(type == "int_direct"){
    sidebar._container.querySelector('#status_value').value = value;
  } else {
    sidebar._container.querySelector('#status_value').value = value;
  } 
}

function open_graph(element){
  //Admin_01
  //  http://127.0.0.1:3000/d/0qabI_pVz/test-dashboard?orgId=1&from=now-7d&to=now&var-dataprovider=static://local/DoublePointInformation/300&editPanel=4
  // &var-dataprovider=static://local/DoublePointInformation/300&kiosk
  // <iframe src="http://127.0.0.1:3000/d-solo/0qabI_pVz/test-dashboard?orgId=1&var-dataprovider=static%3A%2F%2Flocal%2FDoublePointInformation%2F300&from=1675411683672&to=1676016483673&panelId=4" width="450" height="200" frameborder="0"></iframe>
  // http://127.0.0.1:3000/d/0qabI_pVz/test-dashboard?orgId=1&from=1675412329996&to=1676017129996&viewPanel=4&var-dataprovider=static://local/DoublePointInformation/300&kiosk

  // http://127.0.0.1:3000/d/0qabI_pVz/test-dashboard?orgId=1&from=1675412329996&to=1676017129996&viewPanel=4&var-dataprovider=static://local/DoublePointInformation/300&kiosk=tv

  //alert(element.toString());
  //event.preventDefault();
  var url = "http://127.0.0.1:3000/d/0qabI_pVz/test-dashboard?orgId=1&viewPanel=4&var-dataprovider="+element+"&kiosk=tv";
  var x = 0;//window.outerWidth + window.screenX;
  var y = 0;//window.screenY;
  var h = 300; //window.outerHeight - 37;
  let params = 'width=500,height='+ h +',left='+ x +',top='+ y;
  window.open(url, 'test', params);
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//generic functions

//function to shorten a number to a fixed length, and include units such as kilo, mega, etc
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

function hideAllModalWindows () {
  var modalFader = document.querySelector(".modal-fader");
  var modalWindows = document.querySelectorAll(".modal-window");
  
  if(modalFader.className.indexOf("active") !== -1) {
      modalFader.className = modalFader.className.replace("active", "");
  }
  
  modalWindows.forEach(function (modalWindow) {
      if(modalWindow.className.indexOf("active") !== -1) {
          modalWindow.className = modalWindow.className.replace("active", "");
      }
  });
}



function createLayersFromJson(data) {
  const layers = L.geoJSON();

  data.forEach(function (geo, id) {
    L.geoJSON(geo, {
      pointToLayer: (feature, latlng) => {
        if (feature.properties.radius) {
          return new L.Circle(latlng, feature.properties.radius);
        } else {
          return new L.Marker(latlng);
        }
      },
      onEachFeature: (feature, layer) => {
        layer.addTo(layers);
      },
    });
  });
  
  return layers;
};
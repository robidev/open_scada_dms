/**
 * @class L.SvgObject
 * @aka SvgObject
 * @inherits L.SVGOverlay
 */
 L.SvgObject = L.SVGOverlay.extend({

	options:{
		svgViewBox:{
			viewBox: false, // viewbox can be "x y w h" to directly set viewBox attribute of svg, 'false' to use bounds instead, or "calculate" to derive from svg bbox
			fitBounds: false, // false means bounds are used directly, true means only center latlng of bounds are used, and actual bounds are fit to bbox of svg
			scaleBounds: 1.0 // scale the size of the svg bounds on the map
		},
	},

	initialize: function (svgString, bounds, uuid, options) {
		this.uuid = uuid;
		////
		this._dataPoints = {};
		this._templateName = "";
		this._newTemplate = false;
		////
		options = options || this.options;
		options.interactive = true;
		this._svgViewBox = null;

		let docObj = new DOMParser().parseFromString(svgString, "image/svg+xml").documentElement;

		//set viewbox specific (independent from bounds)
		if(options.svgViewBox && (typeof options.svgViewBox.viewBox === 'string' || options.svgViewBox.viewBox instanceof String)){
			if(options.svgViewBox.viewBox === "calculate"){
				document.body.appendChild(docObj);//svg needs to be visible
				let bbox = docObj.getBBox();
				document.body.removeChild(docObj);//remove it before anyone can see
				this._svgViewBox = (bbox.x).toString() + " " + (bbox.y).toString() + " " + (bbox.width).toString() + " " + (bbox.height).toString();
			}
			else { //set viewbox to bounds-width/height
				this._svgViewBox  = options.svgViewBox.viewBox;
			}
			//set bounds to viewbox
			let bbox_s = this._svgViewBox.split(" ");
			if(options.svgViewBox.fitBounds == true && bbox_s.length == 4){
				let latlng = L.latLng(0,0);
				latlng.lat = bounds._southWest.lat + (bounds._northEast.lat - bounds._southWest.lat)/2;
				latlng.lng = bounds._southWest.lng + (bounds._northEast.lng - bounds._southWest.lng)/2;

				//set scale of bounds
				let scale = 1.0;
				if(options.svgViewBox.scaleBounds){
					scale = options.svgViewBox.scaleBounds;
				}
				
				bounds = [[
					latlng.lat - ((bbox_s[3] / 2)*scale), 
					latlng.lng - ((bbox_s[2] / 2)*scale)
				], [latlng.lat + ((bbox_s[3] / 2)*scale), 
					latlng.lng + ((bbox_s[2] / 2)*scale)
				]];//size on map
			}
			options.svgViewBox.viewBox = this._svgViewBox;
		}
		// use bounds if no viewbox was set
		if(this._svgViewBox == null){ 
			this._svgViewBox = "0 0 " +  (bounds._northEast.lng - bounds._southWest.lng).toString() + " " + (bounds._northEast.lat - bounds._southWest.lat).toString();
		}
		// set the viewbox
		docObj.setAttribute('viewBox',this._svgViewBox );

		// call actual initializer of SVGOverlay
		L.SVGOverlay.prototype.initialize.call(this, docObj, bounds, options);

		// initialize latlng to center of bounds
		this._latlng = this.getLatLng();
	},

	fitBounds: function(){
		let latlng = this.getLatLng();
		let bbox = this._svgViewBox.split(" ");
		if(bbox.length != 4){
			return
		}
		this.setBounds([[latlng.lat - (bbox[3] / 2), latlng.lng - (bbox[2] / 2)], [latlng.lat + (bbox[3] / 2), latlng.lng + (bbox[2] / 2)]]);// size on map
	},

	// @method setLatLng(latLng: LatLng): this
	// Sets the position of a SvgObject to a new location.
	setLatLng: function (latlng) {
		let oldLatLng = this._latlng;
		let bounds = this.getBounds();
		this.setBounds([
			[
				latlng.lat - (bounds._northEast.lat - bounds._southWest.lat)/2,
				latlng.lng - (bounds._northEast.lng - bounds._southWest.lng)/2
			],
			[
				latlng.lat + (bounds._northEast.lat - bounds._southWest.lat)/2,
				latlng.lng + (bounds._northEast.lng - bounds._southWest.lng)/2
			]
		]);
		this._latlng = this.getLatLng();

		// @event move: Event
		// Fired when the SvgObject is moved, Old and new coordinates are included in event arguments as `oldLatLng`, `latlng`.
		return this.fire('move', {oldLatLng: oldLatLng, latlng: this._latlng});
	},

	// @method getLatLng(): LatLng
	// Returns the current geographical position of the SvgObject
	getLatLng: function () {
		let bounds = this.getBounds();
		let latlng = L.latLng(0,0);
		latlng.lat = bounds._southWest.lat + (bounds._northEast.lat - bounds._southWest.lat)/2;
		latlng.lng = bounds._southWest.lng + (bounds._northEast.lng - bounds._southWest.lng)/2;
		this._latlng = latlng;
		return this._latlng;
	},

	redraw: function () {

	}
});

//ensure draw exists
L.Draw = L.Draw || {};

L.drawLocal.draw.handlers.svg = {
	tooltip: {
		start: 'Add SVG.'
	},
};
L.drawLocal.draw.toolbar.buttons.svg = "Draw an svg";

/**
 * @class L.Draw.Svg
 * @aka Draw.Svg
 * @inherits L.Draw.SimpleShape
 */
 L.Draw.Svg = L.Draw.SimpleShape.extend({
	statics: {
		TYPE: 'svg'
	},

	options: {
		shapeOptions: {
			clickable: true
		},
	},

	// @method initialize(): void
	initialize: function (map, options) {
		// Save the type so super can fire, need to do this as cannot do this.TYPE :(
		this.type = L.Draw.Svg.TYPE;
		this._initialLabelText = L.drawLocal.draw.handlers.svg.tooltip.start;
		L.Draw.SimpleShape.prototype.initialize.call(this, map, options);

		//default settings to override before enable() is called
		this._template = '<rect width="100" height="100" />';//svg object template
		this._templateBounds = [[0,0],[100,100]];// size on map, in latlng. only center is used if bounds are calculated by fitBounds
		this._svgViewBox = false;// x y w h of svg viewBox attribute. value can be:"0 0 100 100", "calulated" or false
		this._svgFitBounds = false;// property to make the bounds fit the viewbox. value can be false or true;
		this._scale = 1.0;// scale of svg object on map
		this._newTemplate = false;
		this._templateName = "";
	},

	_fireCreatedEvent: function () {
		let mlat = (this._templateBounds[1][0] - this._templateBounds[0][0])/2
		let mlng = (this._templateBounds[1][1] - this._templateBounds[0][1])/2
		let svg = new L.SvgObject('<svg xmlns="http://www.w3.org/2000/svg">'+this._template+'</svg>', 
			L.latLngBounds([this._startLatLng.lat-mlat, this._startLatLng.lng-mlng], [this._startLatLng.lat+mlat, this._startLatLng.lng+mlng]),
			null, {svgViewBox: {viewBox: this._svgViewBox, fitBounds: this._svgFitBounds, scaleBounds: this._scale}});
			
		svg._newTemplate = this._newTemplate;
		svg._templateName = this._templateName;

		L.Draw.SimpleShape.prototype._fireCreatedEvent.call(this, svg);
	},

	_onMouseMove: function (e) {
		let latlng = e.latlng;

		this._tooltip.updatePosition(latlng);

		if (!this._shape) {
			let mlat = (this._templateBounds[1][0] - this._templateBounds[0][0])/2
			let mlng = (this._templateBounds[1][1] - this._templateBounds[0][1])/2
			this._shape = new L.SvgObject('<svg xmlns="http://www.w3.org/2000/svg">'+this._template+'</svg>', 
				L.latLngBounds([latlng.lat-mlat, latlng.lng-mlng], [latlng.lat+mlat, latlng.lng+mlng]), 
				null,  {svgViewBox: {viewBox: this._svgViewBox, fitBounds: this._svgFitBounds, scaleBounds: this._scale}});
			this._map.addLayer(this._shape);
		}
		else {
			this._shape.setLatLng(latlng);
		}

		let subtext = '';
		this._tooltip.updateContent({
			text: this._endLabelText,
			subtext: subtext
		});
	},
});


//ensure edit exists
L.Edit = L.Edit || {};
/**
 * @class L.Edit.CircleMarker
 * @aka Edit.Circle
 * @inherits L.Edit.SimpleShape
 */
L.Edit.Svg = L.Edit.SimpleShape.extend({

	addHooks: function () {
		L.Edit.SimpleShape.prototype.addHooks.call(this);
		let icon = this._shape._image;
		icon.style.display = 'none';
		L.DomUtil.addClass(icon, 'leaflet-edit-svg-selected');
		icon.style.display = '';
	},

	removeHooks: function () {
		let icon = this._shape._image;
		icon.style.display = 'none';
		L.DomUtil.removeClass(icon, 'leaflet-edit-svg-selected');
		icon.style.display = '';
		L.Edit.SimpleShape.prototype.removeHooks.call(this);
	},

	_createMoveMarker: function () {
		let center = this._shape.getLatLng();
		this._moveMarker = this._createMarker(center, this.options.moveIcon);
	},

	_move: function (latlng) {
		//EDIT
		/*if (this._resizeMarkers.length) {
			let resizemarkerPoint = this._getResizeMarkerPoint(latlng);
			// Move the resize marker
			this._resizeMarkers[0].setLatLng(resizemarkerPoint);
		}*/

		// Move the svg
		this._shape.setLatLng(latlng);

		// EDIT Reposition the resize markers
		this._repositionCornerMarkers();

		this._map.fire(L.Draw.Event.EDITMOVE, {layer: this._shape});
	},

	/*_createResizeMarker: function () {
		// To avoid an undefined check in L.Edit.SimpleShape.removeHooks
		this._resizeMarkers = [];
	},*/
	///////////////////////////////////////////////////////////////////////////////////////////////
	_createResizeMarker: function () {
		var corners = this._getCorners();

		this._resizeMarkers = [];

		for (var i = 0, l = corners.length; i < l; i++) {
			this._resizeMarkers.push(this._createMarker(corners[i], this.options.resizeIcon));
			// Monkey in the corner index as we will need to know this for dragging
			this._resizeMarkers[i]._cornerIndex = i;
		}
	},

	_onMarkerDragStart: function (e) {
		L.Edit.SimpleShape.prototype._onMarkerDragStart.call(this, e);

		// Save a reference to the opposite point
		var corners = this._getCorners(),
			marker = e.target,
			currentCornerIndex = marker._cornerIndex;

		this._oppositeCorner = corners[(currentCornerIndex + 2) % 4];

		this._toggleCornerMarkers(0, currentCornerIndex);
	},

	_onMarkerDragEnd: function (e) {
		var marker = e.target,
			bounds, center;

		// Reset move marker position to the center
		if (marker === this._moveMarker) {
			bounds = this._shape.getBounds();
			center = bounds.getCenter();

			marker.setLatLng(center);
		}

		this._toggleCornerMarkers(1);

		this._repositionCornerMarkers();

		L.Edit.SimpleShape.prototype._onMarkerDragEnd.call(this, e);
	},

	_resize: function (latlng) {
		var bounds;

		// Update the shape based on the current position of this corner and the opposite point
		this._shape.setBounds(L.latLngBounds(latlng, this._oppositeCorner));

		// Reposition the move marker
		bounds = this._shape.getBounds();
		this._moveMarker.setLatLng(bounds.getCenter());

		this._map.fire(L.Draw.Event.EDITRESIZE, {layer: this._shape});
	},

	_getCorners: function () {
		var bounds = this._shape.getBounds(),
			nw = bounds.getNorthWest(),
			ne = bounds.getNorthEast(),
			se = bounds.getSouthEast(),
			sw = bounds.getSouthWest();

		return [nw, ne, se, sw];
	},

	_toggleCornerMarkers: function (opacity) {
		for (var i = 0, l = this._resizeMarkers.length; i < l; i++) {
			this._resizeMarkers[i].setOpacity(opacity);
		}
	},

	_repositionCornerMarkers: function () {
		var corners = this._getCorners();

		for (var i = 0, l = this._resizeMarkers.length; i < l; i++) {
			this._resizeMarkers[i].setLatLng(corners[i]);
		}
	}
});

//add Edit.Svg to SvgObject, so that it can be edited
L.SvgObject.addInitHook(function () {
	if (L.Edit.Svg) {
		this.editing = new L.Edit.Svg(this);

		if (this.options.editable) {
			this.editing.enable();
		}
	}
});


/** overrides
 * @class L.DrawToolbar
 * @aka Toolbar
 */
 L.DrawToolbar.include({

	options: {
		polyline: {},
		polygon: {},
		rectangle: {},
		circle: {},
		marker: {},
		circlemarker: {},
		svg: {}
	},
	// @method getModeHandlers(): object
	// Get mode handlers information
	getModeHandlers: function (map) {
		return [
			{
				enabled: this.options.polyline,
				handler: new L.Draw.Polyline(map, this.options.polyline),
				title: L.drawLocal.draw.toolbar.buttons.polyline
			},
			{
				enabled: this.options.polygon,
				handler: new L.Draw.Polygon(map, this.options.polygon),
				title: L.drawLocal.draw.toolbar.buttons.polygon
			},
			{
				enabled: this.options.rectangle,
				handler: new L.Draw.Rectangle(map, this.options.rectangle),
				title: L.drawLocal.draw.toolbar.buttons.rectangle
			},
			{
				enabled: this.options.circle,
				handler: new L.Draw.Circle(map, this.options.circle),
				title: L.drawLocal.draw.toolbar.buttons.circle
			},
			{
				enabled: this.options.marker,
				handler: new L.Draw.Marker(map, this.options.marker),
				title: L.drawLocal.draw.toolbar.buttons.marker
			},
			{
				enabled: this.options.circlemarker,
				handler: new L.Draw.CircleMarker(map, this.options.circlemarker),
				title: L.drawLocal.draw.toolbar.buttons.circlemarker
			},
			{
				enabled: this.options.svg,
				handler: new L.Draw.Svg(map, this.options.svg),
				title: L.drawLocal.draw.toolbar.buttons.svg
			}
		];
	},
});



/**
 * @class L.EditToolbar.Edit
 * @aka EditToolbar.Edit
 */
 L.EditToolbar.Edit.include({

	_backupLayer: function (layer) {
		let id = L.Util.stamp(layer);

		if (!this._uneditedLayerProps[id]) {
			// Polyline, Polygon or Rectangle
			if (layer instanceof L.Polyline || layer instanceof L.Polygon || layer instanceof L.Rectangle) {
				this._uneditedLayerProps[id] = {
					latlngs: L.LatLngUtil.cloneLatLngs(layer.getLatLngs())
				};
			} else if (layer instanceof L.Circle) {
				this._uneditedLayerProps[id] = {
					latlng: L.LatLngUtil.cloneLatLng(layer.getLatLng()),
					radius: layer.getRadius()
				};
			} else if (layer instanceof L.Marker || layer instanceof L.CircleMarker) { // Marker
				this._uneditedLayerProps[id] = {
					latlng: L.LatLngUtil.cloneLatLng(layer.getLatLng())
				};
			} else if(layer instanceof L.SvgObject ){
				this._uneditedLayerProps[id] = {
					bounds: layer.getBounds()
				};
			}
		}
	},

	_revertLayer: function (layer) {
		let id = L.Util.stamp(layer);
		layer.edited = false;
		if (this._uneditedLayerProps.hasOwnProperty(id)) {
			// Polyline, Polygon or Rectangle
			if (layer instanceof L.Polyline || layer instanceof L.Polygon || layer instanceof L.Rectangle) {
				layer.setLatLngs(this._uneditedLayerProps[id].latlngs);
			} else if (layer instanceof L.Circle) {
				layer.setLatLng(this._uneditedLayerProps[id].latlng);
				layer.setRadius(this._uneditedLayerProps[id].radius);
			} else if (layer instanceof L.Marker || layer instanceof L.CircleMarker) { // Marker or CircleMarker
				layer.setLatLng(this._uneditedLayerProps[id].latlng);
			} else if(layer instanceof L.SVGOverlay ) {
				layer.setBounds(this._uneditedLayerProps[id].bounds);
			}

			layer.fire('revert-edited', {layer: layer});
		}
	},
});



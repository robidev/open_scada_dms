/**
 * @class L.SvgObject
 * @aka SvgObject
 * @inherits L.SVGOverlay
 */
 L.SvgObject = L.SVGOverlay.extend({

	initialize: function (svgString, bounds, uuid, options) {
		this.uuid = uuid;
		options = options || {};
		options.interactive = true;

		var docObj = new DOMParser().parseFromString(svgString, "image/svg+xml").documentElement;
		docObj.setAttribute('viewBox', 
			"0 0 " + 
			(bounds._northEast.lng - bounds._southWest.lng).toString() + 
			" " + 
			(bounds._northEast.lat - bounds._southWest.lat).toString() );

		L.SVGOverlay.prototype.initialize.call(this, docObj, bounds, options);
		this._latlng = this.getLatLng();
	},

	// @method setLatLng(latLng: LatLng): this
	// Sets the position of a SvgObject to a new location.
	setLatLng: function (latlng) {
		var oldLatLng = this._latlng;
		var bounds = this.getBounds();
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
		var bounds = this.getBounds();
		var latlng = L.latLng(0,0);
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
		this._template = '<rect width="100" height="100" />';
		this._templateBounds = [[0,0],[100,100]];
	},

	_fireCreatedEvent: function () {
		var mlat = (this._templateBounds[1][0] - this._templateBounds[0][0])/2
		var mlng = (this._templateBounds[1][1] - this._templateBounds[0][1])/2
		var svg = new L.SvgObject('<svg xmlns="http://www.w3.org/2000/svg">'+this._template+'</svg>', 
			L.latLngBounds([this._startLatLng.lat-mlat, this._startLatLng.lng-mlng], [this._startLatLng.lat+mlat, this._startLatLng.lng+mlng]),
			null);
		//svg.editing = new L.Edit.Svg(svg);
		L.Draw.SimpleShape.prototype._fireCreatedEvent.call(this, svg);
	},

	_onMouseMove: function (e) {
		var latlng = e.latlng;

		this._tooltip.updatePosition(latlng);

		if (!this._shape) {
			var mlat = (this._templateBounds[1][0] - this._templateBounds[0][0])/2
			var mlng = (this._templateBounds[1][1] - this._templateBounds[0][1])/2
			this._shape = new L.SvgObject('<svg xmlns="http://www.w3.org/2000/svg">'+this._template+'</svg>', 
				L.latLngBounds([latlng.lat-mlat, latlng.lng-mlng], [latlng.lat+mlat, latlng.lng+mlng]), 
				null);
			this._map.addLayer(this._shape);
		}
		else {
			this._shape.setLatLng(latlng);
		}

		var subtext = '';
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
		var icon = this._shape._image;
		icon.style.display = 'none';
		L.DomUtil.addClass(icon, 'leaflet-edit-svg-selected');
		icon.style.display = '';
	},

	removeHooks: function () {
		var icon = this._shape._image;
		icon.style.display = 'none';
		L.DomUtil.removeClass(icon, 'leaflet-edit-svg-selected');
		icon.style.display = '';
		L.Edit.SimpleShape.prototype.removeHooks.call(this);
	},

	_createMoveMarker: function () {
		var center = this._shape.getLatLng();
		this._moveMarker = this._createMarker(center, this.options.moveIcon);
	},

	_createResizeMarker: function () {
		// To avoid an undefined check in L.Edit.SimpleShape.removeHooks
		this._resizeMarkers = [];
	},

	_move: function (latlng) {
		if (this._resizeMarkers.length) {
			var resizemarkerPoint = this._getResizeMarkerPoint(latlng);
			// Move the resize marker
			this._resizeMarkers[0].setLatLng(resizemarkerPoint);
		}

		// Move the svg
		this._shape.setLatLng(latlng);
		this._map.fire(L.Draw.Event.EDITMOVE, {layer: this._shape});
	},
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

	drawDialog: function(){
		
	}
	
});



/**
 * @class L.EditToolbar.Edit
 * @aka EditToolbar.Edit
 */
 L.EditToolbar.Edit.include({

	_backupLayer: function (layer) {
		var id = L.Util.stamp(layer);

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
		var id = L.Util.stamp(layer);
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



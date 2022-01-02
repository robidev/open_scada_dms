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


	//svg_obj(0, 0, 100, 100, '<svg xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" /></svg>', "_12345");
	svg_obj: function (x, y, x2, y2, svgString) {
		var obj = new DOMParser().parseFromString(svgString, "image/svg+xml").documentElement;
		obj.setAttribute('viewBox', "0 0 " + (x2-x).toString() + " " + (y2-y).toString() );
		var svg = L.svgOverlay(obj, [ [ y,x], [ y2,x2 ] ], {'interactive': true });//.addTo(this._map);
		svg.getLatLng = function(){
			var bounds = this.getBounds();
			var center = L.latLng(0,0);
			center.lat = bounds._southWest.lat + (bounds._northEast.lat - bounds._southWest.lat)/2;
			center.lng = bounds._southWest.lng + (bounds._northEast.lng - bounds._southWest.lng)/2;
			return center;
		}
		svg.setLatLng = function(latlng){
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
		}
		svg.redraw = function(){

		}
		return svg;
	},
	// @method initialize(): void
	initialize: function (map, options) {
		// Save the type so super can fire, need to do this as cannot do this.TYPE :(
		this.type = L.Draw.Svg.TYPE;

		this._initialLabelText = L.drawLocal.draw.handlers.svg.tooltip.start;

		L.Draw.SimpleShape.prototype.initialize.call(this, map, options);
	},


	_fireCreatedEvent: function () {
		var svg = this.svg_obj(this._startLatLng.lng-50, this._startLatLng.lat-50, this._startLatLng.lng+50, this._startLatLng.lat+50, '<svg xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" /></svg>');
		svg.editing = new L.Edit.Svg(svg);
		L.Draw.SimpleShape.prototype._fireCreatedEvent.call(this, svg);
	},

	_onMouseMove: function (e) {
		var latlng = e.latlng;

		this._tooltip.updatePosition(latlng);

		if (!this._shape) {
			this._shape = this.svg_obj(latlng.lng-50, latlng.lat-50, latlng.lng+50, latlng.lat+50, '<svg xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" /></svg>');
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
	}
});


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
			} else if(layer instanceof L.SVGOverlay ){
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
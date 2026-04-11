/*
 * L.Grid displays a grid of lat/lng lines on the map.
 */

L.Grid = L.LayerGroup.extend({
	options: {
		xticks: 100,
		yticks: 100,
		// Path style for the grid lines
		lineStyle: {
			stroke: true,
			color: '#111',
			opacity: 0.6,
			weight: 1
		},
		// Redraw on move or moveend
		redraw: 'move'
	},

	initialize: function (options) {
		L.LayerGroup.prototype.initialize.call(this);
		L.Util.setOptions(this, options);

	},

	onAdd: function (map) {
		this._map = map;

		var grid = this.redraw();
		this._map.on('viewreset '+ this.options.redraw, function () {
			grid.redraw();
		});

		this.eachLayer(map.addLayer, map);
	},
	
	onRemove: function (map) {
		// remove layer listeners and elements
		map.off('viewreset '+ this.options.redraw, this.map);
		this.eachLayer(this.removeLayer, this);
	},

	redraw: function () {
		// pad the bounds to make sure we draw the lines a little longer
		this._bounds = this._map.getBounds().pad(0.5);

		var grid = [];
		var i;

		var latLines = this._latLines();
		for (i in latLines) {
			grid.push(this._horizontalLine(latLines[i]));
		}

		var lngLines = this._lngLines();
		for (i in lngLines) {
			grid.push(this._verticalLine(lngLines[i]));
		}

		this.eachLayer(this.removeLayer, this);
		for (i in grid) {
			this.addLayer(grid[i]);
		}
		return this;
	},

	_latLines: function () {
		return this._lines(
			this._bounds.getSouth(),
			this._bounds.getNorth(),
			this.options.yticks
		);
	},
	_lngLines: function () {
		return this._lines(
			this._bounds.getWest(),
			this._bounds.getEast(),
			this.options.xticks
		);
	},

	_lines: function (low, high, ticks) {
		var zoom = this._map.getZoom();
		// change scale only every 4 zoom levels
		var effectiveZoom = Math.floor(zoom / 4) * 4;
		var zoomscale = this._map.getZoomScale(effectiveZoom, 0);
		var delta = -4096 / zoomscale;
		var tick = delta / ticks;
		var oo = low % tick;
		low -= oo;

		var lines = [];
		for (var i = -1; (low - (i * tick)) <= high; i++) {
			lines.push(low - (i * tick));
		}
		return lines;
	},

	_verticalLine: function (lng) {
		return new L.Polyline([
			[this._bounds.getNorth(), lng],
			[this._bounds.getSouth(), lng]
		], this.options.lineStyle);
	},
	_horizontalLine: function (lat) {
		return new L.Polyline([
			[lat, this._bounds.getWest()],
			[lat, this._bounds.getEast()]
		], this.options.lineStyle);
	}

});

L.grid = function (options) {
	return new L.Grid(options);
};

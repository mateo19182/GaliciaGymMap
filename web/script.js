// script.js

var map = L.map("map").setView([42.5751, -7.6498], 8); // Set the initial coordinates and zoom level
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

var geojsonFiles = [
  "http://127.0.0.1:5500/coruna.geojson",
  "http://127.0.0.1:5500/lugo.geojson",
  "http://127.0.0.1:5500/ourense.geojson",
  "http://127.0.0.1:5500/pontevedra.geojson"
];
var markersGroup = L.layerGroup().addTo(map);
var geoJSONLayers = {};

function createGeoJSONLayer(data, name, markerColor) {
    fetch(data)
    .then(response => response.json())
    .then(geojson => {
        const geoJSONLayer = L.geoJSON(geojson, {
            pointToLayer: function (feature, latlng) {
                const marker = L.marker(latlng, { color: markerColor });
                const featureName = feature.properties.name; // Get the name from feature properties
                console.log(featureName);
                marker.bindPopup(featureName); // Bind popup with the correct name
                return marker;
            }
        });

        const layerControl = L.control.layers(null, null, { collapsed: false });
        geoJSONLayer.addTo(map);
        layerControl.addOverlay(geoJSONLayer, name);
        layerControl.addTo(map);
    })
    .catch(error => console.error('Error fetching GeoJSON:', error));
}



geojsonFiles.forEach((file, index) => {
    var colors = ["red", "blue", "green", "orange"];
    var layers = ["Coruña", "Lugo", "Ourense", "Pontevedra"];
    createGeoJSONLayer(file, layers[index], colors[index]);
});

// script.js

// Initialize the map
var map = L.map('map').setView([42.5751, -7.6498], 8); // Set the initial coordinates and zoom level

// Add a tile layer with OpenStreetMap data
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Create an object to store province layers
var provinceLayers = {};

// Function to add markers for a specific province
function addMarkersForProvince(province, markerData) {
    var markers = [];

    // Create markers for each location in the province
    markerData.forEach(function (location) {
        var marker = L.marker([location.latitude, location.longitude]).bindPopup(location.name);
        markers.push(marker);
    });

    // Create a layer group for the province and add markers to it
    provinceLayers[province] = L.layerGroup(markers);
}

// Example data for provinces and markers
var provinceData = {
    'A Coruña': [
        { name: 'Coruña Location 1', latitude: 43.3623, longitude: -8.4115 },
        // Add more locations as needed
    ],
    'Lugo': [
        { name: 'Lugo Location 1', latitude: 43.0129, longitude: -7.5559 },
        // Add more locations as needed
    ],
    // Add more provinces with respective locations
};

// Loop through province data and add markers and layers
for (var province in provinceData) {
    addMarkersForProvince(province, provinceData[province]);
}

// Add a layer control to toggle province visibility
L.control.layers(null, provinceLayers).addTo(map);
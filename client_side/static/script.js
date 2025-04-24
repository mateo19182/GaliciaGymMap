document.addEventListener('DOMContentLoaded', () => {
    const csvFilePath = '/static/updated_categories.csv'; // Relative path from index.html
    let allData = [];
    let map;
    let markers = L.markerClusterGroup();
    let initialUniqueValues = {}; // To store the full set of unique values for each filter

    const filters = {
        nombre: document.getElementById('nombreFilter'),
        sector: document.getElementById('sectorFilter'),
        tipo_instalacion: document.getElementById('tipoInstalacionFilter'),
        subtipo_instalacion: document.getElementById('subtipoInstalacionFilter'),
        area_actividad: document.getElementById('areaActividadFilter'),
        provincia: document.getElementById('provinciaFilter'),
        comarca: document.getElementById('comarcaFilter'),
        municipio: document.getElementById('municipioFilter'),
    };
    const resultsTableBody = document.getElementById('resultsBody');
    const resultsCount = document.getElementById('resultsCount');
    const mapContainer = document.getElementById('map');
    const clearFiltersButton = document.getElementById('clearFiltersBtn');
    const toggleMapCheckbox = document.getElementById('toggleMap');

    // Initialize the map
    const initialCenter = [42.5751, -7.8379]; // Galicia Center
    const initialZoom = 8;
    map = L.map('map').setView(initialCenter, initialZoom);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    map.addLayer(markers); // Add the cluster group layer to the map

    // Fetch and parse CSV data
    Papa.parse(csvFilePath, {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: (results) => {
            allData = results.data.map(row => {
                // Clean up data - replace empty strings/nulls with 'None' for consistency
                // Trim whitespace from string values
                for (const key in row) {
                    if (typeof row[key] === 'string') {
                        row[key] = row[key].trim();
                    } 
                    if (row[key] === null || row[key] === undefined || row[key] === '') {
                        row[key] = 'None'; // Use 'None' for internal consistency, display 'N/A' or similar
                    } 
                    // Convert numeric fields if necessary (example)
                    if (key === 'latitude' || key === 'longitude') {
                        row[key] = parseFloat(row[key]) || null; // Use null if conversion fails
                    } 
                }
                return row;
            });
            console.log("Datos cargados e procesados:", allData.length, "filas"); // Translated log
            populateFilters(); // Populate filters initially with all options
            applyFilters(); // Apply filters initially (display all data and set initial filter states)

            // Add event listener for Clear Filters button
            clearFiltersButton.addEventListener('click', clearAllFilters);

            // Add event listener for Map Toggle checkbox
            toggleMapCheckbox.addEventListener('change', toggleMapVisibility);

            // Initial map visibility check
            toggleMapVisibility(); // Set initial state based on checkbox
        },
        error: (error) => {
            console.error("Erro ao cargar ou analizar o CSV:", error); // Translated error
            resultsTableBody.innerHTML = '<tr><td colspan="10">Erro ao cargar os datos.</td></tr>'; // Translated error message
            resultsCount.textContent = 'Erro ao cargar os datos.'; // Translated error message
        }
    });

    // Function to populate filter dropdowns initially
    function populateFilters() {
        const uniqueValues = {
            sector: new Set(),
            tipo_instalacion: new Set(),
            subtipo_instalacion: new Set(),
            area_actividad: new Set(),
            provincia: new Set(),
            comarca: new Set(),
            municipio: new Set(),
        };

        allData.forEach(row => {
            Object.keys(uniqueValues).forEach(key => {
                 if (row[key] && row[key] !== 'None') { // Check for valid string before adding
                    uniqueValues[key].add(row[key]);
                }
            });
        });

        // Store the initial full set of unique values
        Object.keys(uniqueValues).forEach(key => {
            initialUniqueValues[key] = Array.from(uniqueValues[key]).sort((a, b) => a.localeCompare(b, 'gl'));
        });

        // Populate dropdowns
        Object.keys(filters).forEach(key => {
            if (filters[key] && filters[key].tagName === 'SELECT') {
                const select = filters[key];
                // Clear existing options except the first one ("All" / "Todos")
                let defaultOptionText = "Todos"; // Default translation
                if (key === 'area_actividad' || key === 'provincia' || key === 'comarca') {
                    defaultOptionText = "Todas"; // Use feminine form where appropriate
                }
                select.innerHTML = `<option value="">${defaultOptionText}</option>`;
                // Use the stored initial unique values for initial population
                initialUniqueValues[key].forEach(value => {
                    const option = document.createElement('option');
                    option.value = value;
                    option.textContent = value;
                    select.appendChild(option);
                });
            }
        });

        // Add event listeners *after* populating
        Object.values(filters).forEach(filterElement => {
            if (filterElement.tagName === 'SELECT' || filterElement.id === 'nombreFilter') {
                const eventType = filterElement.id === 'nombreFilter' ? 'input' : 'change';
                filterElement.addEventListener(eventType, applyFilters);
            }
        });
    }

    // Function to apply filters and update UI
    function applyFilters() {
        const activeFilters = {};
        Object.keys(filters).forEach(key => {
            if (filters[key]) {
                 activeFilters[key] = filters[key].value;
            }
        });

        console.log("Aplicando filtros:", activeFilters);

        const filteredData = allData.filter(row => {
            return Object.keys(activeFilters).every(key => {
                const filterValue = activeFilters[key];
                if (!filterValue || filterValue === "") return true; // No filter applied for this key

                const rowValue = row[key] ? row[key].toString() : ''; // Handle potential null/undefined

                if (key === 'nombre') {
                    return rowValue.toLowerCase().includes(filterValue.toLowerCase());
                } else {
                    return rowValue === filterValue;
                }
            });
        });

        updateFilterOptions(filteredData); // Update dropdown options based on filtered results
        displayResults(filteredData); // Display the filtered results on table and map
    }

    // Function to update the enabled/disabled state of filter options
    function updateFilterOptions(filteredData) {
        const currentUniqueValues = {
            sector: new Set(),
            tipo_instalacion: new Set(),
            subtipo_instalacion: new Set(),
            area_actividad: new Set(),
            provincia: new Set(),
            comarca: new Set(),
            municipio: new Set(),
        };

        // Calculate unique values available in the *currently filtered* data
        filteredData.forEach(row => {
            Object.keys(currentUniqueValues).forEach(key => {
                if (row[key] && row[key] !== 'None') {
                    currentUniqueValues[key].add(row[key]);
                }
            });
        });

        // Update each dropdown
        Object.keys(filters).forEach(key => {
            if (filters[key] && filters[key].tagName === 'SELECT') {
                const select = filters[key];
                const currentSelectedValue = select.value;

                // Iterate over options (skip the first 'All'/'Todos' option)
                for (let i = 1; i < select.options.length; i++) {
                    const option = select.options[i];
                    const hasResults = currentUniqueValues[key].has(option.value);
                    
                    // Disable if the option value isn't present in the filtered data,
                    // UNLESS it's the currently selected value.
                    option.disabled = !hasResults && option.value !== currentSelectedValue;
                    option.classList.toggle('disabled-option', option.disabled);
                }
            }
        });
    }

    // Function to clear all filters
    function clearAllFilters() {
        console.log("Clearing all filters");
        // Reset input field
        filters.nombre.value = '';
        // Reset select dropdowns
        Object.keys(filters).forEach(key => {
            if (filters[key] && filters[key].tagName === 'SELECT') {
                filters[key].value = ''; // Set to default 'All'/'Todos' option
            }
        });
        // Re-apply filters to show all data and reset dropdown states
        applyFilters(); 
    }

    // Function to toggle map visibility
    function toggleMapVisibility() {
        const isChecked = toggleMapCheckbox.checked;
        if (isChecked) {
            mapContainer.classList.remove('hidden');
            // Invalidate map size after showing it to ensure correct rendering
            if (map) {
                 // Delay slightly to ensure the container is visible before invalidating
                 setTimeout(() => map.invalidateSize(), 100);
            }
        } else {
            mapContainer.classList.add('hidden');
        }
        console.log(`Map visibility toggled: ${isChecked ? 'shown' : 'hidden'}`);
    }

    // Function to display results in the table and on the map
    function displayResults(data) {
        resultsTableBody.innerHTML = ''; // Clear previous table results
        markers.clearLayers(); // Clear previous map markers from the cluster group
        resultsCount.textContent = `${data.length} resultados atopados`; // Translated count

        if (data.length === 0) {
            resultsTableBody.innerHTML = '<tr><td colspan="10">Non se atoparon resultados cos criterios seleccionados.</td></tr>'; // Translated message
            map.setView(initialCenter, initialZoom); // Reset map view if no results
            return;
        }

        const markerCoords = []; // Array to hold coordinates for bounds calculation

        data.forEach(row => {
            // Add row to table
            const tr = document.createElement('tr');
            const displayKeys = ['nombre', 'municipio', 'provincia', 'sector', 'tipo_instalacion', 'subtipo_instalacion', 'area_actividad', 'telefono', 'web_link', 'maps_link'];
            displayKeys.forEach(key => {
                const td = document.createElement('td');
                let content = (row[key] && row[key] !== 'None') ? row[key] : 'N/D'; // Use 'N/D' (Non Dispoñible) for missing data in display

                // Make links clickable
                if ((key === 'web_link' || key === 'maps_link') && content !== 'N/D') {
                    // Basic check if it looks like a URL
                    if (typeof content === 'string' && (content.startsWith('http://') || content.startsWith('https://'))) {
                        td.innerHTML = `<a href="${content}" target="_blank">Ligazón</a>`; // Translated link text
                    } else {
                        td.textContent = 'URL non válida'; // Translated invalid URL
                    }
                } else {
                    td.textContent = content;
                }
                tr.appendChild(td);
            });
            resultsTableBody.appendChild(tr);

            // Add marker to map if coordinates exist
            if (row.latitude && row.longitude && !isNaN(row.latitude) && !isNaN(row.longitude)) {
                const lat = parseFloat(row.latitude);
                const lon = parseFloat(row.longitude);
                const marker = L.marker([lat, lon]);
                markerCoords.push([lat, lon]); // Add coordinates to array for bounds

                // Create popup content
                let popupContent = `<b>${row.nombre || 'Nome non dispoñible'}</b><br>`; // Translated label
                popupContent += `${row.municipio || 'Concello non dispoñible'}`; // Translated label
                if (row.direccion && row.direccion !== 'None') {
                     popupContent += `<br>${row.direccion}`; // Add address if available
                }

                marker.bindPopup(popupContent);
                markers.addLayer(marker); // Add marker to the cluster group
            }
        });

        // Fit map bounds to the displayed markers
        if (markerCoords.length > 0) {
            const bounds = L.latLngBounds(markerCoords);
            map.fitBounds(bounds, { padding: [50, 50] }); // Add padding so markers aren't on the edge
        } else {
            // Optional: Keep the current view or reset if preferred
            // map.setView(initialCenter, initialZoom); // Uncomment to reset if no markers have coordinates
        }
    }

});

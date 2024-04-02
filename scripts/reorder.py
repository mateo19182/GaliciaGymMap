import csv

# Define the order of columns you want in the output file
desired_order = [
    'id', 'nombre', 'municipio', 'comarca', 'provincia', 'direccion', 'codigo_postal', 
    'sector', 'tipo_instalacion', 'subtipo_instalacion', 'area_actividad', 'telefono', 
    'web_link', 'latitude', 'longitude', 'descripcion', 'maps_link', 'place_id', 
    'otro1', 'otro2', 'otro3'
]

# Open the input CSV file
with open('/home/mateo/GaliciaGymMap/search_demo/static/output2.csv', newline='', encoding='utf-8') as infile:
    # Create a csv reader object
    reader = csv.DictReader(infile)
    
    # Open the output CSV file
    with open('output3.csv', 'w', newline='', encoding='utf-8') as outfile:
        # Create a csv writer object with the desired header order
        writer = csv.DictWriter(outfile, fieldnames=desired_order)
        
        # Write the header to the output file
        writer.writeheader()
        
        # Reorder each row according to the desired order and write to the output file
        for row in reader:
            # Using dict comprehension to filter out any missing keys to avoid KeyError
            reordered_row = {key: row.get(key, '') for key in desired_order}
            writer.writerow(reordered_row)

print("CSV reordering complete. Output saved to 'output.csv'.")

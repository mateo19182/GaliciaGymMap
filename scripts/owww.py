import csv

def filter_rows_by_location(input_csv_path, output_csv_path):
    # Define the latitude and longitude bounds for Galicia
    lat_min, lat_max = 41.85, 43.79
    lon_min, lon_max = -9.29, -6.75

    with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
         open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        # Filter rows where latitude and longitude fall within Galicia
        for row in reader:
            try:
                lat = float(row['latitude'])
                lon = float(row['longitude'])
                if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
                    writer.writerow(row)
            except ValueError:
                # Skip rows with invalid data
                continue

# Example usage
input_csv_path = '/home/mateo/GaliciaGymMap/search_demo/static/transformed.csv'  # Update this to your CSV file's path
output_csv_path = 'output.csv'  # Desired path for the output CSV

filter_rows_by_location(input_csv_path, output_csv_path)

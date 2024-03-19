import pandas as pd
import geopandas as gpd
import geojson
import requests
import os
import re
import unicodedata


def xls_to_geojson(xls_file_path, geojson_file_path, latitude_column, longitude_column):
    # Read Excel file into a DataFrame
    df = pd.read_excel(xls_file_path)

    # Create a GeoDataFrame using latitude and longitude columns
    geometry = gpd.points_from_xy(df[longitude_column], df[latitude_column])
    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    # Convert GeoDataFrame to GeoJSON and save to a file
    gdf.to_file(geojson_file_path, driver='GeoJSON')

def get_coordinates(concello_name, country="Spain", format="json"):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{concello_name}, {country}",
        "format": format
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        location = data[0]
        latitude, longitude = float(location["lat"]), float(location["lon"])
        return latitude, longitude
    else:
        print(f"Error: Unable to retrieve coordinates for {concello_name}")
        return None

def extract_concello_name(file_name):
    match = re.search(r'concello\s*([\w\s]+)\.xls', file_name, re.IGNORECASE | re.UNICODE)
    if match:
        return match.group(1).strip()
    else:
        return None

def process_files_in_folder(folder_path):
    concello_names = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            concello_name = extract_concello_name(file_name)
            if concello_name:
                concello_names.append(concello_name)
                print(f"Folder: {os.path.basename(root)}, File: {file_name}, Concello: {concello_name}")

    return concello_names

def create_geojson(main_folder_path):
    for root, dirs, files in os.walk(main_folder_path):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            concellos_features = []
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(".xls"):
                    full_path = os.path.join(folder_path, file_name)
                    concello_name = extract_concello_name(file_name)
                    if concello_name is not None:
                        coordinates = get_coordinates(concello_name)
                        if coordinates:
                            print(f"Concello: {concello_name}, Coordinates: {coordinates}")
                            feature = geojson.Feature(
                                properties={'name': concello_name},
                                geometry=geojson.Point((coordinates[1], coordinates[0]))
                            )
                            concellos_features.append(feature)
            if concellos_features:
                feature_collection = geojson.FeatureCollection(concellos_features)
                output_file = f"{dir_name.lower().replace(' ', '_')}.geojson"
                with open(output_file, "w") as f:
                    geojson.dump(feature_collection, f)
                print(f"GeoJSON file '{output_file}' created successfully for folder '{dir_name}'.")

def normalize_filename(filename):
    normalized_filename = unicodedata.normalize('NFD', filename)
    ascii_filename = normalized_filename.encode('ascii', 'ignore').decode('ascii')
    return ascii_filename

def rename_files(folder_path):
    files = os.listdir(folder_path)
    for filename in files:
        old_filepath = os.path.join(folder_path, filename)
        normalized_filename = normalize_filename(filename)
        new_filepath = os.path.join(folder_path, normalized_filename)
        os.rename(old_filepath, new_filepath)
        print(f'Renamed: {filename} to {normalized_filename}')

if __name__ == "__main__":
    #rename_files('fichas/pontevedra')
    create_geojson("fichas")
    print(f'Conversion completed.')

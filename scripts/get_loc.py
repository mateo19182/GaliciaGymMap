import pandas as pd
import requests
from tqdm import tqdm
import csv  # Import the csv module

# Define the function to get province and municipio using latitude and longitude
def get_location_details(lat, lon):
    url = f"https://www.cartociudad.es/geocoder/api/geocoder/reverseGeocode?lon={lon}&lat={lat}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('province', 'Not Found'), data.get('muni', 'Not Found')
        else:
            return 'Error', 'Error'
    except Exception as e:
        print(f"Exception occurred: {e}")
        return 'Exception', 'Exception'

# Function to update the CSV file with tqdm progress bar
def update_csv(file_path, new_file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Ensure 'provincia' and 'municipio' columns exist, or add them
    if 'provincia' not in df.columns:
        df['provincia'] = None
    if 'municipio' not in df.columns:
        df['municipio'] = None

    # Prepare the header for the new file based on the original DataFrame's columns
    headers = df.columns.tolist()

    # Write headers to the new file
    with open(new_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    # Wrap the iteration with tqdm for a progress bar
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Updating"):
        provincia, municipio = get_location_details(row['latitude'], row['longitude'])
        # Update the row in the DataFrame
        df.at[index, 'provincia'] = provincia
        df.at[index, 'municipio'] = municipio

        # Append the updated row to the new CSV file
        with open(new_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(df.loc[index].tolist())

# Specify the original file path and the new file path
original_file_path = '/home/mateo/GaliciaGymMap/search_demo/static/output.csv'
new_file_path = '/home/mateo/GaliciaGymMap/search_demo/static/output2.csv'

# Call the function with both file paths
update_csv(original_file_path, new_file_path)
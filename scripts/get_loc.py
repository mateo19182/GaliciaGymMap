import pandas as pd
import requests
from tqdm import tqdm

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
def update_csv(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Initialize a list to hold the updated data
    updated_data = []

    # Wrap the iteration with tqdm for a progress bar
    for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Updating"):
        provincia, municipio = get_location_details(row['latitude'], row['longitude'])
        updated_data.append((provincia, municipio))
    
    # Update the DataFrame with the fetched data
    df['provincia'], df['municipio'] = zip(*updated_data)
    
    # Write the updated DataFrame back to the CSV, overwriting the original
    df.to_csv(file_path, index=False)

# Replace 'your_file.csv' with the path to your actual CSV file
update_csv('/home/mateo/GaliciaGymMap/search_demo/static/output.csv')

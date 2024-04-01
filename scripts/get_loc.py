import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm  # for progress bar, optional

# Initialize geolocator
geolocator = Nominatim(user_agent="your_application_name")

# Load your CSV data
df = pd.read_csv("/home/mateo/GaliciaGymMap/search_demo/static/transformed.csv")  # make sure your CSV has 'latitude' and 'longitude' columns

# Function to get province, comarca, and municipio
def get_location_info(lat, lon):
    location = geolocator.reverse((lat, lon), exactly_one=True, language="es")
    if location:
        address = location.raw.get('address', {})
        provincia = address.get('state', '')
        comarca = address.get('county', '')
        municipio = address.get('municipality', '')
        return provincia, comarca, municipio
    else:
        return "", "", ""


province, comarca, municipio = get_location_info(df.iloc[0]['latitud'], df.iloc[0]['longitud'])
print(f"Province: {province}, Comarca: {comarca}, Municipio: {municipio}")
province, comarca, municipio = get_location_info(df.iloc[1]['latitud'], df.iloc[1]['longitud'])
print(f"Province: {province}, Comarca: {comarca}, Municipio: {municipio}")
# Apply the function to each row
tqdm.pandas()  # optional, for progress bar
df[['provincia', 'comarca', 'municipio']] = df.progress_apply(lambda row: get_location_info(row['latitud'], row['longitud']), axis=1, result_type="expand")

# Save the updated dataframe to a new CSV
df.to_csv("updated_file.csv", index=False)

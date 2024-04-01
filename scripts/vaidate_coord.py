import pandas as pd

def validate_coordinate(lat, lon):
    try:
        lat = float(lat)
        if not -90 <= lat <= 90:
            return False, f"Latitude {lat} out of range. Must be between -90 and 90."
    except ValueError:
        return False, f"Latitude value is not a valid number: '{lat}'."
    
    try:
        lon = float(lon)
        if not -180 <= lon <= 180:
            return False, f"Longitude {lon} out of range. Must be between -180 and 180."
    except ValueError:
        return False, f"Longitude value is not a valid number: '{lon}'."
    
    return True, "Coordinates are valid."

# Load the CSV data
df = pd.read_csv("/home/mateo/GaliciaGymMap/search_demo/static/transformed.csv")  # Update this to your file path

# Check each row for valid latitude and longitude
for index, row in df.iterrows():
    is_valid, message = validate_coordinate(row['latitud'], row['longitud'])
    if not is_valid:
        # Print the entire row with the problem
        print(f"Row {index + 1} has invalid coordinates: {message}")
        # Print the problematic row's details
        print(row)

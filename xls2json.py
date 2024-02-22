import pandas as pd
import geopandas as gpd

def xls_to_geojson(xls_file_path, geojson_file_path, latitude_column, longitude_column):
    # Read Excel file into a DataFrame
    df = pd.read_excel(xls_file_path)

    # Create a GeoDataFrame using latitude and longitude columns
    geometry = gpd.points_from_xy(df[longitude_column], df[latitude_column])
    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    # Convert GeoDataFrame to GeoJSON and save to a file
    gdf.to_file(geojson_file_path, driver='GeoJSON')

if __name__ == "__main__":
    xls_file_path = 'Fichas instalaciขns 4 provincias xullo 2009\Fichas instalaciขns concellos A Coruคa\Ficha instalaciขns deportivas concello Oroso.xls'  # Replace with the path to your Excel file
    geojson_file_path = 'output.geojson'  # Replace with the desired output GeoJSON file path
    latitude_column = 'Latitude'  # Replace with the actual latitude column name in your Excel file
    longitude_column = 'Longitude'  # Replace with the actual longitude column name

    xls_to_geojson(xls_file_path, geojson_file_path, latitude_column, longitude_column)

    print(f'Conversion completed. GeoJSON file saved at: {geojson_file_path}')

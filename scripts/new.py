import pandas as pd


original_df = pd.read_csv('/home/mateo/GaliciaGymMap/search_demo/static/updated_file.csv')

#original_df = original_df[~original_df['WKT']]

# original_df = original_df[~original_df['business_status'].isin(['CLOSED_PERMANENTLY', 'CLOSED_TEMPORARILY'])]
# original_df = original_df[~original_df['subtypes'].isin(['cemetery', 'Hotel', 'Church', 'Monastery, Tourist attraction', 'City or town hall', 'Airport', 'Beauty salon'])]
# original_df = original_df[~original_df['business_status'].isin(['CLOSED_PERMANENTLY', 'CLOSED_TEMPORARILY'])]


# column_mappings = {
#     'name': 'nombre',
#     'phone': 'telefono',
#     'site': 'web_link',
#     'full_address': 'direccion',
#     'postal_code': 'codigo_postal',
#     'latitude': 'latitud',
#     'longitude': 'longitud',
#     'description': 'descripcion',
#     'site': 'web_link',
#     'phone': 'telefono',
#     'location_link': 'maps_link',
#     'place_id': 'place_id',
#     'category': 'sector',
#     'type': 'tipo_instalacion',
#     'subtypes': 'subtipo_instalacion',
#     'borough': 'provincia',
#     'city': 'municipio',
#     'query': 'otro1',
#     'about': 'otro2',
#     }

# original_df = original_df.rename(columns=column_mappings)[list(column_mappings.values())]

# original_df['id'] = range(1, len(original_df) + 1)
# original_df['comarca'] = 'None'
# original_df['area_actividad'] = 'None'
# original_df['otro3'] = 'None'

#get loc

original_df = original_df[(original_df['provincia'] == 'Galicia') | pd.isna(original_df['provincia'])]


original_df.to_csv('transformed.csv', index=False)

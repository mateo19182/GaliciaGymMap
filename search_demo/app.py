from flask import Flask, jsonify, request, render_template_string
import pandas as pd

app = Flask(__name__)

# Assuming your CSV has the required columns 'sector', 'tipo_instalacion', 'subtipo_instalacion', 'area_actividad', etc.
csv_file_path = '/home/mateo/GaliciaGymMap/sports_complexes_galicia.csv'
df = pd.read_csv(csv_file_path)
df.fillna("None", inplace=True)

@app.route('/')
def home():
    # Extract unique values for the new sorting/filtering criteria
    sectors = df['sector'].unique().tolist()
    tipo_instalacion = df['tipo_instalacion'].unique().tolist()
    subtipo_instalacion = df['subtipo_instalacion'].unique().tolist()
    area_actividad = df['area_actividad'].unique().tolist()
    # Pass these lists to your template for rendering the filters/dropdowns
    return render_template_string(open('index.html').read(), sectors=sectors, tipo_instalacion=tipo_instalacion, subtipo_instalacion=subtipo_instalacion, area_actividad=area_actividad)

@app.route('/data', methods=['GET'])
def get_data():
    # Retrieve filter parameters from the query string
    sector = request.args.get('sector')
    tipo_instalacion = request.args.get('tipo_instalacion')
    subtipo_instalacion = request.args.get('subtipo_instalacion')
    area_actividad = request.args.get('area_actividad')

    # Start with all data, then filter based on the provided parameters
    filtered_data = df
    if sector:
        filtered_data = filtered_data[filtered_data['sector'] == sector]
    if tipo_instalacion:
        filtered_data = filtered_data[filtered_data['tipo_instalacion'] == tipo_instalacion]
    if subtipo_instalacion:
        filtered_data = filtered_data[filtered_data['subtipo_instalacion'] == subtipo_instalacion]
    if area_actividad:
        filtered_data = filtered_data[filtered_data['area_actividad'] == area_actividad]

    # Ensure proper JSON serialization
    filtered_data = filtered_data.where(pd.notnull(filtered_data), None)
    return jsonify(filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

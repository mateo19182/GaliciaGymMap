from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your CSV data into a DataFrame
df = pd.read_csv('/home/mateo/GaliciaGymMap/modified_file.csv')
# data = [
#     {"id": 0, "name": "Área recreativa Ponte das Taboas", "type": "Public swimming pool", "subtype": "attractions"},
#     {"id": 1, "name": "Praia fluvial de Ponte Caldelas", "type": "Hiking area", "subtype": "Tourist attraction"}
# ]
df['type'] = df['type'].fillna('')
df['subtypes'] = df['subtypes'].fillna('')
@app.route('/search', methods=['GET'])
def search():
    type_filter = request.args.get('type')
    subtype_filter = request.args.get('subtype')
    
    # Filter the DataFrame based on query parameters
    filtered_df = df
    if type_filter:
        filtered_df = filtered_df[filtered_df['type'].str.contains(type_filter, case=False)]
    if subtype_filter:
        filtered_df = filtered_df[filtered_df['subtypes'].str.contains(subtype_filter, case=False)]
    
    # Convert the filtered DataFrame to JSON
    result = filtered_df.to_json(orient="records")
    return result

if __name__ == '__main__':
    app.run(debug=True)

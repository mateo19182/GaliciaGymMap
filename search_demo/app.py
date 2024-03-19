from flask import Flask, jsonify, request, render_template_string
import pandas as pd

app = Flask(__name__)

# Assuming the CSV is named 'data.csv' and has columns 'id', 'name', 'category', etc.
csv_file_path = '/home/mateo/GaliciaGymMap/modified_file.csv'
df = pd.read_csv(csv_file_path)
df.fillna("None", inplace=True)

# df['category'] = df['category'].fillna('')
# df['type'] = df['type'].fillna('')
# df['subtypes'] = df['subtypes'].fillna('')

# Home route to serve the HTML page
@app.route('/')
def home():
    # Extract unique categories for the category dropdown
    categories = df['category'].unique().tolist()
    return render_template_string(open('index.html').read(), categories=categories)

# Data route to handle filtering and return JSON data
@app.route('/data', methods=['GET'])
def get_data():
    category = request.args.get('category')
    type_filter = request.args.get('type')

    # Start with all data, then filter by category
    filtered_data = df[df['category'] == category] if category else df

    # If a type is specified, further filter by type within the selected category
    if type_filter:
        filtered_data = filtered_data[filtered_data['type'] == type_filter]

    # Replace NaN values to ensure proper JSON serialization
    filtered_data = filtered_data.where(pd.notnull(filtered_data), None)
    return jsonify(filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

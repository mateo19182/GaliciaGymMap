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
@app.route('/')
def home():
    categories = df['category'].unique().tolist()
    return render_template_string(open('index.html').read(), categories=categories)

@app.route('/data', methods=['GET'])
def get_data():
    category = request.args.get('category')
    if category:
        filtered_data = df[df['category'] == category].copy()
    else:
        filtered_data = df.copy()
    
    # Replace NaN values with None, which is converted to null in JSON
    filtered_data = filtered_data.where(pd.notnull(filtered_data), None)

    return jsonify(filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd

# Load the CSV file
df = pd.read_csv('/home/mateo/GaliciaGymMap/search_demo/static/updated_categories.csv')

# Filter the DataFrame where 'comarca' equals 'Pontevedra'
filtered_df = df[df['comarca'] == 'Pontevedra']

# Write the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_pontevedra.csv', index=False)

print("Filtered CSV file has been created.")

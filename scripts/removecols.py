import pandas as pd

# Load the CSV file
df = pd.read_csv('merged.csv')

# Columns to be removed
columns_to_remove = [
    'query', 'us_state', 'country', 'country_code', 'time_zone', 'plus_code',
    'area_service', 'reviews', 'reviews_tags', 'reviews_per_score',
    'reviews_per_score_1', 'reviews_per_score_2', 'reviews_per_score_3',
    'reviews_per_score_4', 'reviews_per_score_5', 'photos_count', 'street_view',
    'located_in', 'working_hours_old_format', 'other_hours', 'popular_times',
    'range', 'posts', 'typical_time_spent'
]


# Drop the specified columns
df_modified = df.drop(columns=columns_to_remove, errors='ignore')

# Save the modified DataFrame to a new CSV file
df_modified.to_csv('modified_file.csv', index=False)

print("Columns removed and file saved as 'modified_file.csv'.")

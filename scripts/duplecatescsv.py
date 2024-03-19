import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with your actual file paths
file1_path = 'data/piscinas2.csv'
file2_path = 'data/sport3.csv'

# Read the CSV files
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

df = pd.concat([df1, df2])
df.to_csv('merged.csv')


'''
# Find rows present in both dataframes
common_rows = pd.merge(df1, df2, how='inner')

# If you want to remove rows based on a specific column or columns being identical,
# you can specify those columns in the on parameter of merge function like this:
# common_rows = pd.merge(df1, df2, on=['column_name1', 'column_name2'], how='inner')

# Remove rows from df1 that are present in df2
df1_modified = pd.concat([df1, common_rows, common_rows]).drop_duplicates(keep=False)

# Save the modified dataframe to a new CSV file
df1_modified.to_csv('C:\\Users\\mateo\\Downloads\\sport3.csv', index=False)
'''
print('Done--------------------')

import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('your_excel_file.xlsx', sheet_name='Sheet1')

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)

# Save the JSON to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

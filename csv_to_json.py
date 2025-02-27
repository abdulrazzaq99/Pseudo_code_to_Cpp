import pandas as pd
import json

# Load the dataset from a CSV file
csv_file_path = 'your_file.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Initialize variables
concatenated_data = []
current_pseudo = ""
current_code = ""

# Iterate through the DataFrame
for index, row in df.iterrows():
    if row['line'] == 0 and index != 0:
        # Save the previous code block
        concatenated_data.append({
            'pseudocode': current_pseudo.strip(),
            'code': current_code.strip()
        })
        # Reset for new code block
        current_pseudo = ""
        current_code = ""
    
    # Concatenate pseudocode and code
    if pd.notna(row['text']):
        current_pseudo += row['text'] + "\n"
    if pd.notna(row['code']):
        current_code += row['code'] + "\n"

# Append the last code block
if current_pseudo or current_code:
    concatenated_data.append({
        'pseudocode': current_pseudo.strip(),
        'code': current_code.strip()
    })

# Convert to JSON
json_output = json.dumps(concatenated_data, indent=4)
print(json_output)

# Optionally, save the JSON to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_output)
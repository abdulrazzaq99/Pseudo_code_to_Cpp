import json

# Load dataset
file_path = "cleaned_dataset.json"  # Change this to your actual file path

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Remove the "cpp_code" field from each entry
for entry in data:
    if "cpp_code" in entry:
        del entry["cpp_code"]

# Save the updated dataset
cleaned_file_path = "cleaned_dataset1.json"
with open(cleaned_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Cleaned dataset saved to {cleaned_file_path}")
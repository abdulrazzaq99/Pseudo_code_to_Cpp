import json
import re

# Load dataset
file_path = "output.json"  # Change this to your actual file path

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Function to clean pseudocode
def clean_pseudocode(pseudocode):
    if not pseudocode or pseudocode.strip().lower() == "nan":
        return ""

    # Normalize whitespace
    pseudocode = re.sub(r'\s+', ' ', pseudocode.strip())

    # Standardize keywords
    pseudocode = re.sub(r'\bcreate\b', 'let', pseudocode, flags=re.IGNORECASE)
    pseudocode = re.sub(r'\bRead\b', 'read', pseudocode, flags=re.IGNORECASE)

    # Ensure consistent formatting for expressions
    pseudocode = re.sub(r'set (\w+) =', r'\1 =', pseudocode)

    # Fix spacing around operators
    pseudocode = re.sub(r'([+\-*/=<>])', r' \1 ', pseudocode)

    return pseudocode.strip()

# Function to clean C++ code
def clean_cpp_code(code):
    if not code or code.strip().lower() == "nan":
        return ""

    # Normalize indentation
    code = re.sub(r'\t+', '    ', code)  # Convert tabs to spaces
    code = re.sub(r' +\n', '\n', code)  # Remove trailing spaces

    return code.strip()

# Apply cleaning functions
for entry in data:
    # Clean pseudocode and C++ code
    cleaned_pseudocode = clean_pseudocode(entry.get("pseudocode", ""))
    cleaned_cpp_code = clean_cpp_code(entry.get("cpp_code", ""))

    # Update the entry with cleaned data
    entry["pseudocode"] = cleaned_pseudocode
    entry["cpp_code"] = cleaned_cpp_code

# Save cleaned dataset
cleaned_file_path = "cleaned_dataset.json"
with open(cleaned_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Cleaned dataset saved to {cleaned_file_path}")
import pandas as pd
import json

# Load the CSV file
df = pd.read_csv("full_taxonomy.csv")

# Replace NaN values with 'unknown'
df.fillna("unknown", inplace=True)

# Convert to list of dictionaries
taxonomy_list = df.to_dict(orient="records")

# Write to JSON file
with open("full_taxonomy.json", "w") as f:
    json.dump(taxonomy_list, f, indent=2)

print("Saved as full_taxonomy.json")

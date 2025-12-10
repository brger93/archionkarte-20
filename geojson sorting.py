import json
from pathlib import Path

# Define Input GeoJSON
input_file = input("Enter path to input file:") 
path = Path(input_file.replace('"', ''))

# Load GeoJSON
with open(input_file, "r", encoding="utf-8") as file:
    geojson = json.load(file)

# Sort features by "district" property
geojson["features"].sort(key=lambda feature: (feature["properties"].get("district"), feature["properties"].get("name")))

# Define Output GeoJSON (Windows)
output_file = input("Enter path to output file:") 
path = Path(output_file.replace('"', ''))

# Save sorted GeoJSON
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(geojson, file, indent=4, ensure_ascii=False)
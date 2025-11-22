import json
from pathlib import WindowsPath

# Define Input GeoJSON (Windows)
input_file = input("Enter path to input file:") 
path = WindowsPath(input_file.replace('"', ''))

# Load GeoJSON
with open(input_file, "r", encoding="utf-8") as file:
    geojson = json.load(file)

# Sort features by "district" property
geojson["features"].sort(key=lambda feature: feature["properties"].get("district", "name"))

# Define Output GeoJSON (Windows)
output_file = input("Enter path to output file:") 
path = WindowsPath(output_file.replace('"', ''))

# Save sorted GeoJSON
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(geojson, file, indent=2)
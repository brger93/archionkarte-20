import json
from pathlib import Path

# Input Path
input_file = input('Enter path to input file:')
path = Path(input_file.replace('"', ''))

# Load GeoJSON
with open(input_file, 'r', encoding='utf-8') as file:
    geojson = json.load(file)

# Sorting
geojson['features'].sort(
    key=lambda feature: (
        feature['properties'].get('district'),
        feature['properties'].get('name'),
    )
)

# Output Path
output_file = input('Enter path to output file:')
path = Path(output_file.replace('"', ''))

# Save GeoJSON
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(geojson, file, indent=2, ensure_ascii=False)

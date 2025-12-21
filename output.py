import json
import logging
import pandas as pd

logger = logging.getLogger('archionkarte_20')


def write_df_to_geojson(df: pd.DataFrame) -> dict:
    """
    This function transforms a DataFrame into a dict with GeoJSON format.
    """
    geojson = {'type': 'FeatureCollection', 'features': []}

    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': {}},
            'properties': {},
        }
        feature['geometry']['coordinates'] = [row['longitude'], row['latitude']]
        for prop in ['name', 'district', 'archive', 'path']:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    logger.info('GeoJSON was created.')
    return geojson


def save_geojson(output_json_path: str, geojson_archion: dict):
    """
    This function dumps the dict in GeoJSON format into a json file.
    """
    with open(output_json_path, 'wb') as file:
        file.write(json.dumps(geojson_archion, indent=2).encode('utf-8'))
    logger.info('GeoJSON was saved.')
    return file

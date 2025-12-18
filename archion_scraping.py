import json
import logging
import pandas as pd
import requests
import time

from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

logger = logging.getLogger('archionkarte_20')


def scrape_archion_content(url: str) -> tuple[list, list]:
    """
    This function extracts a list of all digitised church books for a
    single archive on www.archion.de and the respective direct links.
    """
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    archion = soup.find('div', id='archive-nav')

    # Extract titles
    archive_list = []
    for anchor in archion.find_all('a'):
        archive_list.append(anchor.text.strip())

    logger.info('Parish titles were processed.')

    # Extract links
    link_list = []
    for anchor in archion.find_all('a'):
        link_list.append(anchor.get('href'))

    logger.info('Parish links were processed.')
    return archive_list, link_list


def get_long_and_lat(archive_list: list) -> tuple[list, list]:
    """
    This function requests latitude and longitude for each parish
    and writes the values into a list.
    """
    # Initalize
    archive_names = []
    lat = []
    long = []

    # Create list with only archive names (Beware: Parish name with suffix)
    for i in range(len(archive_list)):
        archive_names.append(archive_list[i].split()[0])

    logger.info('Archive names were extracted.')

    # Get lat and long
    geolocator = Nominatim(user_agent='archionkarte')

    for name in archive_names:
        location = geolocator.geocode(name)
        logger.info(f'Processing of: {name}')

        try:
            lat.append(location.latitude)
            long.append(location.longitude)
        except Exception:
            logger.warning(f'Geodata could not be retrieved: {name}')
            lat.append(0)
            long.append(0)
        # apply sleep time to comply with Nominatim GTCs
        time.sleep(0.5)

    logger.info('Geodata was processed.')
    return lat, long


def get_df(
    archive_list: list,
    link_list: list,
    archive_name: str,
    district_name: str,
    lat: list,
    long: list,
) -> pd.DataFrame:
    """
    This function creates a DataFrame with parish name, district name, archive name,
    parish URL, parish latitude and parish longitude.
    """
    df = pd.DataFrame(archive_list)
    df['district'] = district_name
    df['archive'] = archive_name
    df['path'] = pd.Series(link_list, index=df.index)
    df['latitude'] = pd.Series(lat, index=df.index)
    df['longitude'] = pd.Series(long, index=df.index)
    df.columns = ['name', 'district', 'archive', 'path', 'latitude', 'longitude']
    df.reset_index(drop=True)
    logger.info('DataFrame was created.')
    return df


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


def main():
    # Logging Config
    logging.basicConfig(level=logging.INFO)

    # Define URL (e.g. https://www.archion.de/de/alle-archive/niedersachsen/archiv-der-evangelisch-lutherischen-landeskirche-oldenburg)
    url = input('Enter URL to Archion archive overview page:')
    url = f'{url}'

    # Web Scraping
    archive_list, link_list = scrape_archion_content(url)

    # Define Archive Name (e.g. Bistumsarchiv Speyer)
    archive_name = input('Enter name of archive:')

    # Define District Name (e.g. Kirchenkreis Hamburg-Ost)
    district_name = input('Enter name of district:')

    # Get Latitude and Longitude
    lat, long = get_long_and_lat(archive_list)

    # Get DataFrame
    df = get_df(
        archive_list,
        link_list,
        archive_name,
        district_name,
        lat,
        long,
    )

    # Create GeoJSON
    geojson_archion = write_df_to_geojson(df)

    # Define Output GeoJSON File Path
    output_json_path = input('Enter path to save GeoJSON output file:')

    # Save to GeoJSON
    save_geojson(output_json_path, geojson_archion)


if __name__ == '__main__':
    main()

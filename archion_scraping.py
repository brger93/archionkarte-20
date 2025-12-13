from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import json
import pandas as pd
import requests


def scrape_archion_content(url):
    """
    This function extracts a list of all digitised church books for a
    single archive on www.archion.de and the respective direct links.
    """
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    archion = soup.find('div', id='archive-nav')

    # Extract titles
    archive_list = []
    for i in archion.find_all('a'):
        archive_list.append(i.text.strip())

    # Extract links
    link_list = []
    for i in archion.find_all('a'):
        link_list.append(i.get('href'))
    return archive_list, link_list


def get_long_and_lat(archive_list):
    """
    This function requests latitude and longitude for each parish.
    """
    # Initalize
    archive_names = []
    lat = []
    long = []

    # Create list with only archive names
    for i in range(len(archive_list)):
        archive_names.append(archive_list[i].split()[0])

    # Get lat and long
    geolocator = Nominatim(user_agent='archionkarte')

    for a in archive_names:
        location = geolocator.geocode(a)

        lat.append(location.latitude)
        long.append(location.longitude)
    return lat, long


def save_df_to_excel(
    output_excel_path, archive_list, link_list, archive_name, district_name, lat, long
):
    """
    This function saves a DataFrame with parish name, district name, archive name,
    parish URL, parish latitude and parish longitude to xlxs.
    """
    df = pd.DataFrame(archive_list)
    df['district'] = district_name
    df['archive'] = archive_name
    df['path'] = pd.Series(link_list, index=df.index)
    df['latitude'] = pd.Series(lat, index=df.index)
    df['longitude'] = pd.Series(long, index=df.index)
    df.columns = ['name', 'district', 'archive', 'path', 'latitude', 'longitude']
    file = df.to_excel(output_excel_path, index=False)
    return file


def write_df_to_geojson(data, properties, lat='latitude', lon='longitude'):
    """
    This function transforms the created DataFrame into GeoJSON format.
    """
    geojson = {'type': 'FeatureCollection', 'features': []}

    for _, row in data.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': {}},
            'properties': {},
        }
        feature['geometry']['coordinates'] = [row[lon], row[lat]]
        for prop in ['name', 'district', 'archive', 'path']:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


def save_geojson(output_json_path, geojson_archion):
    """
    This function saves the created GeoJSON into a json file.
    """
    with open(output_json_path, 'wb') as file:
        file.write(json.dumps(geojson_archion, indent=2).encode('utf-8'))
    return file


def main():
    # Define Output File Path
    output_excel_path = input('Enter path to save Excel output file:')

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

    # Save to Excel
    save_df_to_excel(
        output_excel_path,
        archive_list,
        link_list,
        archive_name,
        district_name,
        lat,
        long,
    )

    # Read-in Archion Data
    data = pd.read_excel(output_excel_path)
    cols = ['name', 'district', 'archive', 'path', 'latitude', 'longitude']

    # Create GeoJSON
    geojson_archion = write_df_to_geojson(data, cols)

    # Define Output GeoJSON File Path
    output_json_path = input('Enter path to save GeoJSON output file:')

    # Save to GeoJSON
    save_geojson(output_json_path, geojson_archion)


if __name__ == '__main__':
    main()

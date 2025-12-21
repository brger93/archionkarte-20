import logging

from archion_scraping import (
    scrape_archion_content,
    get_df,
    get_long_and_lat,
    write_df_to_geojson,
    save_geojson,
)


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

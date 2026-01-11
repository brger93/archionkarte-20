import argparse
import logging

from archionkarte.output import save_geojson, write_df_to_geojson
from archionkarte.preprocessing import (
    get_df,
    get_long_and_lat,
    scrape_archion_content,
)


def main() -> None:
    """Create and save GeoJSON based on user settings."""
    # Logging Config
    logging.basicConfig(level=logging.INFO)

    # Parser Config
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        help="URL to Archion web page",
        required=True,
    )
    parser.add_argument(
        "--archive",
        help="Name of archive",
        required=True,
    )
    parser.add_argument(
        "--district",
        help="Name of district",
        required=True,
    )
    parser.add_argument(
        "--path",
        help="Output path",
        required=True,
    )
    args = parser.parse_args()

    # Define URL
    url = args.url

    # Web Scraping
    archive_list, link_list = scrape_archion_content(url)

    # Define Archive Name
    archive_name = args.archive

    # Define District Name
    district_name = args.district

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
    output_json_path = args.path

    # Save to GeoJSON
    save_geojson(output_json_path, geojson_archion)


if __name__ == "__main__":
    main()

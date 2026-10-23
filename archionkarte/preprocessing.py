import json
import logging
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

logger = logging.getLogger("archionkarte_20")


def scrape_archion_content(url: str) -> tuple[list, list]:
    """Extract a list of all digitised church books on www.archion.de."""
    soup = BeautifulSoup(requests.get(url, timeout=20).content, "html.parser")

    archion = soup.find("div", id="archive-nav")

    # Extract titles
    archive_list = []
    for anchor in archion.find_all("a"):
        archive_list.append(anchor.text.strip())

    logger.info("Parish titles were processed.")

    # Extract links
    link_list = []
    for anchor in archion.find_all("a"):
        link_list.append(anchor.get("href"))

    logger.info("Parish links were processed.")
    return archive_list, link_list


def get_long_and_lat(archive_list: list) -> tuple[list, list]:
    """Get latitude and longitude for each parish and write to a list."""
    # Initalize
    archive_names = []
    lat = []
    long = []

    # Create list with only archive names (Beware: Parish name with suffix)
    for i in range(len(archive_list)):
        archive_names.append(archive_list[i].split()[0])

    logger.info("Archive names were extracted.")

    # Get lat and long
    geolocator = Nominatim(user_agent="archionkarte")

    for name in archive_names:
        location = geolocator.geocode(name)
        logger.info("Processing of: %s", name)

        try:
            lat.append(location.latitude)
            long.append(location.longitude)
        except Exception:
            logger.warning("Geodata could not be retrieved: %s", name)
            lat.append(0)
            long.append(0)
        # apply sleep time to comply with Nominatim GTCs
        time.sleep(1.5)

    logger.info("Geodata was processed.")
    return lat, long


def get_gov_id(archive_list: list) -> list[str]:
    """Get GOV ID for each parish and write to a list."""
    # Initialize
    gov_id = []
    archive_names = []
    gov_object_type = 26  # Parish
    status = 200  # HTTP 200 OK

    # Create list with only archive names (Beware: Parish name with suffix)
    for i in range(len(archive_list)):
        archive_names.append(archive_list[i].split()[0])

    # Get GOV object ID
    for parish in archive_names:
        api_params = {"placename": parish, "types": gov_object_type}
        api_url = "https://gov.genealogy.net/api/searchByNameAndType"

        response = requests.get(api_url, params=api_params, timeout=10)

        if response.status_code == status:
            data = json.loads(response.text)

            if not data:
                gov_id.append("")
            if data:
                parish_gov_id = data[0]["id"]
                gov_id.append(parish_gov_id)

    return gov_id


def get_df(
    archive_list: list,
    link_list: list,
    archive_name: str,
    district_name: str,
    gov_id: list,
    lat: list,
    long: list,
) -> pd.DataFrame:
    """Create a DataFrame with parish properties."""
    df = pd.DataFrame(archive_list)
    df["district"] = district_name
    df["archive"] = archive_name
    df["path"] = pd.Series(link_list, index=df.index)
    df["gov"] = pd.Series(gov_id, index=df.index)
    df["latitude"] = pd.Series(lat, index=df.index)
    df["longitude"] = pd.Series(long, index=df.index)
    df.columns = [
        "name",
        "district",
        "archive",
        "path",
        "gov",
        "latitude",
        "longitude",
    ]
    df.reset_index(drop=True)
    logger.info("DataFrame was created.")
    return df

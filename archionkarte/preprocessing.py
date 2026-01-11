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
        time.sleep(0.5)

    logger.info("Geodata was processed.")
    return lat, long


def get_df(
    archive_list: list,
    link_list: list,
    archive_name: str,
    district_name: str,
    lat: list,
    long: list,
) -> pd.DataFrame:
    """Create a DataFrame with parish properties."""
    df = pd.DataFrame(archive_list)
    df["district"] = district_name
    df["archive"] = archive_name
    df["path"] = pd.Series(link_list, index=df.index)
    df["latitude"] = pd.Series(lat, index=df.index)
    df["longitude"] = pd.Series(long, index=df.index)
    df.columns = [
        "name",
        "district",
        "archive",
        "path",
        "latitude",
        "longitude",
    ]
    df.reset_index(drop=True)
    logger.info("DataFrame was created.")
    return df

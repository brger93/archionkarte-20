from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
 
def scrape_archion_content(url): 
    """
    This function extracts a list of all digitised church
    books for a single archive on www.archion.de and the
    respective direct links.
    """ 
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    archion = soup.find("div", id="archive-nav")

    # Extract titles
    archive_list = []
    for i in archion.find_all("a"):
        archive_list.append(i.text.strip())
    
    # Extract links
    link_list =[]
    for i in archion.find_all("a"):
        link_list.append(i.get("href"))
        
    return archive_list, link_list

def save_df_to_excel(output_excel_path, archive_list, link_list, archive_name, district_name):
    """
    This function saves a DataFrame(parish name, district name, archive name, parish URL)
    to xlxs.
    """
    df = pd.DataFrame(archive_list)
    df['district'] = district_name
    df['archive'] = archive_name
    df['path'] = pd.Series(link_list, index=df.index)
    df['latitude'] = 51.3300
    df['longitude'] = 12.1700
    df.columns = ['name', 'district', 'archive', 'path', 'latitude', 'longitude']
    file = df.to_excel(output_excel_path, index=False)
    return file

def write_df_to_geojson(data, properties, lat='latitude', lon='longitude'):
    geojson = {"type": "FeatureCollection", "features":[]}

    for _, row in data.iterrows():
        feature = {"type": "Feature",
                   "geometry": {"type": "Point",
                   "coordinates":{}},
                   "properties":{},}
        feature["geometry"]["coordinates"] = [row[lon], row[lat]]
        for prop in ['name', 'district', 'archive', 'path']:
            feature["properties"][prop] = row[prop]
        geojson["features"].append(feature)
    return geojson
    
def save_geojson(output_json_path, geojson_archion):
    with open(output_json_path, "wb") as file:
        file.write(json.dumps(geojson_archion, indent=4).encode("utf-8"))
    return file

def main(): 
    # Define Output File Path
    output_excel_path = input("Enter path to save Excel output file:") 
    
    # Define URL (e.g. https://www.archion.de/de/alle-archive/niedersachsen/archiv-der-evangelisch-lutherischen-landeskirche-oldenburg)
    url = input("Enter URL to Archion archive overview page:")
    url = f"{url}"

    # Web Scraping
    archive_list, link_list = scrape_archion_content(url)

    # Define Archive Name (e.g. Bistumsarchiv Speyer)
    archive_name = input("Enter name of archive:") 
   
    # Define District Name (e.g. Kirchenkreis Hamburg-Ost)
    district_name = input("Enter name of district:") 
    
    # Save to Excel
    save_df_to_excel(output_excel_path, archive_list, link_list, archive_name, district_name)

    # Define Input File Path
    input_file = input("Enter path to read-in Excel file:") 
    
    # Read-in Archion Data
    data = pd.read_excel(input_file)
    cols = ["name", "district", "archive", "path", "latitude", "longitude"]

    # Create GeoJSON
    geojson_archion = write_df_to_geojson(data, cols)

    # Define Output GeoJSON File Path
    output_json_path = input("Enter path to save GeoJSON output file:")

    # Save to GeoJSON
    save_geojson(output_json_path, geojson_archion)

if __name__ == "__main__":
    main()
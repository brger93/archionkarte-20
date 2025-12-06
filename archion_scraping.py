from bs4 import BeautifulSoup
import requests
import pandas as pd
 
def ContentScraping(url): 
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

def SaveExcel(output_file, archive_list, link_list):
    """
    This function saves a DataFrame(Parish Name, Parish URL)
    to xlxs.
    """
    df = pd.DataFrame(archive_list)
    df['Link'] = pd.Series(link_list, index=df.index)
    file = df.to_excel(output_file, index=False, header=False)
    return file
    
def main(): 
    # Define Output File Path
    output_file = input("Enter path to output file:") 
    
    # Example URL: https://www.archion.de/de/alle-archive/niedersachsen/archiv-der-evangelisch-lutherischen-landeskirche-oldenburg
    url = input("Enter URL to Archion archive overview page:")
    url = f"{url}"

    # Web Scraping
    archive_list, link_list = ContentScraping(url)
    
    # Saving
    SaveExcel(output_file, archive_list, link_list)

if __name__ == "__main__":
    main()
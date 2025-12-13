# archionkarte-20
GeoJSONs for uMap *Archionkarte 2.0*

<!-- ABOUT THE PROJECT -->
## About the Project
The genealogy platform [ARCHION](https://www.archion.de) provides access to digitised church books.

To enable a graphical 

The uMap [Archionkarte 2.0](https://umap.openstreetmap.de/de/map/archionkarte-20_113993) was created to provide a graphical overview of the digitisation status. The underlying GeoJSONs are maintened in this GitHub repository.

<!-- CONTRIBUTION -->
## Contribution
### First Contact
Dial into public Zoom meeting of [WikiTree Stammtisch](https://www.wikitree.com/wiki/Space:Stammtisch) and you will be made a GitHub collaborator.

### Alignment
Ongoing projects are posted on [Archionkarte 2.0](https://www.wikitree.com/wiki/Space:Archionkarte_2.0) under the chapter *Work in Progress*. A WikiTree account is required to modify the free space page.

### GeoData
Please follow these steps to update geodata:
* Create GeoJSON (district) via *archion_scraping.py*.
* If applicable, copy GEOJSON (district) into GeoJSON (archive) manually.

There are no requirements set for pushes to *main* at the moment for project collaborators.

<!-- RELEASE PROCESS -->
## Release Process
Please follow these steps to update the uMap:
* Copy GitHub's raw content URL of updated GeoJSON (sorted).
* Open [Archionkarte 2.0](https://umap.openstreetmap.de/de/map/anonymous-edit/113993:ienKfbLQGKj4f7-ECaz57MoGGDLw_VjWkT2Q0LFKPME).
* Select on the right side **Import data**.
* Paste GitHub's raw content URL.
* Choose data format *geojson* from dropdown menu.
* Choose the corresponding layer (aka archive) from dropdown menu.
* Check the box *replace layer content*.
* Upload the data

<!-- Change Log -->
## Change Log
Changes shall be documented in CHANGELOG.

<!-- Archive -->
## Archive
GeoJSONs under folder *geojson* should not be uploaded to uMap. Those are archived versions which were published by user **Basil** in January 2025 on legacy uMap [Archionkarte](https://umap.openstreetmap.de/de/map/archionkarte_46875).

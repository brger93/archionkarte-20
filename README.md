# archionkarte-20
GeoJSONs for uMap *Archionkarte 2.0*

<!-- ABOUT THE PROJECT -->
## About the Project
The genealogy platform [ARCHION](https://www.archion.de) provides access to digitised church books.

The uMap [Archionkarte 2.0](https://umap.openstreetmap.de/de/map/archionkarte-20_113993) was created to provide a graphical overview of the digitisation status. The underlying GeoJSONs are maintened in this GitHub repository.

<!-- Getting Started -->
## Getting Started
### Alignment
Ongoing projects are posted on [Archionkarte 2.0](https://www.wikitree.com/wiki/Space:Archionkarte_2.0) under the chapter *Work in Progress*.

### Setup
Before starting on this project, you need to get [uv](https://docs.astral.sh/uv/). We recommend to install it as standalone via *pipx*.

Once *uv* is installed, run the following command to set up your development environment. This will install all dependencies and the correct Python version required. Package versions are locked in *uv.lock* file.
```bash
uv sync --upgrade --all-groups
```
Activate your environment via:
```bash
.venv/Scripts/activate
```
<!-- CONTRIBUTION -->
## Contribution
There are no requirements set for pushes to main branch at the moment for project collaborators.

### GeoData Processing
To create a GeoJSON for a desired church district, call `main` module and execute as script:
```bash
python -m archionkarte.main --url URL --archive ARCHIVE --district DISTRICT --path PATH
```
The following command-line arguments are expected:
* `--url`: URL to Archion web page on district level
* `--archive`: Name of archive, e.g. "Ev. Landeskirche in Mitteldeutschland - Magdeburg"
* `--district`: Name of district, e.g. "Kirchenkreis Elbe-Fläming"
* `--path`: Output path for json file, e.g. "C:/Users/username/workspace/elbe-fläming.json"

> [!TIP]
>If applicable, copy GeoJSON (district) into existing GeoJSON (archive) manually.

> [!IMPORTANT]
>The geolocations must be checked for accuracy!

### GOV Object ID Processing
The geolocations are supplemented by object IDs (type 26) of GOV, a historical geographic database maintained by CompGen. The IDs are obtained using the GOV Webservice (searchByNameAndType).

> [!IMPORTANT]
>The object IDs must be checked for accuracy!

<!-- RELEASE PROCESS -->
## Release Process
Please follow these steps to update the uMap:
* Copy GitHub's raw content URL of updated GeoJSONs in folder *data/geojson_sorted*.
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
GeoJSONs in folder *data/geojson* should not be uploaded to uMap. Those are archived versions which were published by user **Basil** in January 2025 on legacy uMap [Archionkarte](https://umap.openstreetmap.de/de/map/archionkarte_46875).

# archionkarte-20
GeoJSONs for uMap *Archionkarte 2.0*

<!-- ABOUT THE PROJECT -->
## About The Project
The genealogy platform [ARCHION](https://www.archion.de) provides access to digitised church records. To gain a better overview of the locations of the 175,000 church books that have already been digitised, a uMap has been set up:
* [Archionkarte 2.0. Read-only](https://umap.openstreetmap.de/de/map/archionkarte-20_113993)

This GitHub repository helps to maintain the underlying GeoJSONs so that they correctly reflect the digitisation status on the map.

<!-- CONTRIBUTION -->
## Contribution
As soon as new church records are uploaded to [ARCHION](https://www.archion.de/de/archion-entdecken/alle-news/neue-digitalisate), all help is welcome.

Ongoing projects can be found on web page of [WikiTree Stammtisch](https://www.wikitree.com/wiki/Space:Stammtisch). Please announce your project either in the biweekly meeting or add it to the *Work in Progress* list on the web page under chapter 4 *Archionkarte 2.0*.

There are no requirements set for pushes to *main* at the moment.

<!-- RELEASE PROCESS -->
## Release Process
The following steps must be executed to update the uMap:
* Copy GitHub's raw content URL of updated GeoJSON (sorted).
* Open [Archionkarte 2.0 Edit](https://umap.openstreetmap.de/de/map/anonymous-edit/113993:ienKfbLQGKj4f7-ECaz57MoGGDLw_VjWkT2Q0LFKPME).
* Select on the right side **Import data**.
* Paste GitHub's raw content URL.
* Choose data format *geojson* from dropdown menu.
* Choose the corresponding layer (aka archive) from dropdown menu.
* Check the box *replace layer content*.
* Upload the data

<!-- Change Log -->
## Change Log
Changes and relases shall be documented in CHANGELOG.


<!-- Archive -->
## Archive
GeoJSONs under folder *geojson* should not be uploaded to uMap. Those are archived versions which were published by user **Basil** in January 2025 on legacy uMap [Archionkarte](https://umap.openstreetmap.de/de/map/archionkarte_46875).

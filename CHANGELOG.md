# Change Log
All notable changes to this project will be documented in this file.

## [4.2.0] - 2026-01-11
### Added
* *raw input* replaced with *argparse* for input of url, archive, district and output path

## [4.1.0] - 2026-01-10
### Added
* *sachsen_sorted.json* was extended by new parishes (Kirchenbezirk Auerbach)

## [4.0.0] - 2026-01-09  
### Changed
* uv was introduced as project and package manager

## [3.4.1] - 2026-01-05  
### Added
* bug in *magdeburg_sorted.json* was fixed (Döbrichau)

## [3.4.0] - 2026-01-04  
### Added
* *bayern_sorted.json* was extended by missing parishes (Dekanat Michelau i.OFr)

## [3.3.0] - 2026-01-01  
### Added
* *bayern_sorted.json* was extended by missing parishes

## [3.2.1] - 2025-12-26  
### Added
* bug in *magdeburg_sorted.json* was fixed (Großlehna)

## [3.2.0] - 2025-12-20  
### Added
* *braunschweig_sorted.json* was extended by missing parishes

## [3.1.0] - 2025-12-19  
### Added
* *hannover_sorted.json* was extended by *Kirchenkreis Bodenwerder*, *Kirchenkreis Rotenburg* and *Kirchenkreis Sarstedt*

## [3.0.0] - 2025-12-16  
### Added
* *hannover_sorted.json* was extended by *Kirchenkreis Bockenem-Hoheneggelsen*
  
### Changed
* Processing via Excel was removed
* Logging was introduced

## [2.0.0] - 2025-12-13  
### Added
* *magdeburg_sorted.json* was extended by *Kirchenkreis Erfurt*

### Changed
* GeoJSON update process was fully automated

## [1.10.0] - 2025-12-12  
### Added
* *magdeburg_sorted.json* was extended by *Kirchenkreis Merseburg*

## [1.9.0] - 2025-12-07  
### Added
* *output.py* was extended by write_df_to_geojson function
* *magdeburg_sorted.json* was extended by *Kirchenkreis Mühlhausen*

## [1.8.0] - 2025-12-06  
### Added
* *main.py*, *input.py* and *output.py* were added

## [1.7.0] - 2025-11-27  
### Added
* *trier_sorted.json* was added to reflect *Bistumsarchiv Trier* church book uploads
* *magdeburg_sorted.json* was extended by *Kirchenkreis Halle-Saalkreis* (S-Z)

## [1.6.0] - 2025-11-26  
### Added
* *bayern_sorted.json* was extended by all uploads until 2025-11-25
* geojson sorting.py for alphabetical sorting of GeoJSONs by *district* and *name* property

## [1.5.0] - 2025-11-22  
### Added
* *magdeburg_sorted.json* was extended by *Kirchenkreis Halle-Saalkreis* (Alsleben-Asendorf und Halle Paket 1)
* geojson sorting.py for alphabetical sorting of GeoJSONs by *district* property

## [1.4.0] - 2025-11-20  
### Added
* *magdeburg_sorted.json* was extended by *Kirchenkreis Halle-Saalkreis* (Oberteutschenthal-Rothenburg)

## [1.3.0] - 2025-11-18  
### Added
* *magdeburg_sorted.json* was extended by *Kirchenkreis Halle-Saalkreis* (Maschwitz-Nietleben)

## [1.2.0] - 2025-11-17  
### Added
* *magdeburg_sorted.json* was extended by *Kirchenkreis Halle-Saalkreis* (Döblitz-Lochau), excl. Halle

## [1.1.0] - 2025-11-16  
### Added
* *anhalt_sorted.json* was extended by missing church books of *Kirchenkreis Dessau* and *Kirchenkreis Köthen*
* *magdeburg_sorted.json* was extended by *Kirchenkreis Halle-Saalkreis* (Bebitz-Dobis), excl. Alsleben

## [1.0.0] - 2025-11-15   
### Added
* *anhalt_sorted.json* was extended by missing church books of *Kirchenkreis Ballenstedt* and *Kreis Bernburg*
* *nordkirche_sorted.json* was extended by missing church books of *Kirchenkreis Hamburg-Ost* and *Kirchenkreis Pommern*
* *blieskastel_sorted.json* was added to reflect *Stadtarchiv Blieskastel* church book uploads
### Changed
* sorted GeoJSON were introduced as leading version
* GeoJSONs were sorted by properties *district*

## [0.0.0] - 2025-11-14
Project start


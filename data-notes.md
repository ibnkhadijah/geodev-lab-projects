# Data notes

## GRID3 Nigeria Operational Wards v3.0 (Kano Municipal)
- Source: https://data.grid3.org
- Downloaded: 2026-09-19
- 13 features, polygons
- Columns: ward_name (text), lga_name (text), state (text)
- No nulls in ward_name
- Covers Kano Municipal LGA fully

## OSM Roads, extracted via QuickOSM
- Query: highway=* within Kano Municipal extent
- Extracted: 2026-09-19
- 4,070 features, lines
- Many roads have no surface tag, so paved and unpaved cannot be separated everywhere
- Coverage looks good in the built-up area, sparse at the edges

## OSM Health Facilities, extracted via QuickOSM
- Query: amenity=hospital, clinic, doctors, pharmacy within Kano Municipal extent
- Extracted: 2026-09-19
- 43 features, points
- Coverage looks dense in the city center, but sparse in peripheral wards

## OSM Pharmacies, extracted via QuickOSM
- Query: amenity=pharmacy within Kano Municipal extent
- Extracted: 2026-09-19
- 1 feature, point
- Only one pharmacy mapped, which is a significant gap

## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Kano Municipal LGA, extracted from GRID3 Nigeria Operational Wards v3.0
- 13 wards, all layers clipped to the LGA boundary
- All working layers reprojected to EPSG:32632 (UTM 32N), saved in data/processed/
- Area sanity check: sum of ward polygons ≈ 13.5 km²
- Official Kano Municipal LGA area is ~17 km² (Wikipedia, Towns & Villages)
- Ward polygons cover ~79% of the official LGA area, because GRID3 operational wards are administrative units that do not tile the entire land surface
- Working files in data/processed/, raw files untouched

## Clipping
- Study area: kano_municipal_utm.gpkg (13 wards, EPSG:32632)
- OSM roads clipped to study area, saved as roads_kano_municipal.gpkg
- OSM health facilities clipped to study area, saved as health_kano_municipal.gpkg
- Both clipped layers in EPSG:32632
- Raw unclipped layers preserved in data/raw/

## OSM health facilities, extracted via QuickOSM
- Query: amenity=hospital, clinic, doctors, pharmacy within Kano Municipal extent
- Extracted: 26/09/2026
- 3 features, points: Fuskar Gabas Primary Health Centre, Murtala Mohammed Specialist Hospital, Universal Specialist Hospital
- Completeness: manual check against my own knowledge of Kano suggests at least one or more clinic exists that is not tagged. Assume moderate under-count (roughly 20–30%).
- Currency: most features last edited 26/09/2026; acceptable for a baseline analysis
- Positional accuracy: checked against satellite imagery, points align to buildings
- Attribute accuracy: names and addresses populated for all three; wards mostly filled
- Fitness for purpose: adequate for a coarse straight-line accessibility check; NOT adequate for a comprehensive health coverage analysis
- 

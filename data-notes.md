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
- 15 features, points
- Coverage looks dense in the city center, but sparse in peripheral wards

## OSM Pharmacies, extracted via QuickOSM
- Query: amenity=pharmacy within Kano Municipal extent
- Extracted: 2026-09-19
- 1 feature, point
- Only one pharmacy mapped, which is a significant gap

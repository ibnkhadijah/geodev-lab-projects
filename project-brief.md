# My GeoDev Lab Africa project

## 1. The question
Which wards in Kano Municipal LGA have the lowest accessibility to healthcare facilities within a 15-minute travel time?

## 2. Why it matters
Understanding where healthcare access is poorest helps local health authorities prioritise the construction of new clinics or the improvement of road networks. It also provides a baseline for measuring progress towards universal health coverage in Kano.

## 3. The data I need
- Administrative ward boundaries for Kano Municipal LGA
- Health facility locations
- Road network

## 4. Where each dataset comes from
- **Ward boundaries** – GRID3 – https://data.grid3.org – GeoPackage – (downloaded)
- **Health facilities** – OpenStreetMap via QuickOSM – extracted for Kano Municipal
- **Roads** – OpenStreetMap via QuickOSM – extracted for Kano Municipal
- **Coordinate Reference System:** All datasets will be reprojected to EPSG:32632 (UTM Zone 32N) for accurate distance measurement.

## 5. What I would build
A web map showing access to health facilities for every ward. Currently, this uses straight line distance (a 2km buffer) to approximate a 15-minute walk, with plans to upgrade to a full travel time routing engine in later months. The map will highlight wards where more than 30% of the area is more than 2km away from a clinic.

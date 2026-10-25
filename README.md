# My GeoDev Lab Africa project

# Kano Municipal Healthcare Accessibility
**GeoDev Lab Africa — Cohort One**

## The Question
Which wards in Kano Municipal LGA have the lowest accessibility to healthcare facilities within a 15-minute travel time?

## Project Context
Built over twelve months with GeoDev Lab Africa. See [project-brief.md](./project-brief.md) for the full brief. This project aims to use open spatial data to identify gaps in healthcare access and demonstrate how spatial analysis can support urban planning in Kano.

## Data Sources
- **Ward Boundaries:** GRID3 Nigeria Operational Wards v3.0
- **Health Facilities:** OpenStreetMap (via QuickOSM)
- **Road Network:** OpenStreetMap (via QuickOSM)

## Tools Used
- **GIS:** QGIS
- **Development:** Python, VS Code.

## Project Log
- **Week 1-4:** Data collection, clipping, reprojection (EPSG:32632), and spatial analysis (2km buffer on health facilities). Created an accessibility map.
- **Week 5:** Set up Python, VS Code, and the terminal. `hello.py` runs successfully.
- **Week 6:** set up the project with uv and added pandas. check.py prints the pandas version.
- **Week 7:** analyse.py reads wards.csv, converts each area and classifies each ward.
- **Week 8:** inspect_data.py summarizes the area_km2 column in my Kano data.

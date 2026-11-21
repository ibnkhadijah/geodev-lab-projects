import geopandas as gpd

# Loading the wards GeoPackage layer
# Specifying layer="wards" because a .gpkg can hold multiple layers
wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")

# Printing the first 5 rows
print("--- HEAD ---")
print(wards.head())

# Printing the CRS (Coordinate Reference System)
print("\n--- CRS ---")
print(wards.crs)

# Printing the geometry types (e.g., Polygon, MultiPolygon)
print("\n--- GEOMETRY TYPES ---")
print(wards.geometry.geom_type.value_counts())

# Checking the total bounds (min/max X and Y)
print("\n--- BOUNDS ---")
print(wards.total_bounds)
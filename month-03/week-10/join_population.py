import geopandas as gpd
import pandas as pd

# Loading the data
wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
pop = pd.read_csv("data/raw/ward_population.csv")

# Cleaning the names so they match exactly
# Making everything uppercase and replace hyphens with spaces
wards["join_key"] = wards["ward_name"].str.upper().str.replace("-", " ").str.strip()
pop["join_key"] = pop["ward"].str.upper().str.strip()

# Merging the data
# Joining 'pop' into 'wards' based on the 'join_key'
joined = wards.merge(pop, on="join_key", how="left")

# Checking if it worked
print("--- JOINED DATA ---")
print(joined[["ward_name", "population_2024"]].head())

# Saving the result as a new GeoPackage for the next step
import os
os.makedirs("data/processed", exist_ok=True)
joined.to_file("data/processed/wards_with_pop.gpkg", layer="wards", driver="GPKG")
print("\nSaved to data/processed/wards_with_pop.gpkg")
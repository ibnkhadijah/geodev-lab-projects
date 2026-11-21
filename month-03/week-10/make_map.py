import geopandas as gpd
import matplotlib.pyplot as plt

# Loading the joined GeoPackage we just created
joined = gpd.read_file("data/processed/wards_with_pop.gpkg", layer="wards")

# Setting up the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plotting the data
# Using the column 'population_2024' to color the map
joined.plot(
    column="population_2024", 
    cmap="OrRd",              # Orange-Red color map
    legend=True,              # Adds a color bar
    edgecolor="black",        # Black outlines for wards
    ax=ax
)

# Adding labels
for idx, row in joined.iterrows():
    # Place the text at the center of each polygon
    plt.annotate(
        text=row['ward_name'], 
        xy=(row.geometry.centroid.x, row.geometry.centroid.y),
        horizontalalignment='center',
        fontsize=8
    )

# Adding a title and remove the axis numbers
ax.set_title("Population by Ward (2024)", fontsize=16)
ax.set_axis_off()

# Saving the map as a PNG
plt.savefig("month-03/week-10/population_map.png", dpi=150, bbox_inches="tight")
print("Map saved to month-03/week-10/population_map.png")
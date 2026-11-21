# Week 10: GeoPandas, layers as tables

## What this folder contains
- `explore_pandas.py`: loaded the ward population CSV and filters it.
- `explore_layer.py`: loaded the wards GeoPackage and checks its geometry and CRS.
- `join_population.py`: cleaned the ward names and joins the CSV to the GeoPackage.
- `make_map.py`: plotted the joined data and saves a map.
- `population_map.png`: Generated map.

## How i ranned it
From the repository root:
`uv run month-03/week-10/make_map.py`

## What I found
Agbowo has the highest population (52,300), while Inalende has the lowest (19,800). The color map clearly shows this variation.

## What went wrong and how I fixed it
The "Sabo" ward showed up as NaN (missing) during the join. I fixed it by adding `.str.strip()` to remove the invisible trailing spaces from the names before joining.
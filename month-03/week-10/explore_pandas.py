import pandas as pd

# Loading the CSV into a DataFrame
pop = pd.read_csv("data/raw/ward_population.csv")

# Printing the first 5 rows
print("--- HEAD ---")
print(pop.head())

# Printing the shape (rows, columns)
print("\n--- SHAPE ---")
print(pop.shape)

# Printing the column names
print("\n--- COLUMNS ---")
print(pop.columns)

# Filtering rows where population is greater than 35,000
print("\n--- FILTERED (> 35,000) ---")
big_wards = pop[pop["population_2024"] > 35000]
print(big_wards)
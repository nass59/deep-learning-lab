# Import cars data
import pandas as pd

cars = pd.read_csv('../datasets/cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows():
    print(str(lab) + ": " + str(row['cars_per_cap']))

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)

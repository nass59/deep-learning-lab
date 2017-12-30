# Import cars data
import pandas as pd

cars = pd.read_csv('../datasets/cars.csv', index_col=0)

# Extract drives_right column as Series: dr
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Import numpy as np
import numpy as np

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for height in areas:
    print(height)

# Change for loop to use enumerate()
for index, a in enumerate(areas):
    print("room " + str(index) + ": " + str(a))

# house list of lists
house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50]
]

# Build a for loop from scratch
for a in house:
    print("the " + str(a[0]) + " is " + str(a[1]) + " sqm")

# Definition of dictionary
europe = {
    'spain': 'madrid', 'france': 'paris', 'germany': 'bonn',
    'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'australia': 'vienna'
}

# Iterate over europe
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))

np_baseball = np.array([18.0, 20.0, 10.75, 9.50])

# For loop over np_baseball
for baseball in np.nditer(np_baseball):
    print(str(baseball))

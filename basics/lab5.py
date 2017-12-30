# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
height = [74, 76, 79, 73, 69, 78, 71, 72]
weight = [180, 231, 230, 188, 176, 219, 200, 210]

# Import the numpy package as np
import numpy as np

s = np.array(5)
print(s)

x = s + 3
print(x)
print(x.shape)
print(type(x))

print('-------')
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
print(m.shape)
print('-------')

t = np.array([
    [
        [
            [1], [2]
        ],
        [
            [3], [4]
        ],
        [
            [5], [6]
        ]
    ],
    [
        [
            [7], [8]
        ],
        [
            [9], [10]
        ],
        [
            [11], [12]
        ]
    ],
    [
        [
            [13], [14]
        ],
        [
            [15], [16]
        ],
        [
            [17], [17]
        ]
    ]
])

print(t)
print(t.shape)
print(t[2][1][1][0])
print('-------')

v = np.array([1, 2, 3, 4])
print(v)
print(v.shape)

v2 = v.reshape(1, 4)
print(v2)
print(v2.shape)

v3 = v.reshape(4, 1)
print(v3)
print(v3.shape)
print('-------')

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)
print(np_height.shape)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)

# Create the light array
light = bmi < 25

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Print out the weight at index 50
print(bmi[2])

# Print out sub-array of np_height: index 100 up to and including index 110
print(bmi[3:6])

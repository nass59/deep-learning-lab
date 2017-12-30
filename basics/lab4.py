# Definition of radius
r = 0.43

# Import the math package
from math import pi
from math import exp
from math import radians

# Calculate C
C = 2 * pi * r

# Calculate A
A = pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

expo = 1 / (1 + exp(2))
print(expo)

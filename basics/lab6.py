# Create baseball, a list of lists
baseball = [
    [180, 78.4],
    [215, 102.7],
    [210, 98.5],
    [188, 75.2]
]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print out the 50th row of np_baseball
print(np_baseball[2])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:, 1]
print(np_weight)

# Print out height of 124th player
print(np_baseball[3, 0])

# Create np_height from np_baseball
np_height = np.array(np_baseball[:, 0])

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(['GK', 'M', 'A', 'D'])
np_heights = np.array([191, 184, 185, 180])

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

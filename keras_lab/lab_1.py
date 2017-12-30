import os

import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Activation

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Using TensorFlow 1.0.0; use tf.python_io in later versions
tf.python_io = tf

# Set random seed
np.random.seed(42)

# Our data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).astype('float32')
y = np.array([[0], [1], [1], [0]]).astype('float32')

# One-hot encoding the output
y = np_utils.to_categorical(y)

# Building the model
xor = Sequential()

# Add required layers
xor.add(Dense(32, input_dim=2))

# Add a tanh Activation function
xor.add(Activation('sigmoid'))

# Output layer
xor.add(Dense(2))

# Add a sigmoid Activation function
xor.add(Activation('sigmoid'))

# Specify loss as "binary_crossentropy", optimizer as "adam",
# and add the accuracy metric
xor.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Uncomment this line to print the model architecture
xor.summary()

# Fitting the model
history = xor.fit(X, y, epochs=1000, verbose=1)

# Scoring the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))

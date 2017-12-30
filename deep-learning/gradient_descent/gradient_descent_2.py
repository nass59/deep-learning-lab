import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    """
    # Derivative of the sigmoid function
    """
    return sigmoid(x) * (1 - sigmoid(x))


learnrate = 0.5
x = np.array([1, 2, 3, 4])
y = np.array(0.5)

# Initial weights
w = np.array([0.5, -0.5, 0.3, 0.1])

### Calculate one gradient descent step for each weight
### Note: Some steps have been consilated, so there are
###       fewer variable names than in the above sample code

# TODO: Calculate the node's linear combination of inputs and weights
h = np.dot(w, x)  # Sum of Wx(i)
print(h)

# TODO: Calculate output of neural network
nn_output = sigmoid(h)  # Output Formula
print(nn_output)

# TODO: Calculate error of neural network
error = y - nn_output  # E = y - y_hat

# TODO: Calculate the error term
#       Remember, this requires the output gradient, which we haven't
#       specifically added a variable for.
error_term = error * sigmoid_prime(h)  # Error_term = (y - y_hat) * f'(h)

# TODO: Calculate change in weights
del_w = learnrate * error_term * x  # Delta_wi = learnrate * error_term * x(i)

print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(del_w)

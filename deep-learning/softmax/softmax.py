import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    values = []

    exp_l = np.exp(L)
    sum_exp_l = sum(exp_l)

    for i in exp_l:
        values.append(i / sum_exp_l)

    return values


result = softmax([5, 6, 7])
print(result)


def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)

    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


result = cross_entropy([1, 1, 0], [0.8, 0.7, 0.1])
print(result)

#!/usr/bin/env python3
"""
this function shuffles the data point in two matrices the same way
"""


import numpy as np


def shuffle_data(X, Y):
    """
    this function shuffles the data identically
    """
    m = X.shape[0]
    permutation = np.random.permutation(m)
    X_shuffled = X[permutation]
    Y_shuffled = Y[permutation]

    return X_shuffled, Y_shuffled

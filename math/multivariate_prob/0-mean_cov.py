#!/usr/bin/env python3
"""this function calculates the mean and covariance of a data set"""


import numpy as np

def mean_cov(X):
    """check here all the edge cases as denotes in the requirements"""

    if X is not np.ndarray:
        raise TypeError("C must be a numpy.ndarray")

    if len(X.shape) != 2 or X.shape[0] != X.shape[1] :
        raise ValueError("C must be a 2D square matrix")
    
    mean = np.mean(X, axis=0)
    cov = np.zeros((d, d))
    for i in range(n):
        cov += np.outer((X[i] - mean), (X[i] - mean))
    cov /= (n - 1)
    return mean.reshape(1, d), cov

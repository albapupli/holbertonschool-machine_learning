#!/usr/bin/env python3
"""this function calculates the mean and covariance of a data set"""


import numpy as np

def mean_cov(X):
    """check here all the edge cases as denotes in the requirements"""
    mean = np.mean(X, axis=0)
    cov = np.zeros((d, d))
    for i in range(n):
        cov += np.outer((X[i] - mean), (X[i] - mean))
    cov /= (n - 1)
    return mean.reshape(1, d), cov

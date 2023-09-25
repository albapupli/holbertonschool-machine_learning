#!/usr/bin/env python3
"""
function that initializes all variables required to calculate
the P affinities in t-SNE
"""


import numpy as np


def P_init(X, perplexity):
    """
    p affinities in t sne calculated
    """
    n, d = X.shape

    # Calculate the squared pairwise distance matrix D
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i][j] = np.sum((X[i] - X[j])**2)

    # Initialize P affinities matrix to zeros
    P = np.zeros((n, n))

    # Initialize beta values to 1.0 for all data points
    betas = np.ones((n, 1))

    # Calculate the Shannon entropy H
    H = np.log2(perplexity)

    return D, P, betas, H

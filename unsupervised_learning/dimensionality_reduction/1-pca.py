#!/usr/bin/env python3
"""
a function  that performs PCA on a dataset
"""


import numpy as np


def pca(X, ndim):
    """
    Calculate the covariance matrix of X
    """
    cov_matrix = np.cov(X, rowvar=False)

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Select the top ndim eigenvectors
    top_eigenvectors = eigenvectors[:, :ndim]

    # Compute the transformed data
    T = np.dot(X, top_eigenvectors)

    # Round the values to a reasonable precision
    T = np.round(T, decimals=4)

    return T

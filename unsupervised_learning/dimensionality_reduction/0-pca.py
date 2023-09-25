#!/usr/bin/env python3
"""
a function  that performs PCA on a dataset
"""


import numpy as np


def pca(X, var=0.95):
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

    # Calculate the cumulative explained variance
    explained_variance = np.cumsum(eigenvalues) / np.sum(eigenvalues)

    # Determine the number of components to keep to maintain var fraction of variance
    n_components = np.argmax(explained_variance >= var) + 1

    # Select the top n_components eigenvectors
    top_eigenvectors = eigenvectors[:, :n_components]

    # Compute the weights matrix
    weights_matrix = top_eigenvectors

    return weights_matrix

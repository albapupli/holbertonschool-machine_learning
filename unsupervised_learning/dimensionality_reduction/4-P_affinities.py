#!/usr/bin/env python3
"""
a function that calculates the symmetric P affinities of a data set
"""


import numpy as np
P_init = __import__('2-P_init').P_init
HP = __import__('3-entropy').HP


def binary_search_beta(Di, target_entropy, tol=1e-5):
    """
    do a binary search beta
    """
    low = 1e-10
    high = None
    beta = 1.0

    # Perform binary search on beta
    for _ in range(200):
        H, Pi = HP(Di, beta)
        H_diff = H - target_entropy

        if abs(H_diff) < tol:
            return beta, Pi

        if H_diff > 0:
            high = beta if high is None else min(beta, high)
            beta = (beta + low) / 2.0
        else:
            low = beta if low is None else max(beta, low)
            if high is None:
                beta *= 2.0
            else:
                beta = (beta + high) / 2.0

    # If we didn't converge, return the last calculated Pi
    return beta, Pi

def P_affinities(X, tol=1e-5, perplexity=30.0):
    n, d = X.shape
    P = np.zeros((n, n))

    for i in range(n):
        Di, _, betas, _ = P_init(X, perplexity)
        target_entropy = np.log2(perplexity)
        beta, Pi = binary_search_beta(Di[i], target_entropy, tol=tol)
        P[i, :] = Pi

    # Make P symmetric
    P = (P + P.T) / (2 * n)

    return P

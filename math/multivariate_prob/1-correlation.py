#!/usr/bin/env python3
"""this function calculates a correlation matrix"""


def correlation(C):
    """
    Calculates a correlation matrix
    """
    if type(C) is not np.ndarray:
        raise TypeError("C must be a numpy.ndarray")
    if (len(C.shape) != 2) or (C.shape[0] != C.shape[1]):
        raise ValueError("C must be a 2D square matrix")
    D = np.sqrt(np.diag(C))
    D_inverse = 1 / np.outer(D, D)
    corr = D_inverse * C
    return corr

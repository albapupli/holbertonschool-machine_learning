#!/usr/bin/env python3
"""function to concat matrices"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concat two matrices"""
    return np.concatenate((mat1, mat2), axis=axis)

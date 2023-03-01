#!/usr/bin/env python3
"""function concat two matrices"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concat two matrices"""
    return (np.matmul(mat1, mat2)) # mat1.matmul(mat2)

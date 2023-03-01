#!/usr/bin/env python3
"""function to concat matrices"""


import numpy as np
def cat_matrices2D(mat1, mat2, axis=0):
    """concat matrices"""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        return None
    return result

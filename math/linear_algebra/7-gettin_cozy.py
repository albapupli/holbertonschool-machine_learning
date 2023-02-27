#!/usr/bin/env python3
"""function to concat matrices"""


import numpy as np
def cat_matrices2D(mat1, mat2, axis=0):
    """concat matrices"""
    return np.concatenate((mat1,mat2),axis)

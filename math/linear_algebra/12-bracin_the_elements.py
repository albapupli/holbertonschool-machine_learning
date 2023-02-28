#!/usr/bin/env python3
"""find element wise of a matrix"""


import numpy as np
def np_elementwise(mat1, mat2):
    """add subtr mul div matrices"""
    return np.add(mat1, mat2), np.subtract(mat1, mat2), np.multiply(mat1, mat2), np.divide(mat1, mat2)

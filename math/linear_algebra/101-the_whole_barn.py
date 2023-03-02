#!/usr/bin/env python3
"""function to add two matrices"""


def add_matrices(mat1, mat2):
    """ returns new matrix that is sum of two matrices added element-wise """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    if len(matrix_shape(mat1)) == 1:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    return [add_matrices(mat1[i], mat2[i]) for i in range(len(mat1))]

#!/usr/bin/env python3
"""function to add two matrices together"""


def add_matrices2D(mat1, mat2):
    """add matrices"""
    row = len(mat1)
    col = len(mat1[0])
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    sum = [[mat1[i][j] + mat2[i][j] for j in range(row)] for i in range(col)]
    return sum

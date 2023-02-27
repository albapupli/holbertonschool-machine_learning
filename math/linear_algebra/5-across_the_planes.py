#!/usr/bin/env python3
"""function to add two matrices together"""


def add_matrices2D(mat1, mat2):
    """add matrices"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    sum = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1))] for i in range(len(mat1[0]))]
    return sum

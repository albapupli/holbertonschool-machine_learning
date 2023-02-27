#!/usr/bin/env python3
"""function to add 2 matrices"""

def add_matrices2D(mat1, mat2):
    """add matrices"""
    row = len(mat1)
    col = len(mat1[0])
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    sum = []
    for j in range(row):
        for i in range(col):
            sum.append(mat1[i][j] + mat2[i][j])
    return sum

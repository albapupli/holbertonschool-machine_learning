#!/usr/bin/env python3
"""function that returns the transpose of a matrix"""


def matrix_transpose(matrix):
    """transpose the matrix"""
    row = len(matrix)
    col = len(matrix[0])
    result = [[matrix[j][i] for j in range(row)] for i in range(col)]
    return result

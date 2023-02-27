#!/usr/bin/env python3
"""function to concat arr"""


def cat_arrays(arr1, arr2):
    """concat 2 arrays"""
    result = []
    for i in range(len(arr2)):
        result.append(arr2[i])
    return result

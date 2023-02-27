#!/usr/bin/env python3
"""function to add two arrays together"""


def add_arrays(arr1, arr2):
"""add 2 arrays together"""
    if len(arr1) != len(arr2):
        return None
    sum = [arr1[i] + arr2[i] for i in range(len(arr1))]
    return sum

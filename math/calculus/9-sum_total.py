#!/usr/bin/env python3
"""function to calculate summation notation"""


def summation_i_squared(n):
    """sum of n consecutive nr"""
    if type(n) != int or n < 1:
        return None
    return (int)(n*(n+1)*(2*n+1)/6)

#!/usr/bin/env python3
"""function to calculate summation notation"""


def summation_i_squared(n):
    """sum of n consecutive nr"""
    if (n==0):
        return 0;
    return n*n + summation_i_squared(n-1)
        

#!/usr/bin/env python3
"""function to calculate the derivative of a function"""


def poly_derivative(poly):
    """calculate the der"""
    der = []
    for i in range(1, len(poly)):
        der.append(poly[i] * i)
    return der

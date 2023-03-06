#!/usr/bin/env python3
"""function to calculate the derivative of a function"""


def poly_derivative(poly):
    """calculate the der"""
    if type(poly) is not list or poly == []:
        return None
    elif len(poly) < 2:
        return [0]
    der = []
    for i in range(1, len(poly)):
        der.append(poly[i] * i)
    return der

#!/usr/bin/env python3
"""function to calculate integral of a polynomial"""


def poly_integral(poly, C=0):
    """calculate integral of poly"""
    integral = []
    integral.append(0)
    for i in range(0, len(poly)):
        integral.append(poly[i] / (i+1))
    return integral

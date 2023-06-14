#!/usr/bin/env python3
"""
this function calculates the weighted moving avg of dataset
"""


def moving_average(data, beta):
    """
    moving avg of dataset
    """
    v = 0
    EMA = []
    for i in range(len(data)):
        v = ((v * beta) + ((1 - beta) * data[i]))
        EMA.append(v / (1 - (beta ** (i + 1))))
    return EMA

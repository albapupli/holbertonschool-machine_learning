#!/usr/bin/env python3
"""
function that calculates the Shannon entropy and P affinities relative to a data point
"""


import numpy as np


def HP(Di, beta):
    """
    Calculate the unnormalized P affinities
    """
    unnormalized_Pi = np.exp(-beta * Di)

    # Calculate the Shannon entropy Hi
    sum_unnormalized_Pi = np.sum(unnormalized_Pi)
    Hi = np.log(sum_unnormalized_Pi) + beta * np.sum(Di * unnormalized_Pi) / sum_unnormalized_Pi

    # Normalize the P affinities Pi
    Pi = unnormalized_Pi / sum_unnormalized_Pi

    return Hi, Pi

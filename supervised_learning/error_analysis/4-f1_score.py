#!/usr/bin/env python3
"""
calculates the F1 score of a confusion matrix
"""


import numpy as np


def f1_score(confusion):
    # Calculate the precision and sensitivity for each class
    p = precision(confusion)
    r = sensitivity(confusion)

    # Calculate the F1 score for each class
    f1 = 2 * p * r / (p + r)
    f1 = np.nan_to_num(f1, nan=0)  # Handle division by zero

    return f1

#!/usr/bin/env python3
"""
calculates the precision for each class in a confusion matrix
"""


import numpy as np


def precision(confusion):
    """
    calculating the precision in a confusion matrix
    """
    tp = np.diag(confusion)
    fp = np.sum(confusion, axis=0) - tp
    precision = tp / (tp + fp)

    return precision

#!/usr/bin/env python3
"""
this function calculates the sensitivity for each class in a confusion matrix
"""

import numpy as np


def sensitivity(confusion):
    """
    calculating the sensitivity in the confusion matrix
    """
    tp = np.diag(confusion)
    fn = np.sum(confusion, axis=1) - tp
    tpr = tp / (tp + fn)
    
    return tpr

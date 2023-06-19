#!/usr/bin/env python3
"""
this function creates a confusion matrix
"""


import numpy as np


def create_confusion_matrix(labels, logits):
    """
    creating a confusion matrix
    """
    return np.matmul(labels.transpose(), logits)

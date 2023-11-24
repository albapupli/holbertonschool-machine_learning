#!/usr/bin/env python3
"""
Creates a Pandas DataFrame from a numpy library using ndarray
"""


import pandas as pd
import numpy as np
import string


def from_numpy(array):
    """
    Creates a Pandas DataFrame from a numpy.ndarray.
    """
    if array.shape[1] > 26:
        raise ValueError("Input array has more than 26 columns.")

    column_labels = list(string.ascii_uppercase)[:array.shape[1]]
    df = pd.DataFrame(array, columns=column_labels)
    return df
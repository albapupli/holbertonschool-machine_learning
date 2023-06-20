#!/usr/bin/env python3
"""
this function converts a label vector into a one-hot matrix
"""


import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    convert a label vector into one hot matrix
    """
    one_hot = K.utils.to_categorical(labels, num_classes=classes)
    return one_hot

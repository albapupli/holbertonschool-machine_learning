#!/usr/bin/env python3
"""
these functions save and load a models weights
"""


import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """
    saves a models weights
    """
    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """
    loads a models weights
    """
    network.load_weights(filename)
    return None

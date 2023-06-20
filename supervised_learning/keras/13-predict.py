#!/usr/bin/env python3
"""
this function makes a prediction using a neural network
"""


import tensorflow.keras as K


def predict(network, data, verbose=False):
    """
    predicting using nn
    """
    prediction = network.predict(x=data,
                                 verbose=verbose)
    return prediction

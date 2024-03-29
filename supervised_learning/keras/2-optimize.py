#!/usr/bin/env python3
"""
this function sets up Adam optimization for a keras
model with categorical crossentropy loss and accuracy metrics
"""


import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """
    adam optimizer for keras model
    """
    network.compile(optimizer=K.optimizers.Adam(lr=alpha,
                                                beta_1=beta1,
                                                beta_2=beta2),
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

    return None

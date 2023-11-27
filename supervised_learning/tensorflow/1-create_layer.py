#!/usr/bin/env python3
"""
Defines a function to create a layer for neural network
"""


import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """
    a function that create layers
    :param prev: the tensor output of the previous layer
    :param n: the number of nodes in the layer to create
    :param activation: is the activation function that the layer should use
    :return: the tensor output of the layer
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, activation=activation, kernel_initializer=init,
                            name="layer")
    return layer(prev)

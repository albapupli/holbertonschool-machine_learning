#!/usr/bin/env python3
"""
this function creates a training operation for nn
using Adam optimization alg
"""


import tensorflow as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """
    training operation of nn using Adam opt
    """
    optimizer = tf.keras.optimizers.Adam(
        learning_rate=alpha,
        beta_1=beta1,
        beta_2=beta2,
        epsilon=epsilon)
    return optimizer.minimize(loss)

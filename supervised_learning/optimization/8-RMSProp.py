#!/usr/bin/env python3
"""
this function creates the training operation for nn in tf
using RMSProp optimization alg
"""


import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    training operation using RMSProp opt
    """
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha,
                                          decay=beta2, epsilon=epsilon)
    train_op = optimizer.minimize(loss)
    return train_op

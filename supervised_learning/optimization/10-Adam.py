#!/usr/bin/env python3
"""
this function creates a training operation for nn
using Adam optimization alg
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


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
    update a var in place using Adam opt
    """
    v_dW = (beta1 * v) + ((1 - beta1) * grad)
    s_dW = (beta2 * s) + ((1 - beta2) * (grad ** 2))
    v_dW_c = v_dW / (1 - (beta1 ** t))
    s_dW_c = s_dW / (1 - (beta2 ** t))
    var -= alpha * (v_dW_c / (epsilon + (s_dW_c ** (1 / 2))))
    return var, v_dW, s_dW


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

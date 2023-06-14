#!/usr/bin/env python3
"""
this function creates the training operation for a
neural network in tf using gradient descent with momentum
optimization alg
"""


import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """
    training operation of nn with tf
    """
    optimizer = tf.train.MomentumOptimizer(alpha, momentum=beta1)
    train_op = optimizer.minimize(loss)
    return train_op

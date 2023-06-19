#!/usr/bin/env python3
"""
this function  creates a learning rate decay
operation in tensorflow using inverse time decay
"""


import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    updating learning rate via reverse time decay
    """
    updated_alpha = alpha / (1 + decay_rate * (global_step // decay_step))
    return updated_alpha


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    creating learning rate decay via inverse
    time decay in tf
    """
    alpha_new = tf.divide(alpha, tf.pow(1 + decay_rate * tf.floor_div(
                                        global_step, decay_step), 1))
    return alpha_new

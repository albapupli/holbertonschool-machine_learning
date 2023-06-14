#!/usr/bin/env python3
"""
this function calculates the weighted moving avg of dataset
"""


import numpy as np
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
   
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha, decay=beta2, epsilon=epsilon)
    train_op = optimizer.minimize(loss)
    return train_op

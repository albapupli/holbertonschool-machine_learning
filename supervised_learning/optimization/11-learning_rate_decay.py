#!/usr/bin/env python3
"""
this function updates the learning rate using inverse time decay in numpy
"""


import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    updating learning rate via reverse time decay
    """
    updated_alpha = alpha / (1 + decay_rate * (global_step // decay_step))
    return updated_alpha

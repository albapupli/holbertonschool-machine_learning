#!/usr/bin/env python3
"""
this function updates a var using gradient descent with
momentum optimization alg
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    updating a var using gradient descent with momentum optimization
    """
    dW_prev = (beta1 * v) + ((1 - beta1) * grad)
    var -= (alpha * dW_prev)
    return var, dW_prev

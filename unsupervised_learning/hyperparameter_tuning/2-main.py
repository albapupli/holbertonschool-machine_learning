#!/usr/bin/env python3

GP = __import__('2-gp').GaussianProcess
import numpy as np

"""
Based on 1-gp.py, update the class GaussianProcess:

Public instance method def update(self, X_new, Y_new): that updates a Gaussian Process:
X_new is a numpy.ndarray of shape (1,) that represents the new sample point
Y_new is a numpy.ndarray of shape (1,) that represents the new sample function value
Updates the public instance attributes X, Y, and K
"""

def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    gp = GP(X_init, Y_init, l=0.6, sigma_f=2)
    X_new = np.random.uniform(-np.pi, 2*np.pi, 1)
    print('X_new:', X_new)
    Y_new = f(X_new)
    print('Y_new:', Y_new)
    gp.update(X_new, Y_new)
    print(gp.X.shape, gp.X)
    print(gp.Y.shape, gp.Y)
    print(gp.K.shape, gp.K)
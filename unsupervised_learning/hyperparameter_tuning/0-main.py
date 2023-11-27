#!/usr/bin/env python3

GP = __import__('0-gp').GaussianProcess
import numpy as np
"""
Create the class GaussianProcess that represents a noiseless 1D Gaussian process:

Class constructor: def __init__(self, X_init, Y_init, l=1, sigma_f=1):

X_init is a numpy.ndarray of shape (t, 1) representing the inputs already sampled with the black-box function
Y_init is a numpy.ndarray of shape (t, 1) representing the outputs of the black-box function for each input in X_init
t is the number of initial samples
l is the length parameter for the kernel
sigma_f is the standard deviation given to the output of the black-box function
Sets the public instance attributes X, Y, l, and sigma_f corresponding to the respective constructor inputs
Sets the public instance attribute K, representing the current covariance kernel matrix for the Gaussian process
Public instance method def kernel(self, X1, X2): that calculates the covariance kernel matrix between two matrices:

X1 is a numpy.ndarray of shape (m, 1)
X2 is a numpy.ndarray of shape (n, 1)
the kernel should use the Radial Basis Function (RBF)
Returns: the covariance kernel matrix as a numpy.ndarray of shape (m, n)
"""

def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    gp = GP(X_init, Y_init, l=0.6, sigma_f=2)
    print(gp.X is X_init)
    print(gp.Y is Y_init)
    print(gp.l)
    print(gp.sigma_f)
    print(gp.K.shape, gp.K)
    print(np.allclose(gp.kernel(X_init, X_init), gp.K))
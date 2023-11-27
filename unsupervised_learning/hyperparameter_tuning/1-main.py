#!/usr/bin/env python3

GP = __import__('1-gp').GaussianProcess
import numpy as np

"""
Based on 0-gp.py, update the class GaussianProcess:

Public instance method def predict(self, X_s): that predicts the mean and standard deviation of points in a Gaussian process:
X_s is a numpy.ndarray of shape (s, 1) containing all of the points whose mean and standard deviation should be calculated
s is the number of sample points
Returns: mu, sigma
mu is a numpy.ndarray of shape (s,) containing the mean for each point in X_s, respectively
sigma is a numpy.ndarray of shape (s,) containing the variance for each point in X_s, respectively
"""
def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    gp = GP(X_init, Y_init, l=0.6, sigma_f=2)
    X_s = np.random.uniform(-np.pi, 2*np.pi, (10, 1))
    mu, sig = gp.predict(X_s)
    print(mu.shape, mu)
    print(sig.shape, sig)
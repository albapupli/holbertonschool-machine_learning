#!/usr/bin/env python3

"""
Create the class BayesianOptimization that performs Bayesian optimization on a noiseless 1D Gaussian process:

Class constructor def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1, sigma_f=1, xsi=0.01, minimize=True):
f is the black-box function to be optimized
X_init is a numpy.ndarray of shape (t, 1) representing the inputs already sampled with the black-box function
Y_init is a numpy.ndarray of shape (t, 1) representing the outputs of the black-box function for each input in X_init
t is the number of initial samples
bounds is a tuple of (min, max) representing the bounds of the space in which to look for the optimal point
ac_samples is the number of samples that should be analyzed during acquisition
l is the length parameter for the kernel
sigma_f is the standard deviation given to the output of the black-box function
xsi is the exploration-exploitation factor for acquisition
minimize is a bool determining whether optimization should be performed for minimization (True) or maximization (False)
Sets the following public instance attributes:
f: the black-box function
gp: an instance of the class GaussianProcess
X_s: a numpy.ndarray of shape (ac_samples, 1) containing all acquisition sample points, evenly spaced between min and max
xsi: the exploration-exploitation factor
minimize: a bool for minimization versus maximization
You may use GP = __import__('2-gp').GaussianProcess
"""


GP = __import__('2-gp').GaussianProcess
BO = __import__('3-bayes_opt').BayesianOptimization
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    bo = BO(f, X_init, Y_init, (-np.pi, 2*np.pi), 50, l=2, sigma_f=3, xsi=0.05)
    print(bo.f is f)
    print(type(bo.gp) is GP)
    print(bo.gp.X is X_init)
    print(bo.gp.Y is Y_init)
    print(bo.gp.l)
    print(bo.gp.sigma_f)
    print(bo.X_s.shape, bo.X_s)
    print(bo.xsi)
    print(bo.minimize)
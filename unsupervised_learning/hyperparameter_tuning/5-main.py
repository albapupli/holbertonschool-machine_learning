
"""
Based on 4-bayes_opt.py, update the class BayesianOptimization:

Public instance method def optimize(self, iterations=100): that optimizes the black-box function:
iterations is the maximum number of iterations to perform
If the next proposed point is one that has already been sampled, optimization should be stopped early
Returns: X_opt, Y_opt
X_opt is a numpy.ndarray of shape (1,) representing the optimal point
Y_opt is a numpy.ndarray of shape (1,) representing the optimal function value
"""

#!/usr/bin/env python3

BO = __import__('5-bayes_opt').BayesianOptimization
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    bo = BO(f, X_init, Y_init, (-np.pi, 2*np.pi), 50, l=0.6, sigma_f=2)
    X_opt, Y_opt = bo.optimize(50)
    print('Optimal X:', X_opt)
    print('Optimal Y:', Y_opt)
    print('All sample inputs:', bo.gp.X)
#!/usr/bin/env python3
"""this class is multinormal class"""


import numpy as np


class MultiNormal:
    """this is the class construction with one parameter"""
    def __init__(self, data):
        """
        the construction method
        """
        if type(data) is not np.ndarray or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        n, d = data.shape
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")
        self.mean, self.cov = mean_cov(data.T)
        self.mean = self.mean.reshape(-1, 1)

    def pdf(self, x):
        """
        return teh pdf
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if x.shape[0] != 1 or x.shape[1] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        test_d, one = x.shape
        if test_d != d or one != 1:
            raise ValueError("x must have the shape ({}, 1)".format(d))
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        pdf = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)
        mult = np.matmul(np.matmul((x - self.mean).T, inv), (x - self.mean))
        pdf *= np.exp(-0.5 * mult)
        pdf = pdf[0][0]
        return pdf

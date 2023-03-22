#!/usr/bin/env python3
"""this function performs a valid convolution on grayscale img"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images
    """
    m, height, width = images.shape
    kh, kw = kernel.shape
    # in valid, the kernel does not extend beyond the borders
    convoluted = np.zeros((m, height - kh + 1, width - kw + 1))
    for h in range(height - kh + 1):
        for w in range(width - kw + 1):
            output = np.sum(images[:, h: h + kh, w: w + kw] * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = output
        return convoluted

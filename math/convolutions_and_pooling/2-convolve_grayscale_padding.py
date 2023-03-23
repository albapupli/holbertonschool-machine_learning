#!/usr/bin/env python3
"""this funct performs a convolution on grayscale img with custom padding"""


import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images with custom padding
    """
    m, height, width = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant',
                    constant_values=0)

    # (2 * ph) because left-right / top-bottom
    ch = height + (2 * ph) - kh + 1
    cw = width + (2 * pw) - kw + 1

    convoluted = np.zeros((m, ch, cw))

    for h in range(ch):
        for w in range(cw):
            output = np.sum(images[:, h: h + kh, w: w + kw] * kernel,
                            axis=1).sum(axis=1)
            convoluted[:, h, w] = output
    return convoluted

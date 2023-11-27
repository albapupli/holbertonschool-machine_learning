#!/usr/bin/env python3

"""
Write a function def pca_color(image, alphas): that performs PCA color augmentation as described in the AlexNet paper:

image is a 3D tf.Tensor containing the image to change
alphas a tuple of length 3 containing the amount that each channel should change
Returns the augmented image
"""

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import numpy as np
pca_color = __import__('100-pca').pca_color

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(100)
np.random.seed(100)
doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
for image, _ in doggies.shuffle(10).take(1):
    alphas = np.random.normal(0, 0.1, 3)
    plt.imshow(pca_color(image, alphas))
    plt.show()
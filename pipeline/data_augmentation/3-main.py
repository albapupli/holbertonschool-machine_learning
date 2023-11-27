#!/usr/bin/env python3

"""
Write a function def shear_image(image, intensity): that randomly shears an image:

image is a 3D tf.Tensor containing the image to shear
intensity is the intensity with which the image should be sheared
Returns the sheared image
"""

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
shear_image = __import__('3-shear').shear_image

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(3)

doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
for image, _ in doggies.shuffle(10).take(1):
    plt.imshow(shear_image(image, 50))
    plt.show()
#!/usr/bin/env python3

"""
Write a function def change_brightness(image, max_delta): that randomly changes the brightness of an image:

image is a 3D tf.Tensor containing the image to change
max_delta is the maximum amount the image should be brightened (or darkened)
Returns the altered image
"""

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
change_brightness = __import__('4-brightness').change_brightness

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(4)

doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
for image, _ in doggies.shuffle(10).take(1):
    plt.imshow(change_brightness(image, 0.3))
    plt.show()
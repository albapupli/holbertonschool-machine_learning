#!/usr/bin/env python3

"""
Write a function def crop_image(image, size): that performs a random crop of an image:

image is a 3D tf.Tensor containing the image to crop
size is a tuple containing the size of the crop
Returns the cropped image
"""

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
crop_image = __import__('1-crop').crop_image

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(1)

doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
for image, _ in doggies.shuffle(10).take(1):
    plt.imshow(crop_image(image, (200, 200, 3)))
    plt.show()
#!/usr/bin/env python3

"""
Write a function def autoencoder(input_dims, filters, latent_dims): that creates a convolutional autoencoder:

input_dims is a tuple of integers containing the dimensions of the model input
filters is a list containing the number of filters for each convolutional layer in the encoder, respectively
the filters should be reversed for the decoder
latent_dims is a tuple of integers containing the dimensions of the latent space representation
Each convolution in the encoder should use a kernel size of (3, 3) with same padding and relu activation, followed by max pooling of size (2, 2)
Each convolution in the decoder, except for the last two, should use a filter size of (3, 3) with same padding and relu activation, followed by upsampling of size (2, 2)
The second to last convolution should instead use valid padding
The last convolution should have the same number of filters as the number of channels in input_dims with sigmoid activation and no upsampling
Returns: encoder, decoder, auto
encoder is the encoder model
decoder is the decoder model
auto is the full autoencoder model
The autoencoder model should be compiled using adam optimization and binary cross-entropy loss
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

autoencoder = __import__('2-convolutional').autoencoder

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3)
print(x_train.shape)
print(x_test.shape)
np.random.seed(0)
tf.set_random_seed(0)
encoder, decoder, auto = autoencoder((28, 28, 1), [16, 8, 8], (4, 4, 8))
auto.fit(x_train, x_train, epochs=50, batch_size=256, shuffle=True,
                validation_data=(x_test, x_test))
encoded = encoder.predict(x_test[:10])
print(np.mean(encoded))
reconstructed = decoder.predict(encoded)[:,:,:,0]

for i in range(10):
    ax = plt.subplot(2, 10, i + 1)
    ax.axis('off')
    plt.imshow(x_test[i,:,:,0])
    ax = plt.subplot(2, 10, i + 11)
    ax.axis('off')
    plt.imshow(reconstructed[i])
plt.show()
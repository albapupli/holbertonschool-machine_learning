#!/usr/bin/env python3
"""
this function also train the model with learning rate decay
"""


import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True, shuffle=False):
    """
    train the model with learning rate decay:
    """
    callback = []

    if early_stopping and validation_data:
        callback.append(
            K.callbacks.EarlyStopping(monitor='loss', patience=patience))

    def learning_rate(epoch):

        return (alpha / (1 + decay_rate * epoch))

    if learning_rate_decay and validation_data:
        callback.append(
            K.callbacks.LearningRateScheduler(learning_rate, verbose=1))

    if callback == []:
        callback = None

    history = network.fit(x=data, y=labels,
                          batch_size=batch_size,
                          epochs=epochs,
                          validation_data=validation_data,
                          callbacks=callback,
                          verbose=verbose,
                          shuffle=shuffle)
    return history

import numpy as np
import tensorflow as tf
def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    optimizer = tf.keras.optimizers.Adam(
        learning_rate=alpha, 
        beta_1=beta1, 
        beta_2=beta2, 
        epsilon=epsilon)
    return optimizer.minimize(loss)
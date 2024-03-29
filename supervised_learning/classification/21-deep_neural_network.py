#!/usr/bin/env python3
"""deep neural networks class"""


import numpy as np


class DeepNeuralNetwork:
    """
    class that represents a deep neural network
    performing binary classification
    """

    def __init__(self, nx, layers):

        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or len(layers) < 1:
            raise TypeError("layers must be a list of positive integers")

        weights = {}
        previous = nx

        for index, layer in enumerate(layers, 1):

            if type(layer) is not int or layer < 0:
                raise TypeError("layers must be a list of positive integers")

            weights["b{}".format(index)] = np.zeros((layer, 1))
            weights["W{}".format(index)] = (np.random.randn(layer, previous)
                                            * np.sqrt(2 / previous))
            previous = layer

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = weights

    @property
    def L(self):
        return (self.__L)

    @property
    def cache(self):
        return (self.__cache)

    @property
    def weights(self):
        return (self.__weights)

    def forward_prop(self, X):
        """
        foward propagation guesses the output
        """

        self.__cache["A0"] = X

        for index in range(self.L):
            W = self.weights["W{}".format(index + 1)]
            b = self.weights["b{}".format(index + 1)]

            z = np.matmul(W, self.cache["A{}".format(index)]) + b
            A = 1 / (1 + (np.exp(-z)))

            self.__cache["A{}".format(index + 1)] = A

        return (A, self.cache)

    def cost(self, Y, A):
        """
        calculates the cost of the model using logistic regression function:
        """
        m = Y.shape[1]
        m_loss = np.sum((Y * np.log(A)) + ((1 - Y)
                        * np.log(1.0000001 - A)))
        cost = (1 / m) * (-(m_loss))
        return (cost)

    def evaluate(self, X, Y):
        """
        evaluates the neuron's predictions
        """
        A, cache = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return (prediction, cost)

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
        calculates one pass of gradient descent on the neuron
        derivative of loss function with respect to A:
            dA = (-Y / A) + ((1 - Y) / (1 - A))
        derivative of A with respect to z:
            dz = A * (1 - A)
        combining two above with chain rule,
        derivative of loss function with respect to z:
            dz = A - Y
        using chain rule with above derivative,
        derivative of loss function with respect to __W:
            d__W = Xdz
        derivative of loss function with respect to __b:
            d__b = dz
        one-step of gradient descent updates the attributes with the following:
            __W = __W - (alpha * d__W)
            __b = __b - (alpha * d__b)
        """
        m = Y.shape[1]
        back = {}

        for index in range(self.L, 0, -1):

            A = cache["A{}".format(index - 1)]

            # checks if the current layer is the output layer
            if index == self.L:
                # the derivative of the cost with respect to the
                # output activations A
                # is computed as A - Y
                back["dz{}".format(index)] = (cache["A{}".format(index)] - Y)
            else:
                # compute derivative w.r.t the activations
                # of the previous layer
                # retrieve derivative w.r.t the activations
                # of the current layer+1
                dz_prev = back["dz{}".format(index + 1)]
                # retrieve the activations of the current layer
                A_current = cache["A{}".format(index)]
                # compute the derivative of the cost with
                # respect to the activations
                back["dz{}".format(index)] = (
                    np.matmul(W_prev.transpose(), dz_prev) *
                    (A_current * (1 - A_current)))

            # compute the gradients of the weights and biases of a layer
            # during backpropagation
            # dz is the error of the current layer
            dz = back["dz{}".format(index)]
            # dW is the gradient of the weights
            dW = (1 / m) * (np.matmul(dz, A.transpose()))
            # db is the gradient of the biases, along the m axis
            db = (1 / m) * np.sum(dz, axis=1, keepdims=True)

            W_prev = self.weights["W{}".format(index)]

            self.__weights["W{}".format(index)] = (
                self.weights["W{}".format(index)] - (alpha * dW))

            self.__weights["b{}".format(index)] = (
                self.weights["b{}".format(index)] - (alpha * db))

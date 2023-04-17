#!/usr/bin/env python3
"""class of neural networks"""


import numpy as np


class NeuralNetwork:
    """
    class that represents a neural network with one hidden layer
    performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        class constructor
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0

        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return (self.__W1)

    @property
    def b1(self):
        return (self.__b1)

    @property
    def A1(self):
        return (self.__A1)

    @property
    def W2(self):
        return (self.__W2)

    @property
    def b2(self):
        return (self.__b2)

    @property
    def A2(self):
        return (self.__A2)

    def forward_prop(self, X):
        """
        calculates the forward propagation of the neural network
        """

        z1 = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + (np.exp(-z1)))

        z2 = np.matmul(self.W2, self.__A1) + self.b2
        self.__A2 = 1 / (1 + (np.exp(-z2)))

        return (self.A1, self.A2)

        def cost(self, Y, A):
            """
            calculates the cost of the model using logistic regression
            In binary classification, the output layer has a single node 
            that represents the probability of the positive class. 
            Thus, the cost function is calculated based on the output of this node 
            (i.e., A) and the actual labels (i.e., Y).
            """
            m = Y.shape[1]
            m_loss = np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A)))
            cost = (1 / m) * (=(m_loss))
            return (cost)

import numpy as np


class NeuralNetwork:
    def __init__(self, layer1, layer2, lr):
        self.weights1 = np.random.normal(size=(layer1, layer2), scale = 0.01)
        self.weights2 = np.random.normal(size=(layer2, 1), scale = 0.01)
        self.bias1 = np.zeros(shape=(1, layer2))
        self.bias2 = np.zeros(shape=(1, 1))
        self.lr = lr


    def feedforward(self, x):
        self.input = x
        self.layer1 = self.sigmoid(np.dot(x, self.weights1) + self.bias1)
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2) + self.bias2)


    def sigmoid(self, Z):
        return 1/(1+np.exp(-Z))


    def sigmoid_derivative(self, Z):
        s = 1/(1+np.exp(-Z))
        temp = s * (1-s)
        return temp


    def Loss(self, y_actual):
        self.y = y_actual.reshape(-1, 1)
        self.loss = y_actual - self.output
        

    def backprop(self):

        error_output = (self.y - self.output) * self.sigmoid_derivative(self.output)
        error_output = error_output / len(error_output)
        d_weights2 = np.dot(self.layer1.T, error_output)
        d_weights1 = np.dot(self.input.T,  (np.dot(error_output, self.weights2.T) * self.sigmoid_derivative(self.layer1)))

        d_bias2 = error_output.sum()
        d_bias1 = (np.dot(error_output, self.weights2.T) * self.sigmoid_derivative(self.layer1)).sum(axis = 0)
		
        self.weights1 = self.weights1 + d_weights1 * self.lr
        self.weights2 = self.weights2 + d_weights2 * self.lr

        self.bias1 = self.bias1 + d_bias1 * self.lr
        self.bias2 = self.bias2 + d_bias2 * self.lr



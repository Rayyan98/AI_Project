from NN import NeuralNetwork as nn
import pandas as pd

df = pd.read_csv('mnist_test.csv')

labels = df.iloc[:,0].to_numpy()

data = df.iloc[:, 1:].to_numpy()
ind = int(0.7 * len(data))

labels = labels == 5
trainX = data[:ind]
testX = data[ind:]
trainY = labels[:ind]
testY = labels[ind:]

def iiter(data, labels, n):
    for i in range(0, len(data), n):
        d = data[i: min(len(data), i + n)]
        l = labels[i: min(len(data), i + n)]
        yield d,l


def error(y, y_pred):
    return ((y - y_pred) ** 2).mean()


def accuracy(y, y_pred):
	pred = y_pred >= 0.5
	a = (pred == y).mean()
	return a


lr = 0.3
inp = 28 * 28
hidden = 500
epoch = 10
batch_size = 16

n = nn(inp, hidden, lr)

for i in range(epoch):
	for X,y in iiter(trainX, trainY, batch_size):
		n.feedforward(X)
		n.Loss(y)
		n.backprop()

	n.feedforward(trainX)
	print("train\t", error(trainY, n.output))
	n.feedforward(testX)
	print("test\t", error(testY, n.output))
	print("accuracy: \t", accuracy(testY, n.output))



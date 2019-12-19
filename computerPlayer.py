from alphabeta import AlphaBeta
from hueristic import heuristic
from NN import NeuralNetwork


class computerPlayer:
	def __init__(self, depth):
		self.depth = depth
		
		# self.heuristic = heuristic
		
		n = NeuralNetwork(64, 10, 0.003)
		n.readfile()
		self.heuristic = n.heuristic
		
		
	def makeMove(self, state):
		move = AlphaBeta(state, self.depth, self.heuristic)
		return state.applyMoveChain(move)


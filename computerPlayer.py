from alphabeta import AlphaBeta


class computerPlayer:
	def __init__(self, depth):
		self.depth = depth
		
	def makeMove(self, state):
		move = AlphaBeta(state, self.depth)
		return state.applyMoveChain(move)


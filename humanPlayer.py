import time

class humanPlayer:
	def __init__(self, pipe):
		self.pipe = pipe
		
	
	def makeMove(self, state):
		poss_moves = state.getActualPossMoves()
		possMoves = state.allSeqPositions()
		while not self.pipe.ready:
			time.sleep(0.01)
		move = self.pipe.move
		self.pipe.ready = False
		move = [list(map(int, i.split(","))) for i in move.split(" ")]
		while move not in possMoves:
			while not self.pipe.ready:
				time.sleep(0.01)
			move = self.pipe.move
			self.pipe.ready = False
			move = [list(map(int, i.split(","))) for i in move.split(" ")]
		m = possMoves.index(move)
		return state.applyMoveChain(poss_moves[m])



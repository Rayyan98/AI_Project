class humanPlayer:
	def __init__(self):
		pass
		
	
	def makeMove(self, state):
		poss_moves = state.getActualPossMoves()
		possMoves = state.allSeqPositions()
		print(possMoves)
		move = input()
		move = [list(map(int, i.split(","))) for i in move.split(" ")]
		while move not in possMoves:
			move = input()
			move = [i.split(",") for i in move.split(" ")]
		m = possMoves.index(move)
		return state.applyMoveChain(poss_moves[m])



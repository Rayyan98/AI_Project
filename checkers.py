from checkersState import checkersState
from computerPlayer import computerPlayer


class checkers:

	def __init__(self, startState = []):
		if not startState:
			startState = [  [ 0, -1,  0, -1,  0, -1,  0, -1],
							[-1,  0, -1,  0, -1,  0, -1,  0],
							[ 0, -1,  0, -1,  0, -1,  0, -1],
							[ 0,  0,  0,  0,  0,  0,  0,  0],
							[ 0,  0,  0,  0,  0,  0,  0,  0],
							[ 1,  0,  1,  0,  1,  0,  1,  0],
							[ 0,  1,  0,  1,  0,  1,  0,  1],
							[ 1,  0,  1,  0,  1,  0,  1,  0]    ]
		
		self.currentState = checkersState(startState)
		self.p1 = computerPlayer(1)
		self.p2 = computerPlayer(2)


	def forceSetState(self, state):
		self.currentState = checkersState(state)


	def singleLoop(self):
		turn = 1

		print(self.currentState)

		while self.currentState.hasEnded() == 0:
			if turn % 2 == 1:
				self.currentState = self.p1.makeMove(self.currentState)
			else:
				self.currentState = self.p2.makeMove(self.currentState.invert()).invert()

			turn += 1
			print(self.currentState)

		print(turn)



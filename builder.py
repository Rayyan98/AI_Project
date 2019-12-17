from checkers import checkers
from computerPlayer import computerPlayer

class DataBuilder(checkers):
	
	def __init__(self, startState = []):
		super(DataBuilder, self).__init__(computerPlayer(3), computerPlayer(3), startState)
		self.states = dict()
		self.initState = self.currentState.state.copy().asnumpy().tolist()
		
		
	def makeIter(self, n):
		
		total_turns = 0
		for i in range(n):
			currentStates = dict()
			self.forceSetState(self.initState)
			if self.currentState not in currentStates:
				currentStates[self.currentState] = [0, 1]
			else:
				currentStates[self.currentState][1] += 1
			while self.singleMove():
				if self.currentState not in currentStates:
					currentStates[self.currentState] = [0, 1]
				else:
					currentStates[self.currentState][1] += 1
			if self.currentState.hasEnded() == 1:
				for j in currentStates:
					currentStates[j][0] = currentStates[j][1]
			for j in currentStates:
				if j not in self.states:
					self.states[j] = currentStates[j]
				else:
					self.states[j][0] += currentStates[j][0]
					self.states[j][1] += currentStates[j][1]
			total_turns += self.turn
		print(total_turns)
		print(len(self.states))
				
				



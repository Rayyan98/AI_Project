from mxnet import ndarray as nd
import random


class checkersState:

	def __init__(self, state):
		self.state = nd.array(state).astype(int)
		self.moveMap = nd.array([[-1,-1], [-1, 1], [1, 1], [1, -1],
								 [-2,-2], [-2, 2], [2, 2], [2, -2]]).astype(int)
		self.moveChains = []

    
	def getPossMoves(self):
		state = self.state
		lower, upper = [], []
		pos = nd.zeros(shape = 2).astype(int)

		for i in range(state.shape[0]):
			for j in range(state.shape[1]):
				pos[:] = [i,j]
				if state[i, j] > 0:
					if i - 1 >= 0 and j - 1 >= 0 and state[i - 1, j - 1] == 0:
						lower.append([pos.copy(), 1])
					elif i - 2 >= 0 and j - 2 >= 0 and state[i - 2, j- 2] == 0 and state[i- 1, j - 1] < 0:
						upper.append([pos.copy(), 5])
					if i - 1 >= 0 and j + 1 <= 7 and state[i - 1, j + 1] == 0:
						lower.append([pos.copy(), 2])
					elif i - 2 >= 0 and j + 2 <= 7 and state[i - 2, j + 2] == 0 and state[i - 1, j + 1] < 0:
						upper.append([pos.copy(), 6])
				if state[i, j] > 1:
					if i + 1 <= 7 and j - 1 >= 0 and state[i + 1, j - 1] == 0:
						lower.append([pos.copy(), 4])
					elif i + 2 <= 7 and j - 2 >= 0 and state[i + 2, j - 2] == 0 and state[i + 1, j - 1] < 0:
						upper.append([pos.copy(), 8])                    
					if i + 1 <= 7 and j + 1 <= 7 and state[i + 1, j + 1] == 0:
						lower.append([pos.copy(), 3])
					elif i + 2 <= 7 and j + 2 <= 7 and state[i + 2, j + 2] == 0 and state[i + 1, j + 1] < 0:
						upper.append([pos.copy(), 7])                    
		
		random.shuffle(lower)
		random.shuffle(upper)
		return lower, upper


	def applyMove(self, move):
		state = self.state.copy()
		pos, m_val = move
		m = self.moveMap[m_val - 1, :]
		target = m + pos
		state[pos[0], pos[1]], state[target[0], target[1]] = state[target[0], target[1]], state[pos[0], pos[1]]

		if m_val >= 4:
			mid = m/2 + pos
			state[mid[0], mid[1]] = 0
			
		if target[0] == 0 and abs( state[target[0], target[1]].asscalar() ) == 1:
			state[target[0], target[1]] = state[target[0], target[1]] * 3
		
		return checkersState(state)


	def hasEnded(self):
		state = self.state
		if (state < 0).sum() == 0:
			return 1
		if (state > 0).sum() == 0:
			return -1
		if len(self.getPossMoves()) == 0:
			return -1
		return 0


	def invert(self):
		state = self.state.copy()
		state = state * -1
		state = state.flip(axis = 0)
		state = state.flip(axis = 1)
		return checkersState(state)


	def getActualPossMoves(self):
		if self.moveChains:
			return self.moveChains
		lower, upper = self.getPossMoves()
		if not upper:
			self.moveChains = [[i] for i in lower]
			return self.moveChains
		else:
			result_states = [self.applyMove(i) for i in upper]
			upper_moves = [[i] for i in upper]
			ind = 0
			while ind < len(result_states):
				new_lower, new_upper = result_states[ind].getPossMoves()
				if not new_upper:
					ind += 1
				else:
					new_result_states = [result_states[ind].applyMove(i) for i in new_upper]
					result_states[ind] = new_result_states.pop()
					result_states.extend(new_result_states)
					cache = new_upper.pop()
					upper_moves.extend([upper_moves[ind] + [i] for i in new_upper])
					upper_moves[ind].append(cache)
			assert len(result_states) == len(upper_moves)
			random.shuffle(upper_moves)
			self.moveChains = upper_moves
			return self.moveChains


	def applyMoveChain(self, moveChain):
		state = self
		for i in moveChain:
			state = state.applyMove(i)
		return state


	def __str__(self):
		return self.state.__str__()
		
		
		

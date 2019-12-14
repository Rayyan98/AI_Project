def heuristic(state):
    return ((state.state > 0).sum() - (state.state < 0).sum()).asscalar()
	

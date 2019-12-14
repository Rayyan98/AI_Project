import random

def heuristic(state):
    return ((state > 0).sum() - (state < 0).sum()).asscalar()
    
    

from mxnet import ndarray as nd
from alphabeta import *
import time
import random


class gans:

    def __init__(self):
        self.states = dict()
        self.moveMap = nd.array([   [-1,-1], [-1, 1], [1, 1], [1, -1], 
                                    [-2,-2], [-2, 2], [2, 2], [2, -2]  ]).astype(int)
    
    
    def getPossMoves(self, state):
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
   

    def applyMove(self, state, move):
        state = state.copy()
        pos, m_val = move
        m = self.moveMap[m_val - 1, :]
        target = m + pos
        state[pos[0], pos[1]], state[target[0], target[1]] = state[target[0], target[1]], state[pos[0], pos[1]]

        if m_val >= 4:
            mid = m/2 + pos
            state[mid[0], mid[1]] = 0
            
        if target[0] == 0 and abs( state[target[0], target[1]].asscalar() ) == 1:
            state[target[0], target[1]] = state[target[0], target[1]] * 3
        
        return state


    def hasEnded(self, state):
        if (state < 0).sum() == 0:
            return 1
        if (state > 0).sum() == 0:
            return -1
        if len(self.getPossMoves(state)) == 0:
            return -1
        return 0


    def invert(self, state):
        state = state * -1
        state = state.flip(axis = 0)
        state = state.flip(axis = 1)
        return state


    def getActualPossMoves(self, state):
        lower, upper = self.getPossMoves(state)
        if not upper:
            return [[i] for i in lower]
        else:
            result_states = [self.applyMove(state, i) for i in upper]
            upper_moves = [[i] for i in upper]
            ind = 0
            while ind < len(result_states):
                new_lower, new_upper = self.getPossMoves(result_states[ind])
                if not new_upper:
                    ind += 1
                else:
                    new_result_states = [self.applyMove(result_states[ind], i) for i in new_upper]
                    result_states[ind] = new_result_states.pop()
                    result_states.extend(new_result_states)
                    cache = new_upper.pop()
                    upper_moves.extend([upper_moves[ind] + [i] for i in new_upper])
                    upper_moves[ind].append(cache)
            assert len(result_states) == len(upper_moves)
            random.shuffle(upper_moves)
            return upper_moves


    def applyMoveChain(self, state, moveChain):
        for i in moveChain:
            state = self.applyMove(state, i)
        return state


    def makeMove(self, state, depth):
        # moves = self.getActualPossMoves(state)
        # state[:, :] = self.applyMoveChain(state, moves[0])
        # return 
        move = AlphaBeta(self, state, depth)
        state[:, :] = self.applyMoveChain(state, move)
    

    def compareMoveChain(self, moveChain, moveChain2):
        if len(moveChain2) != len(moveChain):
            return False
        for k,j in zip(moveChain, moveChain2):
            if ((k[0] != j[0]).sum() > 0) or k[1] != j[1]:
                return False
        return True


    def getUserMove(self, state):
        moveChain = [[nd.array([int(a[0]), int(a[1])]).astype(int), int(a[2])] for a in input("Enter move ").split()]
        for i in self.getActualPossMoves(state):
            if self.compareMoveChain(moveChain, i):
                state[:, :] = self.applyMoveChain(state, moveChain)
                return
        self.getUserMove(state)
        
    
    def userPlay(self, state):
        turn = 1
        print(state)

        while self.hasEnded(state) == 0:
            if turn % 2 == 1:
                self.getUserMove(state)
            else:
                print("Waiting for computer ... ")
                self.makeMove(state, 3)
                print(self.invert(state))            
            state = self.invert(state)            
            turn += 1

        if turn % 2 == 1:
            final_state = state
        else:
            final_state = self.invert(state)
        print(final_state)
        if self.hasEnded(final_state) == -1:
            print('loss')
        else:
            print('win')
        print(turn, len(self.states))


    def singleLoop(self, state):
        turn = 1

        while self.hasEnded(state) == 0:
            if turn % 2 == 1:
                print(state)
            else:
                print(self.invert(state))
            
            self.makeMove(state, 7)
            
            state = self.invert(state)            
            turn += 1

        if turn % 2 == 1:
            final_state = state
        else:
            final_state = self.invert(state)

        print(final_state)

        if self.hasEnded(final_state) == -1:
            print('loss')
        else:
            print('win')

        print(turn, len(self.states))


print("Starting ... ")

startState = [  [ 0, -1,  0, -1,  0, -1,  0, -1],
                [-1,  0, -1,  0, -1,  0, -1,  0],
                [ 0, -1,  0, -1,  0, -1,  0, -1],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 1,  0,  1,  0,  1,  0,  1,  0],
                [ 0,  1,  0,  1,  0,  1,  0,  1],
                [ 1,  0,  1,  0,  1,  0,  1,  0]    ]
                
startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0, -1,  0,  0,  0,  0,  0],
                [ 0,  1,  0,  0,  0,  0,  0,  0],
                [ 0,  0, -1,  0, -1,  0,  0,  0],
                [ 0,  1,  0,  1,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0, -1,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  3,  0, -1,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  3,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [-3,  0,  0,  0,  0,  0,  0,  0]    ]

startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0, -1,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  3],
                [ 0,  0,  0,  0, -1,  0,  1,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0, -1,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  3],
                [ 0,  0,  0,  0, -1,  0,  1,  0],
                [ 0,  0,  0, -1,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0]    ]


startState = nd.array(startState).astype(int)

g = gans()

for i in range(30):
    print('current iter is ', i)
    g.singleLoop(startState)
    break


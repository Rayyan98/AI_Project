import hueristic

def AlphaBeta(gan, state, depth):
    return minimax(gan, state, depth, float('-inf'), float('inf'), True, depth)


def minimax(gan, state, depth, alpha, beta, maximizingPlayer, max_depth): #position is the starting point, depth is of tree, mP is a boolean

    if depth == 0 or gan.hasEnded(state) != 0:
        a = hueristic.heuristic(state) * [-1, 1][maximizingPlayer] * 1000 - (max_depth - depth)
        return a

    if maximizingPlayer:
        for i in gan.getActualPossMoves(state):
            num = minimax(gan, gan.invert(gan.applyMoveChain(state, i)), depth-1, alpha, beta, False, max_depth)
            if num > alpha:
                alpha = num
                if max_depth == depth:
                    arg = i    
            if beta <= alpha:
                break
        if max_depth == depth:
            return arg
        return alpha

    else:
        for i in gan.getActualPossMoves(state):
            num = minimax(gan, gan.invert(gan.applyMoveChain(state, i)), depth-1, alpha, beta, True, max_depth)
            beta = min(beta,num)
            if beta <= alpha:
                break
        return beta

     

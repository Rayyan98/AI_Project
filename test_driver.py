from checkers import checkers
from computerPlayer import computerPlayer
from humanPlayer import humanPlayer
from builder import DataBuilder


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
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0, -3,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 3,  0,  0,  0,  0,  0,  0,  0]    ]

# startState = [  [ 0,  3,  0,  0,  0,  0,  0,  0],
                # [ 1,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0, -3,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0, -3,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0, -3,  0, -3,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

# startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0, -1,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  3],
                # [ 0,  0,  0,  0, -1,  0,  1,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

# startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0, -1,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  3],
                # [ 0,  0,  0,  0, -1,  0,  1,  0],
                # [ 0,  0,  0, -1,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

# startState = [  [ 0, -1,  0, -1,  0, -1,  0,  0],
                # [-1,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  1,  0,  0,  0,  0],
                # [ 0,  0,  1,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

# startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0, -1,  0,  0,  0,  0,  0,  0],
                # [ 0,  0,  0,  0,  0,  0,  0,  0],
                # [ 0, -1,  0, -1,  0,  0,  0,  0],
                # [ 0,  0,  1,  0,  0,  0,  0,  0]    ]


print("Starting ... ")

c = checkers(humanPlayer(), computerPlayer(3))
c.singleLoop()

# g = DataBuilder()
# g.buildMoreData(500)


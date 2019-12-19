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

startState = [  [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0, -1,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  3],
                [ 0,  0,  0,  0, -1,  0,  1,  0],
                [ 0,  0,  0, -1,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0]    ]

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

c = checkers(computerPlayer(3), computerPlayer(3), startState)
c.singleLoop()

# g = DataBuilder()
# g.buildMoreData(500)


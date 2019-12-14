import numpy as np
import matplotlib.pyplot as plt

cheakers_board = np.zeros((8,8))
cheakers_board[1::2, 0::2] = 1
cheakers_board[0::2, 1::2] = 1

plt.imshow(cheakers_board, cmap = 'binary')
plt.show()

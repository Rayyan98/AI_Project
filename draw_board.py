import sys, pygame, threading
from checkers import checkers
from computerPlayer import computerPlayer


done = True

def makeTheMove(checkers):
	global done
	checkers.singleMove()
	done = True


pygame.init()

black = 0, 0, 0

height = 600

board = pygame.image.load("board.jpg")
board_rect = board.get_rect()
act_height = board_rect[-1]
new_width = board_rect[-2] * height // act_height
board_rect[-2:] = new_width, height

screen = pygame.display.set_mode(board_rect[-2:])

board = pygame.image.load("board.jpg").convert()
board = pygame.transform.scale(board, board_rect[-2:])

black = pygame.image.load("piece_black.png").convert_alpha()
white = pygame.image.load("piece_white.png").convert_alpha()
black_rect = black.get_rect()
white_rect = white.get_rect()

black_h = black_rect[-1] * height // act_height
white_h = white_rect[-1] * height // act_height
black_w = black_rect[-2] * height // act_height
white_w = white_rect[-2] * height // act_height

black_rect[-2:] = black_w, black_h
white_rect[-2:] = white_w, white_h

black = pygame.transform.scale(black, black_rect[-2:])
white = pygame.transform.scale(white, white_rect[-2:])

start_pos = 70
start_pos = start_pos * height / act_height

dist = 85
dist = dist * height / act_height

c = checkers(computerPlayer(3), computerPlayer(3))

screen.blit(board, board_rect)
pygame.display.flip()

t = threading.Thread(target = makeTheMove, args = (c,))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.blit(board, board_rect)

	if done:
		state = c.getState()
		done = False
		t = threading.Thread(target = makeTheMove, args = (c,))
		t.start()
		
	for i in range(state.shape[0]):
		for j in range(state.shape[1]):
			if state[i][j] > 0:
				temp_rect = white_rect.copy()
				temp_rect.x = dist * j + start_pos
				temp_rect.y = dist * i + start_pos
				screen.blit(white, temp_rect)
			elif state[i][j] < 0:
				temp_rect = black_rect.copy()
				temp_rect.x = dist * j + start_pos
				temp_rect.y = dist * i + start_pos
				screen.blit(black, temp_rect)				
			
	pygame.display.flip()


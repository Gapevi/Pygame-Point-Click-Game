import pygame
pygame.init()

from Game import Game

# Set up the game window
screen_width, screen_height = 1280, 720 #800*1.8, 600*1.3
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point 'n' Click Game")

running = True
clock = pygame.time.Clock()

game = Game(screen=screen, debug=True)


game.ready()

# Game loop
while running:

	running = game.run()

#	Gets time since last frame
	delta_time = clock.tick(60) / 1000
# 	clamps Game.delta_time between 0.001 and 0.1
	game.delta_time = max(0.001, min(delta_time, 0.1))

#   Updates game_surface
	pygame.display.flip()

pygame.quit()
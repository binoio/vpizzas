# Importing pygame library.  Import tells Python what to include.
import pygame
from pygame import *

# Initialize pygame.  This is the behind the scenes setup.
# Object.method(no arguments)
pygame.init()

# Define constants.
# To Do: Create a variable for the window width here.
# To Do: Create a variable for the window height here.
# To Do: Create a variable for the window resolution here.

# This creates the game window.
# Constants get uppercase.
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
WINDOW_RESOLUTION = (WINDOW_WIDTH, WINDOW_HEIGHT)
# To Do: Replace the argument in the set_mode method below.
GAME_WINDOW = display.set_mode(WINDOW_RESOLUTION)
# To Do: Add window caption here

display.set_caption('Attack of the Vampire Pizzas!')

# ------------------------------------------------------------------------------


# Start main game loop.
game_running = True

while game_running:
# Check for events.
	for event in pygame.event.get():
		# Exit loop on quit.
		if event.type == QUIT:
			game_running = False
	display.update()
# End of main game loop.
#------------------------------------------------------------------------------
# Clean up game.
pygame.quit()
"""
A Level Editor for Yozaka.

Can be used for other 2D platformer games as well.
"""

import pygame

# IMPORT FUNCTIONS FROM THE UTILS SCRIPT
from utils import load_image, load_images

# IMPORT SYS MODULE
import sys

# LEVEL EDITOR CLASS RUNS THE LEVEL EDITOR LOOP
class LevelEditor:
	def __init__(self) -> None:
		pygame.init()

		# SET UP PYGAME WINDOW
		pygame.display.set_caption("Yozaka Level Editor")

		self.WIDTH = 1800
		self.HEIGHT = 900
		self.TILE_SIZE = 50

		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.fps = 60
		self.clock = pygame.time.Clock()

		"""
		CREATE PIXEL ART EFFECT:
			RENDER ASSETS ONTO SMALLER DISPLAY (SMALLER RESOLUTION),
			SCALE IT UP TO THE SCREEN (LARGER RESOLUTION)
		"""
		self.PIXEL_WIDTH = 320
		self.PIXEL_HEIGHT = 240
		self.display = pygame.Surface((self.PIXEL_WIDTH, self.PIXEL_HEIGHT))

		self.level = [[0 for _ in range(18)] for _ in range(7)]
		self.level.append([2 for _ in range(10)])
		self.level.append([1 for _ in range(10)])

		# LOAD GAME ASSETS
		# DEFINE IMAGES USED FOR VARIOUS ENTITIES AND OBJECTS
		self.assets = {
			'decor': load_images('tiles/decor'),
			'grass': load_images('tiles/grass'),
			'large_decor': load_images('tiles/large_decor'),
			'stone': load_images('tiles/stone'),
			'player': load_image('entities/player.png')
		}

	def run(self):
		while True:
			# COLOR OF THE SKY
			self.display.fill((114, 116, 248))

			"""
			GET INPUT:
				pygame.event.get():
					GET INPUT BY INTERACTING WITH OS
			"""
			for event in pygame.event.get():
				"""
				WHEN EVENT TYPE IS pygame.quit():
					CLOSE GAME WINDOW
				"""
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()


			"""
			THE BLIT FUNCTION COPIES A SECTION OF MEMORY
			ONTO ANOTHER SURFACE.

			IN PYGAME, A SURFACE IS AN IMAGE.
			THE WINDOW'S SURFACE IS THE SCREEN.
			IT IS ASPECIAL TYPE OF SURFACE.
			
			MOST SURFACES ARE AN IMAGE LOCATED IN MEMORY.

			YOU CAN BLIT ANY SURFACE ONTO ANY SURFACE.
			IT IS LIKE MAKING A COLLAGE OF IMAGES.

			SCALE():
				SCALE DISPLAY SURFACE
				ONTO THE SIZE OF THE SCREEN SURFACE
				REGARDLESS OF SIZE
			"""
			self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

			# UPDATE DISPLAY
			pygame.display.update()

			# FORCE LOOP TO RUN AT 60 FPS
			self.clock.tick(self.fps)


# RUN THE LEVEL EDITOR CLASS
LevelEditor().run()
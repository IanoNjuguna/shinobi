"""
A Level Editor for a 2D platformer game.
"""

import pygame

# IMPORT FUNCTIONS FROM THE UTILS SCRIPT
from utils import load_image, load_images

# IMPORT THE PHYSICS ENTITY OBJECT FROM THE ENTITIES SCRIPT
from entities import PhysicsEntity

# IMPORT THE TILEMAP OBJECT FROM THE TILEMAP SCRIPT
from tilemap import Tilemap

# IMPORT SYS MODULE
import sys

# LEVEL EDITOR CLASS RUNS THE LEVEL EDITOR LOOP
class LevelEditor:
	def __init__(self) -> None:
		pygame.init()

		# SET UP PYGAME WINDOW
		pygame.display.set_caption("Level Editor")

		self.WIDTH = 640
		self.HEIGHT = 480
		self.TILE_SIZE = 16

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

		"""
		self.level = [[0 for _ in range(20)] for _ in range(30)]
		self.level.append([2 for _ in range(20)])
		self.level.append([1 for _ in range(20)])

		# LOAD GAME ASSETS
		# DEFINE IMAGES USED FOR VARIOUS ENTITIES AND OBJECTS
		self.assets = {
			'decor': load_images('tiles/decor'),
			'grass': load_images('tiles/grass'),
			'large_decor': load_images('tiles/large_decor'),
			'stone': load_images('tiles/stone'),
			'clouds': load_images('clouds'),
		}

		self.tiles = [
			"",
			self.assets['decor'],
			self.assets['grass'],
			self.assets['large_decor'],
			self.assets['stone'],
		]

	
	def draw_board(self, board):
		for q in range(len(board)):
			for p in range(len(board[q])):
				if board[q][p] != 0:
					value = board[q][p]
					if 0 < value <= 6:
						self.screen.blit(self.tiles[value], (p * self.TILE_SIZE, q * self.TILE_SIZE))
					elif value == 7:
							self.screen.blit(self.tiles[value], (p * self.TILE_SIZE, q * self.TILE_SIZE - 10))
		"""

	def run(self):

			# COLOR OF THE SKY
			self.display.fill((14, 219, 248))

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
			pygame.display.flip()

			#draw_board(board)

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
Level_Editor = LevelEditor().run()

LevelEditor


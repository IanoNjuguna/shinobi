"""
IMPORT PYGAME MODULE

COORDINATES SYSTEM IN PYGAME:
	TOP-LEFT IS (0, 0)
"""
import pygame

# IMPORT SYS MODULE
import sys

# IMPORT FUNCTIONS FROM THE UTILS SCRIPT
from game_scripts.utils import load_image, load_images

# IMPORT THE PHYSICS ENTITY OBJECT FROM THE ENTITIES SCRIPT
from game_scripts.entities import PhysicsEntity

# IMPORT THE TILEMAP OBJECT FROM THE TILEMAP SCRIPT
from game_scripts.tilemap import Tilemap

# THIS GAME OBJECT RUNS THE GAME LOOP
class Game:
	def __init__(self) -> None:
		# INITIALIZE THE PYGAME MODULE
		pygame.init()

		# GIVE NAME TO WINDOW
		pygame.display.set_caption('Yozaka Ninja')

		# CREATE A WINDOW (USING PYGAME)
		self.WIDTH = 640
		self.HEIGHT = 480
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

		"""
		CREATE PIXEL ART EFFECT:
			RENDER ASSETS ONTO SMALLER DISPLAY (SMALLER RESOLUTION),
			SCALE IT UP TO THE SCREEN (LARGER RESOLUTION)
		"""
		self.PIXEL_WIDTH = 320
		self.PIXEL_HEIGHT = 240
		self.display = pygame.Surface((self.PIXEL_WIDTH, self.PIXEL_HEIGHT))

		# PURPOSE OF CLOCK IS TO FORCE THE GAME TO RUN AT 60FPS
		self.clock = pygame.time.Clock()
		self.fps = 60

		# MOVEMENT VARIABLE
		self.movement = [False, False]

		# DEFINE IMAGES USED FOR VARIOUS ENTITIES AND OBJECTS
		self.assets = {
			'decor': load_images('tiles/decor'),
			'grass': load_images('tiles/grass'),
			'large_decor': load_images('tiles/large_decor'),
			'stone': load_images('tiles/stone'),
			'player': load_image('entities/player.png')
		}

		# INITIALIZE PHYSICS ENTITY OBJECT IN MAIN GAME SCRIPT
		self.player = PhysicsEntity(self, 'player', (50, 50), (8,15))

		# INITIALIZE TILEMAP OBJECT IN MAIN GAME SCRIPT
		self.tilemap = Tilemap(self, tile_size = 16)

	# GAME LOOP
	def run(self):
		while True:
			# COLOR OF THE SKY
			self.display.fill((114, 116, 248))

			# RENDER THE TILEMAP BEHIND THE PLAYER ENTITY
			self.tilemap.render(self.display)

			# UPDATE THE PLAYER ENTITY'S POSITION
			self.player.update((self.movement[1] - self.movement[0], 0))
			
			# RENDER THE PLAYER ENTITY'S NEW POSITION ONTO A NEW FRAME
			self.player.render(self.display)

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
				WHEN EVENT TYPE IS A BUTTON PRESS:
					BIND SPECIFIC KEYS
				"""
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT or event.key == pygame.K_d:
						self.movement[0] = True
					if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
						self.movement[1] = True
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_d:
						self.movement[0] = False
					if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
						self.movement[1] = False

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

			# FORCE LOOP TO RUN AT 60FPS
			self.clock.tick(self.fps)

# RUN GAME
Game().run()


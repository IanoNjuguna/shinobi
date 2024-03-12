import pygame

from sys import exit

from game_scripts.utils import load_image
from game_scripts.entities import PhysicsEntity

class Game:
	def __init__(self) -> None:
		pygame.init()

		pygame.display.set_caption('yozaka')
		self.screen = pygame.display.set_mode((640, 480))
		self.display = pygame.Surface((320, 240))

		self.clock = pygame.time.Clock()

		self.movement = [False, False]

		self.assets = {
			'player': load_image('entities/player.png')
		}

		self.player = PhysicsEntity(self, 'player', (50, 50), (8,15))

	def run(self):
		while True:
			self.display.fill((114, 116, 248))

			self.player.update((self.movement[1] - self.movement[0], 0))
			self.player.render(self.display)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
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

			self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
			pygame.display.update()
			self.clock.tick(60)

Game().run()
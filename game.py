from sys import exit
import pygame

class Game:
	def __init__(self) -> None:
		pygame.init()


		pygame.display.set_caption('yozaka')
		self.screen = pygame.display.set_mode((640,480))

		self.clock = pygame.time.Clock()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			pygame.display.update()
			self.clock.tick(60)

Game().run()
import pygame

# PhysicsEntity OBJECT HANDLES GAME PHYSICS
class PhysicsEntity:
	def __init__(self, game, e_type, pos, size):
		# ANYTHING IN THE GAME IS ACCESSIBLE BY ENTITY
		self.game = game
		# ENTITY TYPE
		self.type = e_type
		# POSITION TO SPAWN ENTITY
		self.pos = list(pos)
		# SIZE OF ENTITY
		self.size = size
		# RATE OF CHANGE IN POSITION ENTITY
		self.velocity = [0, 0]

	# UPDATE MOVEMENT IN EVERY FRAME
	def update(self, movement = (0, 0)):
		# DETERMINE HOW MUCH MOVEMENT TO MAKE IN A FRAME
		frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

		# MOVE ENTITY
		self.pos[0] += frame_movement[0] # X-AXIS
		self.pos[1] += frame_movement[1] # Y-AXIS

	# RENDER ENTITY'S MOVEMENT ONTO THE SURFACE
	def render(self, surf):
		# BLIT THE NEW ENTITY POSITION ONTO THE SURFACE OF THE NEW FRAME
		surf.blit(self.game.assets['player'], self.pos)


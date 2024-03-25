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
		# CHECK FOR COLLISIONS
		self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

	def rect(self):
		return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

	# UPDATE MOVEMENT IN EVERY FRAME
	def update(self,  tilemap, movement = (0, 0)):
		# DETERMINE HOW MUCH MOVEMENT TO MAKE IN A FRAME
		frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

		# DETERMINE DIRECTION OF COLLISIONS
		self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

		# MOVE ENTITY IN THE X-AXIS
		self.pos[0] += frame_movement[0]		
		# CHECK FOR COLLISIONS IN THE X-AXIS
		entity_rect = self.rect()
		for rect in tilemap.physics_rects_around(self.pos):
			if entity_rect.colliderect(rect):
				# CHECK FOR COLLISION ON THE RIGHT
				if frame_movement[0] > 0:
					entity_rect.right = rect.left
					self.collisions['right'] = True
				# CHECK FOR COLLISION ON THE LEFT
				if frame_movement[0] < 0: 
					entity_rect.left = rect.right
					self.collisions['left'] = True

				self.pos[0] = entity_rect.x

		# MOVE ENTITY IN THE Y-AXIS
		self.pos[1] += frame_movement[1] # Y-AXIS
		# CHECK FOR COLLISIONS IN THE Y-AXIS
		for rect in tilemap.physics_rects_around(self.pos):
			if entity_rect.colliderect(rect):
				# CHECK FOR COLLISION ON THE BOTTOM
				if frame_movement[0] > 0:
					entity_rect.bottom = rect.top
					self.collisions['down'] = True
				#CHECK FOR COLLISIONS ON THE TOP
				if frame_movement[1] < 0:
					entity_rect.top = rect.bottom
					self.collisions['up'] = True

				self.pos[1] = entity_rect.y

		# ADD IN-GAME GRAVITY
		self.velocity[1] = min(5, self.velocity[1] + 0.1) # MODIFY THE VELOCITY OF THE Y-AXIS

		if self.collisions['down'] or self.collisions['up']:
			self.velocity[1] = 0

	# RENDER ENTITY'S MOVEMENT ONTO THE SURFACE
	def render(self, surf):
		# BLIT THE NEW ENTITY POSITION ONTO THE SURFACE OF THE NEW FRAME
		surf.blit(self.game.assets['player'], self.pos)


import pygame

# LOOKS UP THE 9 TILES CLOSE TO THE PLAYER'S POSITION TO RUN COLLISIONS
NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

PHYSICS_TILES = {'grass', 'stone'}

# TILEMAP OBJECT HANDLES THE PLACEMENT OF TILES IN THE GAME
class Tilemap:
	def __init__(self, game, tile_size=16):
		self.game = game
		self.tile_size = tile_size

		"""
		EVERY SINGLE TILE ON THE GRID.
		IT IS CONVENIENT TO HANDLE PHYSICS
		WITH ON-GRID TILES.
		"""
		self.tilemap = {}

		# EVERY TILE OFF THE GRID
		self.offgrid_tiles = []

		# CREATE ON-GRID TILES
		for i in range(10):
			self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
			self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

	def tiles_around(self, pos):
		tiles = []
		tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
		for offset in NEIGHBOUR_OFFSETS:
			check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
			if check_loc in self.tilemap:
				tiles.append(self.tilemap[check_loc])
		return tiles

	def physics_rects_around(self, pos):
		rects = []
		for tile in self.tiles_around(pos):
			if tile['type'] in PHYSICS_TILES:
				rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
		return rects

	# RENDER OFF-GRID && ON-GRID TILES
	def render(self, surf):
		for tile in self.offgrid_tiles:
			surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

		for loc in self.tilemap:
			tile = self.tilemap[loc]
			surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))


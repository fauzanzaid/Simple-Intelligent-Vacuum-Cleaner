#! /usr/bin/python2

import random

class Env(object):
	"""docstring for Env"""

	TILE_DIRTY = 1
	TILE_CLEAN = 0
	OUT_OF_BOUND = -1

	def __init__(self, dim, dirtRatio):
		"""

		"""
		super(Env, self).__init__()
		self.dim = dim
		self.dirtRatio = dirtRatio
		self.grid = None

		self.gridCreate(self.dim)
		self.dirtAddRand(self.dirtRatio, self.grid)


	def gridCreate(self, dim):
		self.grid = [ [TILE_CLEAN]*dim[1] for i in xrange(dim[0]) ]


	def dirtAddRand(self, dirtRatio, grid):
		dim = [len(grid), len(grid[0])]
		dirtTilesNum = int( round(dirtRatio*dim[0]*dim[1]) )
		dirtTiles = random.sample( xrange(dim[0]*dim[1]), dirtTilesNum )

		for tileNum in dirtTiles:
			cood = [None, None]
			cood[0] = tileNum // dim[1]
			cood[1] = tileNum % dim[1]
			self.dirtAdd(cood, grid)


	def dirtAdd(self, cood, *args):
		if args:
			grid = args[0]
		else:
			grid = self.grid
		grid[cood[0]][cood[1]] = TILE_DIRTY


	def dirtRemove(self, cood, *args):
		if args:
			grid = args[0]
		else:
			grid = self.grid

		grid[cood[0]][cood[1]] = TILE_CLEAN


	def tileQuery(self, *args):
		if args:
			cood = args[0]
			if cood[0] in range[0,dim[0]] and cood[1] in range[0,dim[1]]:
				return grid[cood[0]][cood[1]]
			else:
				return OUT_OF_BOUND

		else:
			return self.grid

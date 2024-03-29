#! /usr/bin/python2

import random

class TileState(object):
	UNKNOWN = -1
	CLEAN = 0
	DIRTY = 1
	OUT_OF_BOUND = -2


class Env(object):
	"""docstring for Env"""

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
		self.grid = [ [TileState.CLEAN]*dim[1] for i in xrange(dim[0]) ]


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
		grid[cood[0]][cood[1]] = TileState.DIRTY


	def dirtRemove(self, cood, *args):
		if args:
			grid = args[0]
		else:
			grid = self.grid

		grid[cood[0]][cood[1]] = TileState.CLEAN


	def tileQuery(self, *args):
		if args:
			cood = args[0]
			if cood[0] in xrange(0,self.dim[0]) and cood[1] in xrange(0,self.dim[1]):
				return self.grid[cood[0]][cood[1]]
			else:
				return TileState.OUT_OF_BOUND

		else:
			return [row[:] for row in self.grid]

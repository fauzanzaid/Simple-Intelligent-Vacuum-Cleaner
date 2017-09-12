#! /usr/bin/python2

from env import TileState

class Controller(object):

	def __init__(self, dim, homes):
		self.dim = dim[:]
		self.homes = [home[:] for home in  homes]
		self.homeDist = None
		self.stats = {}
		self.homeDistCalc(self.dim)


	def homeDistCalc(self, grid):
		self.homeDist = [ [float("inf")]*self.dim[1] for i in xrange(self.dim[0]) ]

		for i,row in enumerate(self.homeDist):
			for j, v in enumerate(row):

				minCost = float("inf")
				for home in self.homes:
					cost = self.costMoveCalc(home, [i,j])
					if cost<minCost:
						minCost = cost

				self.homeDist[i][j] = minCost


	def costMoveCalc(self, pos1, pos2):
		return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


	def cleanTest(self, grid):
		for row in grid:
			for tile in row:
				if tile == TileState.UNKNOWN or tile == TileState.DIRTY:
					return False
		return True


	def homeTest(self, pos):
		if pos not in self.homes:
			return False
		return True


	def goalTest(self, grid, pos):
		raise NotImplementedError()


	def output(self, grid, pos):
		raise NotImplementedError()

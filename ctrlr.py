#! /usr/bin/python2

class Controller(object):

	def __init__(self, dim, homes):
		self.dim = dim[:]
		self.homes = [home[:] for home in  homes]
		self.homeDist = None
		self.homeDistInit(self.dim)


	def homeDistInit(self, grid):
		self.homeDist = [ [float("inf")]*self.dim[1] for i in xrange(self.dim[0]) ]

		for i,row in enumerate(self.homeDist):
			for j, v in enumerate(row):

				minCost = float("inf")
				for home in self.homes:
					cost = self.costMoveCalc(home, [i,j])
					if cost<minCost:
						minCost = cost

				self.homeDist[i][j] = minCost

	
	def output(self, grid, pos):
		raise NotImplementedError()
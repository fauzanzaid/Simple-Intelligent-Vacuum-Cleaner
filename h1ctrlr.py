#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction

class H1Controller(Controller):

	def __init__(self, dim, homes):
		super(H1Controller, self).__init__(dim, homes)
		self.homeDistInit(self.dim)


	def output(self, grid, pos):
		pass


	def heuristic(self, grid, pos):
		pass


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


	def costMoveCalc(self, pos1, pos2):
		return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

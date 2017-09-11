#! /usr/bin/python2

from ctrlr import Controller
from env import TileState

class DFSController(Controller):

	def __init__(self, dim, homes):
		super(DFSController, self).__init__(dim, homes)

	def output(self, grid, pos):
		actions = []

		dirtTiles = []
		for i, row in enumerate(grid):
			for j, tile in enumerate(row):
				if tile == TileState.DIRTY:
					dirtTiles.append([i,j])

		pathShort = []
		print self.dfs(dirtTiles, pos, pathShort, 0)
		print "Path:", pathShort


	def costMove(self, pos1, pos2):
		return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


	def dfs(self, dirtTiles, pos, path, cost):
		# print "dirtTiles: ",dirtTiles
		if len(dirtTiles) == 0:
			cur = self.homes[0][:]

			for home in self.homes:
				if self.costMove(home, pos) < self.costMove(cur, pos):
					cur = home[:]

			path.append(cur)

			# print "\t", path, cost+self.costMove(cur, pos)

			return cost+self.costMove(cur, pos)

		else:
			costs = []
			paths = []
			for i, dirtTile in enumerate(dirtTiles):
				dirtTilesNew = dirtTiles[:i]+dirtTiles[i+1:]

				pathNew = path[:]
				# print "Pre: ",pathNew
				pathNew.append(dirtTile)
				# print "Mid: ",pathNew
				costNew = self.dfs(dirtTilesNew, dirtTile, pathNew, cost+self.costMove(pos,dirtTile))
				# print "Post:",pathNew
				costs.append(costNew)
				paths.append(pathNew)

			minCost = min(costs)
			pathChoice = paths[costs.index(minCost)]
			# print "Choice: ",pathChoice

			path[:] = []
			path.extend(pathChoice)
			# print "Pre2",path
			# print "Costs:",costs, "Tiles:",dirtTiles

			# path.append(tileChoice)
			# print "Post2:",path
			return minCost

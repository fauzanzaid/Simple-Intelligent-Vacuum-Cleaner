#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction

class BestPathController(Controller):

	def __init__(self, dim, homes):
		super(BestPathController, self).__init__(dim, homes)

	def output(self, grid, pos):
		actions = []

		dirtTiles = []
		for i, row in enumerate(grid):
			for j, tile in enumerate(row):
				if tile == TileState.DIRTY:
					dirtTiles.append([i,j])

		path = []
		cost = self.dfs(dirtTiles, pos, path, 0)

		actions = self.pathToActions(pos, path)
		return actions


	def costMove(self, pos1, pos2):
		return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


	def dfs(self, dirtTiles, pos, path, cost):
		if len(dirtTiles) == 0:
			cur = self.homes[0][:]

			for home in self.homes:
				if self.costMove(home, pos) < self.costMove(cur, pos):
					cur = home[:]

			path.append(cur)
			return cost+self.costMove(cur, pos)

		else:
			costs = []
			paths = []
			for i, dirtTile in enumerate(dirtTiles):
				dirtTilesNew = dirtTiles[:i]+dirtTiles[i+1:]

				pathNew = path[:]
				pathNew.append(dirtTile)
				costNew = self.dfs(dirtTilesNew, dirtTile, pathNew, cost+self.costMove(pos,dirtTile))
				costs.append(costNew)
				paths.append(pathNew)

			minCost = min(costs)
			pathChoice = paths[costs.index(minCost)]

			path[:] = []
			path.extend(pathChoice)
			return minCost


	def pathToActions(self, pos, path):
		actions = []
		pos = pos[:]

		for tile in path:
			disp = [tile[0]-pos[0], tile[1]-pos[1]]

			if disp[0] < 0:
				for i in range(-disp[0]):
					actions.append(IVCAction.MOVE_UP)
			elif disp[0] > 0:
				for i in range(disp[0]):
					actions.append(IVCAction.MOVE_DOWN)

			if disp[1] < 0:
				for i in range(-disp[1]):
					actions.append(IVCAction.MOVE_LEFT)
			elif disp[1] > 0:
				for i in range(disp[1]):
					actions.append(IVCAction.MOVE_RIGHT)

			pos[0] = tile[0]
			pos[1] = tile[1]

			actions.append(IVCAction.SUCK)

		actions.pop()	# Remove last suck, not needed
		return actions

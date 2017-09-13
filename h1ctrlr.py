#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction
import random

class H1Controller(Controller):

	def __init__(self, dim, homes):
		super(H1Controller, self).__init__(dim, homes)
		self.stats["nodesGen"] = 0


	def output(self, grid, pos):
		if self.cleanTest(grid):
			actions = self.actionsToHome(pos)
		else:
			mat = self.heuristic(grid, pos)
			tile = self.heuristicToChoice(mat, pos)
			actions = self.pathToActions(grid, [pos,tile])

		return actions


	def heuristic(self, grid, pos):
		mat = [ [float("inf")]*3 for i in xrange(3) ]
		for i in xrange(3):
			for j in xrange(3):
				r = pos[0]+i-1
				c = pos[1]+j-1
				if r in xrange(self.dim[0]) and c in xrange(self.dim[1]):
					self.stats["nodesGen"] += 1
					if grid[r][c] == TileState.DIRTY:
						mat[i][j] = 0
					elif grid[r][c] == TileState.UNKNOWN:
						mat[i][j] = 5
					elif grid[r][c] == TileState.CLEAN:
						mat[i][j] = 10
					mat[i][j] += abs(i-1) + abs(j-1)

		if grid[pos[0]][pos[1]] != TileState.DIRTY:
			mat[1][1] = float("inf")

		return mat


	def heuristicToChoice(self, mat, pos):
		minVal = float("inf")
		minValTiles = []

		for i, row in enumerate(mat):
			for j, val in enumerate(row):
				tile = [pos[0]+i-1, pos[1]+j-1]
				if val == minVal:
					minValTiles.append(tile)
				elif val < minVal:
					minVal = val
					minValTiles = [tile]
		return random.choice(minValTiles)


	def pathToActions(self, grid, path):
		grid = [ row[:] for row in grid ]
		if path == None:
			return [IVCAction.ABORT]

		pos = path[0]
		actions = []

		for tile in path:

			disp = [tile[0]-pos[0], tile[1]-pos[1]]

			if disp[0] == -1:
				actions.append(IVCAction.MOVE_UP)
			if disp[0] == 1:
				actions.append(IVCAction.MOVE_DOWN)
			if disp[1] == -1:
				actions.append(IVCAction.MOVE_LEFT)
			if disp[1] == 1:
				actions.append(IVCAction.MOVE_RIGHT)

			if grid[tile[0]][tile[1]] == TileState.DIRTY:
				actions.append(IVCAction.SUCK)
				grid[tile[0]][tile[1]] = TileState.CLEAN

			pos = tile

		return actions


	def actionsToHome(self, pos):
		minCost = float("inf")
		minCostHome = None
		for home in self.homes:
			cost = self.costMoveCalc(pos, home)
			if cost < minCost:
				minCost = cost
				minCostHome = home

		actions = []
		disp = [minCostHome[0]-pos[0], minCostHome[1]-pos[1]]

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

		return actions

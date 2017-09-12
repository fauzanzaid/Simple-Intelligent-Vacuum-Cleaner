#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction

class IDDFSController(Controller):

	def __init__(self, dim, homes):
		super(IDDFSController, self).__init__(dim, homes)


	def output(self, grid, pos):

		dirtyTiles = []
		for i, row in enumerate(grid):
			for j, tile in enumerate(row):
				if tile == TileState.UNKNOWN:
					return [IVCAction.ABORT]
				if tile == TileState.DIRTY:
					dirtyTiles.append([i,j])

		path = [pos]
		path = self.iddfs(path, dirtyTiles, 15)
		actions = self.pathToActions(grid, path)

		return actions + self.actionsToHome(path[-1])


	def iddfs(self, path, dirtyTiles, depthMaxLimit):
		for depthMax in range(depthMaxLimit):
			pathRet = self.dldfs(path,dirtyTiles,0,depthMax)
			if pathRet != None:
				return pathRet
		return None


	def dldfs(self, path, dirtyTiles, depth, depthMax):
		if depth > depthMax:
			return None
		elif self.goalTest(path, dirtyTiles) == True:
			return path
		else:
			pos = path[-1]
			if pos[0] != 0:
				pathIncr = path + [[ pos[0]-1,pos[1] ]]
				pathRet = self.dldfs(pathIncr,dirtyTiles,depth+1,depthMax)
				if pathRet != None:
					return pathRet
			
			if pos[0] != self.dim[0]:
				pathIncr = path + [[ pos[0]+1,pos[1] ]]
				pathRet = self.dldfs(pathIncr,dirtyTiles,depth+1,depthMax)
				if pathRet != None:
					return pathRet
			
			if pos[1] != 0:
				pathIncr = path + [[ pos[0],pos[1]-1 ]]
				pathRet = self.dldfs(pathIncr,dirtyTiles,depth+1,depthMax)
				if pathRet != None:
					return pathRet
			
			if pos[1] != self.dim[1]:
				pathIncr = path + [[ pos[0],pos[1]+1 ]]
				pathRet = self.dldfs(pathIncr,dirtyTiles,depth+1,depthMax)
				if pathRet != None:
					return pathRet

		return None


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



	def goalTest(self, path, dirtyTiles):
		for dirtyTile in dirtyTiles:
			if dirtyTile not in path:
				return False
		return True

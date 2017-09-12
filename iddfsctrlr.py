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
			


	def goalTest(self, path, dirtyTiles):
		for dirtyTile in dirtyTiles:
			if dirtyTile not in path:
				return False
		return True

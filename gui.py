#! /usr/bin/python2

import turtle
from env import TileState

class GUI(object):
	"""This class implements the gui in turtle"""

	def __init__(self):
		self.P1_COOD = [0, 625]
		self.G1_COOD = [250, 625]
		self.G2_COOD = [500, 625]
		self.G3_COOD = [250, 375]
		self.G4_COOD = [250, 375]

		self.TILE_SIZE = 20
		self.TILE_SPACING = 20
		self.TILE_MARK_SIZE = 3
		self.TILE_MARK_OFFSET = 5
		self.TILE_MARK_CLEAN = (0.5,0.5,1)
		self.TILE_MARK_DIRTY = (1,0.5,0.5)
		
		self.P1_OFFSET = 30
		self.P1_LINESPACE = 15

		turtle.setworldcoordinates(0,0,750,750)
		turtle.ht()
		turtle.pu()
		turtle.speed(0)
		turtle.delay(0)


	def drawTile(self, cood):
		turtle.goto(cood[0]-self.TILE_SIZE/2.0, cood[1]-self.TILE_SIZE/2.0)
		turtle.seth(90)
		turtle.pd()
		for i in xrange(4):
			turtle.fd(self.TILE_SIZE)
			turtle.rt(90)
		turtle.pu()


	def drawTileMark(self, cood, state):
		turtle.goto(cood[0]-self.TILE_MARK_OFFSET, cood[1]-self.TILE_MARK_OFFSET)
		turtle.pd()
		if state == TileState.CLEAN:
			turtle.dot(self.TILE_MARK_SIZE, self.TILE_MARK_CLEAN)
		if state == TileState.DIRTY:
			turtle.dot(self.TILE_MARK_SIZE, self.TILE_MARK_DIRTY)
		turtle.pu()


	def drawGrid(self, cood, dim):
		for i in xrange(dim[0]):
			for j in xrange(dim[1]):
				x = cood[0] + j*self.TILE_SPACING
				y = cood[1] - i*self.TILE_SPACING
				self.drawTile([x,y])


	def drawGridMark(self, cood, grid):
		for i, row in enumerate(grid):
			for j, state in enumerate(row):
				x = cood[0] + j*self.TILE_SPACING
				y = cood[1] - i*self.TILE_SPACING
				self.drawTileMark([x,y], state)


	def drawPartition1Text(self, idx, val):
		cood = self.P1_COOD
		text = "R"+str(idx)+" :\t"+str(val)
		turtle.goto(cood[0]+self.P1_OFFSET, cood[1]-self.P1_OFFSET-(idx)*self.P1_LINESPACE)
		turtle.write(text)

#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction

class H1Controller(Controller):

	def __init__(self, dim, homes):
		super(H1Controller, self).__init__(dim, homes)


	def output(self, grid, pos):
		pass


	def heuristic(self, grid, pos):
		pass


	def costMoveCalc(self, pos1, pos2):
		return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

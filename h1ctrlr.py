#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction

class H1Controller(Controller):
	
	def __init__(self, dim, homes):
		super(DFSController, self).__init__(dim, homes)

	def output(self, grid, pos):
		pass

	def heuristic(self, grid, pos):
		pass
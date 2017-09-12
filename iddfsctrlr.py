#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction

class UnInfDFSController(Controller):

	def __init__(self, dim, homes):
		super(UnInfDFSController, self).__init__(dim, homes)


	def output(self, grid, pos):
		pass

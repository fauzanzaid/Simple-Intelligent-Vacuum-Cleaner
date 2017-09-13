#! /usr/bin/python2

from ctrlr import Controller
from env import TileState
from ivc import IVCAction
import random

class H2Controller(Controller):

	def __init__(self, dim, homes):
		super(H2Controller, self).__init__(dim, homes)


	def output(self, grid, pos):
		pass

	def heuristic(self, grid, pos):
		pass
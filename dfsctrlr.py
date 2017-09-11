#! /usr/bin/python2

from ctrlr import Controller

class DFSController(Controller):

	def __init__(self, dim, homes):
		super(DFSController, self).__init__(dim, homes)

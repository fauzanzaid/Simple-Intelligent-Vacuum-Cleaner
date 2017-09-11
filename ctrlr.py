#! /usr/bin/python2

class Controller(object):

	def __init__(self, dim, homes):
		self.dim = dim[:]
		self.homes = [home[:] for home in  homes]

	
	def output(self, grid, pos):
		raise NotImplementedError()
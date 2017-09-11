#! /usr/bin/python2

class Controller(object):

	def __init__(self, homes):
		self.homes = [home[:] for home in  homes]

	
	def output(self, env, pos):
		raise NotImplementedError()
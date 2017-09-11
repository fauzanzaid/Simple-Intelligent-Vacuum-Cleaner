#! /usr/bin/python2

from env import Env, TileState

class IVCAction(object):
	SUCK = 0
	U = 1
	D = 2
	L = 3
	R = 4

class IVC(object):

	def __init__(self, env, pos):
		self.env = env
		self.pos = [i for i in pos]


	def memInit(self, env):
		self.mem = [ [TileState.UNKNOWN]*env.dim[1] for i in xrange(env.dim[0]) ]

#! /usr/bin/python2

from env import Env, TileState

class IVCAction(object):
	SUCK = 0
	U = 1
	D = 2
	L = 3
	R = 4



class IVCActionCost(object):
	SUCK = 1
	U = 2
	D = 2
	L = 2
	R = 2



class IVCVisibility(object):
	ALL = -1
	ONE = 1



class IVC(object):

	def __init__(self, env, controller, pos):
		self.env = env
		self.pos = [i for i in pos]
		self.controller = controller


	def memInit(self, env):
		self.mem = [ [TileState.UNKNOWN]*env.dim[1] for i in xrange(env.dim[0]) ]


	def goalTest(self):
		pass


	def act(self, actions):
		pass


	def run(self):
		pass
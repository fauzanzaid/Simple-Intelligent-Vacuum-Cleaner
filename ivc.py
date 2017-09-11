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

	def __init__(self, env, controller, pos, visibility):
		self.env = env
		self.pos = pos[:]
		self.controller = controller
		self.visibility = visibility

		self.queryNum = 0


	def memInit(self, env):
		self.mem = [ [TileState.UNKNOWN]*env.dim[1] for i in xrange(env.dim[0]) ]


	def goalTest(self):
		if pos not in self.controller.homes:
			return False

		for row in self.mem:
			for tile in row:
				if tile == TileState.UNKNOWN or tile == TileState.DIRTY:
					return False

		return True



	def perceive(self):
		if self.visibility == IVCVisibility.ALL:
			if queryNum == 0:
				self.mem = self.env.tileQuery()
				queryNum += 1

		elif self.visibility == IVCVisibility.ONE:
			for cood0 in xrange(pos[0]-1, pos[0]+2):
				for cood1 in xrange(pos[1]-1, pos[2]+2):
					if cood0 in range[0,dim[0]] and cood1 in range[0,dim[1]]:
						self.mem[cood0,cood1] = self.env.tileQuery([cood0,cood1])


	def act(self, actions):
		pass


	def run(self):
		pass
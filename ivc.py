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

	def __init__(self, name, env, controller, pos, visibility):
		self.name = name
		self.env = env
		self.pos = pos[:]
		self.controller = controller
		self.visibility = visibility

		self.queryNum = 0

		self.memInit(self.env)
		self.perceive(self.env, self.pos)


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


	def perceive(self, env, pos):
		if self.visibility == IVCVisibility.ALL:
			if queryNum == 0:	# need to make only one query if ALL
				self.mem = env.tileQuery()
				queryNum += 1

		elif self.visibility == IVCVisibility.ONE:
			for cood0 in xrange(pos[0]-1, pos[0]+2):
				for cood1 in xrange(pos[1]-1, pos[2]+2):
					if cood0 in xrange[0,dim[0]] and cood1 in xrange[0,dim[1]]:
						self.mem[cood0,cood1] = env.tileQuery([cood0,cood1])


	def actMoveUp(self, env):
		if self.pos[0]-1 in xrange[0,dim[0]]:
			pos[0] -= 1
		else:
			raise IndexError("IVC:"name" cannot climb walls")


	def actMoveDown(self, env):
		if self.pos[0]+1 in xrange[0,dim[0]]:
			pos[0] += 1
		else:
			raise IndexError("IVC:"name" cannot climb walls")


	def actMoveLeft(self, env):
		if self.pos[1]-1 in xrange[0,dim[1]]:
			pos[1] -= 1
		else:
			raise IndexError("IVC:"name" cannot climb walls")


	def actMoveRight(self, env):
		if self.pos[1]+1 in xrange[0,dim[1]]:
			pos[1] += 1
		else:
			raise IndexError("IVC:"name" cannot climb walls")


	def actSuck(self, env):
		self.env.dirtRemove(pos)


	def act(self, actions):
		


	def run(self):
		pass
#! /usr/bin/python2

from env import Env, TileState

class IVCAction(object):
	SUCK = 0
	MOVE_UP = 1
	MOVE_DOWN = 2
	MOVE_LEFT = 3
	MOVE_RIGHT = 4



class IVCActionCost(object):
	SUCK = 1
	MOVE_UP = 2
	MOVE_DOWN = 2
	MOVE_LEFT = 2
	MOVE_RIGHT = 2



class IVCVisibility(object):
	ALL = -1
	ONE = 1



class IVC(object):

	def __init__(self, name, env, pos, controller, visibility):
		self.name = name
		self.env = env
		self.pos = pos[:]
		self.controller = controller
		self.visibility = visibility

		self.cost = 0
		self.actionsHistory = []

		self.memInit(self.env)
		self.perceive(self.env, self.pos)


	def memInit(self, env):
		self.mem = [ [TileState.UNKNOWN]*env.dim[1] for i in xrange(env.dim[0]) ]


	def goalTest(self):
		if self.pos not in self.controller.homes:
			return False

		for row in self.mem:
			for tile in row:
				if tile == TileState.UNKNOWN or tile == TileState.DIRTY:
					return False

		return True


	def perceive(self, env, pos):
		if self.visibility == IVCVisibility.ALL:
			self.mem = env.tileQuery()

		elif self.visibility == IVCVisibility.ONE:
			for cood0 in xrange(pos[0]-1, pos[0]+2):
				for cood1 in xrange(pos[1]-1, pos[1]+2):
					if cood0 in xrange(0,env.dim[0]) and cood1 in xrange(0,env.dim[1]):
						self.mem[cood0][cood1] = env.tileQuery([cood0,cood1])


	def actMoveUp(self, env, pos):
		if pos[0]-1 in xrange(0,env.dim[0]):
			pos[0] -= 1
			self.cost += IVCActionCost.MOVE_UP
		else:
			raise IndexError("IVC:"+self.name+" cannot climb walls")


	def actMoveDown(self, env, pos):
		if pos[0]+1 in xrange(0,env.dim[0]):
			pos[0] += 1
			self.cost += IVCActionCost.MOVE_DOWN
		else:
			raise IndexError("IVC:"+self.name+" cannot climb walls")


	def actMoveLeft(self, env, pos):
		if pos[1]-1 in xrange(0,env.dim[1]):
			pos[1] -= 1
			self.cost += IVCActionCost.MOVE_LEFT
		else:
			raise IndexError("IVC:"+self.name+" cannot climb walls")


	def actMoveRight(self, env, pos):
		if pos[1]+1 in xrange(0,env.dim[1]):
			pos[1] += 1
			self.cost += IVCActionCost.MOVE_RIGHT
		else:
			raise IndexError("IVC:"+self.name+" cannot climb walls")


	def actSuck(self, env, pos):
		self.cost += IVCActionCost.SUCK
		env.dirtRemove(pos)


	def act(self, actions):
		for action in actions:
			self.actionsHistory.append(action)

			if action == IVCAction.SUCK:
				self.actSuck(self.env, self.pos)

			elif action == IVCAction.MOVE_UP:
				self.actMoveUp(self.env, self.pos)
			
			elif action == IVCAction.MOVE_DOWN:
				self.actMoveDown(self.env, self.pos)
			
			elif action == IVCAction.MOVE_LEFT:
				self.actMoveLeft(self.env, self.pos)

			elif action == IVCAction.MOVE_RIGHT:
				self.actMoveRight(self.env, self.pos)

		self.perceive(self.env, self.pos)


	def run(self):
		while self.goalTest() == False:
			self.act(self.controller.output(self.mem, self.pos))

#! /usr/bin/python2

from env import Env

class IVC(object):

	def __init__(self, env, pos):
		self.env = env
		self.pos = [i for i in pos]

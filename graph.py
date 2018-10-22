import os
import collections
import math

class Node:
	def __init__(self, _tuple):
		self._id = _tuple[0]
		self.x = _tuple[1]
		self.y = _tuple[2]
		self.costo = 0
	
	def get_coordsx(self):
		return self.x
	
	def get_coordsy(self):
		return self.y
	
	def get_id(self):
		return self._id


	@staticmethod
	def distanceToCity(node1 , node2 ):
		x = abs(node1.get_coordsx() - node2.get_coordsx())
		y = abs(node1.get_coordsy() - node2.get_coordsy())
		return math.sqrt(pow(x,2) + pow(y,2))
	
	def __str__(self):
		return 'id {}: ({}, {})'.format(self._id, self.x, self.y)

class SimpleGraph:
	def __init__():
		edges = {}
	
	def neighbors(self, _id):
		return self.edges[_id]

class Queue:
	def __init__(self):
		self.elements = collections.deque()

	def empty(self):
		return len(self.elements) == 0

	def push(self, x):
		self.elements.append(x)

	def pop(self):
		return self.elements.popleft()

def get_nodes(txt='./nodes.txt'):
	if os.path.isfile(txt):
		txtfile = open(txt, 'r')
		nodes = txtfile.readlines()
		nodes = [tuple(map(lambda x: int(x), n.split(' '))) for n in nodes if ' ' in n]
		return [Node(t) for t in nodes]
	else:
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), txt)
import os
from math import sqrt

class Node:
	def __init__(self, _tuple):
		self._id = _tuple[0]
		self.x = _tuple[1]
		self.y = _tuple[2]
		self.costo = 1
	
	def get_coordsx(self):
		return self.x
	
	def get_coordsy(self):
		return self.y
	
	def get_id(self):
		return self._id

	@staticmethod
	def del_node(node, list_nodes):
		for i in range(len(list_nodes)):
			if node._id == list_nodes[i]._id:
				del list_nodes[i]
				return list_nodes
	
	@staticmethod
	def distanceToCity(node1 , node2): # euclidean
		x = abs(node1.get_coordsx() - node2.get_coordsx())
		y = abs(node1.get_coordsy() - node2.get_coordsy())
		return sqrt(pow(x,2) + pow(y,2))
	
	def __str__(self):
		return 'id {}: ({}, {})'.format(self._id, self.x, self.y)
	
	@staticmethod
	def get_heuristic(nodes):
		heuristica = 0.0
		for i in range(1,len(nodes)):
			heuristica = heuristica + Node.distanceToCity(nodes[i-1],nodes[i])
		# print("la heuristica es ->", heuristica)
		return heuristica

def get_nodes(txt='./nodes.txt'):
	if os.path.isfile(txt):
		txtfile = open(txt, 'r')
		nodes = txtfile.readlines()
		nodes = [tuple(map(lambda x: int(x), n.split(' '))) for n in nodes if ' ' in n]
		return [Node(t) for t in nodes]
	else:
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), txt)

def get_best_F(close_list, open_list):
	g_x = 0.0
	h_x = float("inf")
	min_node = open_list[0]
	
	# comprobar que el nodo rescatado no esta en la close_list
	for idx, node in enumerate(close_list):
		if node.get_id() == min_node.get_id():
			min_node = open_list[idx]
	
	# obtener el g_x del camino recorrido hasta ahora
	if len(close_list) in [0, 1]:
		g_x = 0
	else:
		for i in range(1, len(close_list)):
			g_x += Node.distanceToCity(close_list[i-1], close_list[i])

	# obtener el nodo de menor distancia (h_x)
	if len(close_list) != 0:
		for node in open_list:
			hh = Node.distanceToCity(close_list[-1], node)
			if hh < h_x:
				h_x = hh
				min_node = node
	
	return min_node

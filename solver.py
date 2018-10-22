from graph import Node

def get_heuristic(nodes):
	heuristica = 0.0
	#heuristica = nodes[0].distanceToCity(nodes[1])
	for i in range(1,len(nodes)):
		heuristica = heuristica + Node.distanceToCity(nodes[i-1],nodes[i])
	print("la heuristica es ->", heuristica)




def tsp_solver(nodes):
	tamanno = len(nodes)
	open_list = []
	close_list = []
	open_list.append(nodes[0])
	

	while len(open_list) != 0:
		cont = 0
		del nodes[0]
		print(open_list)
		close_list.append(open_list.pop())
		print(close_list)
		print(open_list)
		
			
		"""
		for i in nodes:
			Node.distanceToCity(open_list[cont],nodes[i])
		nodes.sort(key = costo)
		"""



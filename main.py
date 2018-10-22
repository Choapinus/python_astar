from graph import get_nodes, SimpleGraph
from solver import get_heuristic, tsp_solver

if __name__ == '__main__':
	nodes = get_nodes()

get_heuristic(nodes)

tsp_solver(nodes)

#print (nodes)
"""
for i in nodes:
	print("id: ", i.get_id())
	print("x: ", i.get_coordsx())
	print("y: ", i.get_coordsy())	
"""
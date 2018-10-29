from graph import Node, get_nodes, get_best_F


import time

start = time.time()

nodes = get_nodes()

meta = nodes[-1]
init_node = nodes[0]
solution_found = False

# print('init_node', init_node)
# print('meta', meta, '\n')

open_list = [nodes[0]]
close_list = []
nodes = Node.del_node(nodes[0], nodes)

for node in nodes:
    open_list.append(node)

start_g = 0.0
start_f = start_g + Node.distanceToCity(init_node, meta) # g+h

while open_list != []:
    best_node = get_best_F(close_list, open_list) # get node with best f(x)
    
    if best_node.get_id() == meta.get_id():
        solution_found = True

    close_list.append(best_node)
    open_list = Node.del_node(best_node, open_list)

close_list.append(meta)

total_dist = 0.0

for idx in range(1, len(close_list)):
    total_dist += Node.distanceToCity(close_list[idx-1], close_list[idx])


end = time.time()

print('tiempo total:', end - start, 'segundos')
print('distancia total:', total_dist)
print('cantidad de expansiones:', len(close_list))

# nota:
# dado a que se esta trabajando con un grafo completo,
# la expansion de todo nodo resultara en todos los demas nodos,
# bajo esta logica, se agregan todos los nodos a la lista open una sola vez
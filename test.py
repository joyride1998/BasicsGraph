from dgraph import Graph, Vertex

h = Graph()

h.add_vertex('b')
h.add_vertex('a')
h.add_vertex('c')
h.add_vertex('d')
h.add_vertex('e')
h.add_vertex('f')
h.add_vertex('g')

h.add_edge('a', 'b', 11)  
h.add_edge('a', 'c', 2)
h.add_edge('b', 'c', 3)
h.add_edge('b', 'd', 14)
h.add_edge('c', 'd', 5)
h.add_edge('d', 'c', 6)    
h.add_edge('e', 'f', 7) 
h.add_edge('f', 'c', 18)
h.add_edge('g', 'g', None)
	
print(h.plot_graph()) 


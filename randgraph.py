# Generate a randomly connected graph with N nodes and E edges
# 7-19-2017
# Author: Li-Pin Juan
# Reference: https://goo.gl/DzkgSP Loop-erased random walk
#            https://goo.gl/kX6HjZ Maze generation algorithm   
#            https://goo.gl/s9QDYH Implementation of uniform spanning tree

import random
import argparse
from dgraph import Graph

def random_walk(nodes, num_edges):
    # create a uniform spanning tree; with additional random edges, if needed
    
    def check_input(nodes, num_edges):
        """Checks if the number of requested edges is acceptable."""
        num_nodes = len(nodes)
        min_edges = num_nodes - 1
        if num_edges < min_edges:
            raise ValueError('num_edges less than minimum (%i)' % min_edges)
            max_edges = num_nodes * (num_nodes - 1)
            if num_edges > max_edges:
                raise ValueError('num_edges greater than maximum (%i)' % max_edges)
                   
    check_input(nodes,num_edges)
    # create two partitions, U and V. U starts with the full complement of 
    # the input nodes; V is empty.
    U, V = set(nodes), set() # V is the set of visited nodes
    # Pick a node arbitrarily, mark it as visited (current) node
    current_node = random.sample(U,1).pop()
    U.remove(current_node)
    V.add(current_node)
    g = Graph()
    g.add_vertex(current_node)
    
    tot_edges = 0
    # create a random directed graph
    while U:
        # Randomly pick the next node from the neighbors of the current node.
        neighbor_node = random.sample(nodes,1).pop()
        if neighbor_node not in V:
            g.add_vertex(neighbor_node)
            g.add_edge(current_node,neighbor_node)
            tot_edges = tot_edges + 1
            U.remove(neighbor_node)
            V.add(neighbor_node)
        current_node = neighbor_node
    # add random edges until the designated number of edges is reached.
    while(tot_edges<num_edges): 
        frm, to = random.sample(V,2)        
        g.add_edge(frm,to)
        tot_edges = tot_edges + 1
    
    print(g.plot_graph())  
    return g

  
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('nodes',
                        help='filename containing node labels (one per line) '
                             'OR integer number of nodes to generate')
    parser.add_argument('-e', '--edges', type=int,
                        help='number of edges (default is minimum possible)')
    args = parser.parse_args()

    num_edges = args.edges
    # Nodes
    try:
        nodes = []
        with open(args.nodes) as f:
            for line in f:
                nodes.append(line.strip())
    except IOError:
        try:
            nodes = [x for x in xrange(int(args.nodes))]
        except ValueError:
            raise TypeError('nodes argument must be a filename or an integer')

    # Run
    graph = random_walk(nodes, num_edges)

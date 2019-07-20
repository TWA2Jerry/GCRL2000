import networkx as nx

g = nx.Graph()

g.add_nodes_from([1,2,3,4,5,6])
g.add_edges_from([(1,5), (1,2), (1,4), (2,3),(2,4), (3,5), (3,4),(3,6),(4,6)])
print(g.node)

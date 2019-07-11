import networkx as nx

g = nx.Graph()
g.add_nodes_from([1,2,3,4])
g.add_edges_from([(1,2), (2,3)])
g[1][2]["weight"] = 4.0
print(g.edges[1,2]["weight"])

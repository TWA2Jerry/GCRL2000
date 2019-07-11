import networkx as nx

g = nx.Graph()

g.add_nodes_from(['James', 'John', 'Jesse'])
g.add_edges_from([('James', 'Jesse'), ('Jesse', 'John')])

print(g.edges)
g['James']['Jesse']['color'] = "blue"
print(g.edges['James', 'Jesse']['color'])

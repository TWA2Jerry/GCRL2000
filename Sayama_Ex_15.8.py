import networkx as nx

g = nx.complete_graph(10)

for i in range(1, 11):
	g.add_node(10+i)
	g.add_edge(i, 10+i)

print(g.nodes())
print(g.edges)

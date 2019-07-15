import networkx as nx, pylab

g = nx.erdos_renyi_graph(100, 0.11)
h = nx.watts_strogatz_graph(100, 11, 0.5)
j = nx.barabasi_albert_graph(100, 6)

print(nx.average_clustering(g))
print(nx.average_clustering(h))
print(nx.average_clustering(j))

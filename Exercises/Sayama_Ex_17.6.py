import networkx as nx, pylab

g = nx.erdos_renyi_graph(100, 0.11)
g.pos = nx.spring_layout(g)

h = nx.watts_strogatz_graph(100, 11, 0.5)
h.pos = nx.spring_layout(h)

j = nx.barabasi_albert_graph(100, 6)
j.pos = nx.spring_layout(j)
print(nx.density(g))
print(nx.density(h))
print(nx.density(j))

pylab.subplot(1,3,1)
a = nx.degree_centrality(g)
nx.draw(g, node_color = [a[i] for i in a], pos = g.pos)
pylab.subplot(1,3,2) 
b = nx.degree_centrality(h)
nx.draw(h, node_color = [b[i] for i in b], pos = h.pos)
pylab.subplot(1,3,3) 
c = nx.degree_centrality(j)
nx.draw(g, node_color = [a[i] for i in c], pos = j.pos) 
pylab.show()

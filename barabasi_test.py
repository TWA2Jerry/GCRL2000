import networkx as nx, pylab

g = nx.barabasi_albert_graph(100, 6)
g.pos = nx.spring_layout(g)
print(nx.density(g))
nx.draw(g, pos = g.pos)
pylab.show()

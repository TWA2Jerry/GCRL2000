import networkx as nx, pylab

pdata = []
Ldata = []
Cdata = []

g0 = nx.watts_strogatz_graph(1000, 10, 0)
L0 = nx.average_shortest_path_length(g0)
C0  = nx.average_clustering(g0)

p = 0.0001
while p < 1.0:
	pdata.append(p)
	Laverages = []
	Caverages = []
	for i in range(3):
		g = nx.watts_strogatz_graph(1000, 10, p)
		a = nx.average_shortest_path_length(g)/L0
		c = nx.average_clustering(g)/C0
		Laverages.append(a)
		Caverages.append(c)
	Ldata.append(pylab.mean(Laverages))
	Cdata.append(pylab.mean(Caverages))
	p *= 1.5

pylab.semilogx(pdata, Ldata, label = 'L / L0')
pylab.semilogx(pdata, Cdata, label = 'C / C0')
pylab.xlabel('p')
pylab.legend()
pylab.show()

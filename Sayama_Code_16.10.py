import matplotlib
matplotlib.use("TkAgg")
import networkx as nx, pylab
import random as rd

k = 2
n = 30

def init():
	global g
	g = nx.Graph()
	g.add_nodes_from(range(1, n+1))
	for i in g.nodes():
		for j in range(1, int(k/2)):
			g.add_edges_from([(grade.node[i], graph.node[(i-j)%n]), (graph.node[i], graph.node[(i+j)%n])])
	g.pos = nx.spring_layout(g)
	g.count = 0
	
		

def update():
	global g
	g.count += 1
	if g.count%20 == 0:
		originnode = rd.choice(list(g.nodes()))
		nds = (g.nodes())
		if g.degree(originnode):
			g.remove_edge(originnode, rd.choice(list(g.neighbors(originnode))))
			for j in (g.neighbors(originnode)):
				nds.remove(j)
			g.add_node(originnode, rd.choice(list(nds)))

	g.pos = nx.spring_layout(g, pos=g.pos, iterations = 5)

def observe():
	global g
	pylab.cla()
	nx.draw(g)

import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])	


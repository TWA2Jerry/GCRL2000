import matplotlib
matplotlib.use('TkAgg')
import networkx as nx, pylab
import random as rd

p = 0.5

def init():
	global g
	g = nx.grid_graph([5,6], periodic=False)
	g.pos = nx.spring_layout(g)
	g.count = 1				

def update():
	global g
	g.count += 1
	if g.count%20 == 0:
		nds = list(g.nodes())
		originnode = rd.choice(nds)
		if(g.degree[originnode] > 0):
			g.remove_edge(originnode, rd.choice(list(g.neighbors(originnode))))
			for j in list(g.neighbors(originnode)):
				nds.remove(j)
			newnode = rd.choice(nds)
			g.add_edge(originnode, newnode)
		
	g.pos = nx.spring_layout(g, pos=g.pos, iterations=5)		

def observe():
	global g
	pylab.cla()
	nx.draw(g, pos = g.pos)

import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])

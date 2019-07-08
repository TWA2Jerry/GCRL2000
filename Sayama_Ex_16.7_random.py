import matplotlib
matplotlib.use('TkAgg')
import networkx as nx, pylab
import random as rd

alpha = 1
Dt = 0.01

def init():
	global g, nextg
	g = nx.gnp_random_graph(50, 0.4)
	for i in g.nodes():
		g.node[i]['state'] = 1 if pylab.random() < 0.5 else 0
	nextg = g.copy()

def update():
	global g, nextg
	for i in g.nodes():
		ci = g.node[i]['state']
		Lap = sum(g.node[j]['state'] for j in g.neighbors(i))
		Lap = Lap-1*ci*(g.degree(i))
		nextg.node[i]['state'] = g.node[i]['state'] + (alpha*Lap)*Dt
	g, nextg = nextg, g

def observe():
	global g, nextg
	pylab.cla()
	nx.draw(g, cmap = pylab.cm.binary, vmin = 0, vmax = 1, node_color = [g.node[i]['state'] for i in g.nodes()])
	
import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])

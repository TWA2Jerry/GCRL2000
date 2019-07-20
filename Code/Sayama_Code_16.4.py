import matplotlib
from tkinter import ttk
matplotlib.use('TkAgg')
import networkx as nx, pylab

def init():
	global g, nextg
	g = nx.karate_club_graph()
	g.pos = nx.spring_layout(g)
	for i in g.nodes():
		g.node[i]['state'] = 1 if pylab.random() < 0.5 else 0
	nextg = g.copy()

def update():
	global g, nextg
	for i in g.nodes():
		count  = g.node[i]['state']
		for j in g.neighbors(i):
			count += g.node[j]['state']
		ratio = count/(g.degree(i)+1)
		nextg.node[i]['state'] = 1 if ratio > 0.5 else 0
	g, nextg  = nextg, g

def observe():
	global g, nextg
	pylab.cla()
	nx.draw(g, cmap = pylab.cm.RdBu, vmin = 0, vmax = 1, node_color = [g.node[i]['state'] for i in g.nodes()])

import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])	

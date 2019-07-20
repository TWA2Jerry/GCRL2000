import matplotlib 
matplotlib.use('TkAgg')
import networkx as nx, pylab
import random as rd

p_i = 0.5
p_r = 0.5

def p_i_setter(val = p_i):
	global p_i
	p_i = val
	return val

def p_r_setter(val = p_r):
	global p_r
	p_r = val
	return val
	

def init():
	global g
	g = nx.karate_club_graph()
	for i in g.nodes():
		g.node[i]['state'] = 1 if pylab.random() < p_i else 0

def update():
	global g
	a = rd.choice(list(g.nodes()))
	if g.node[a]['state'] == 0:
		b = rd.choice(list(g.neighbors(a)))
		if g.node[b]['state'] == 1:
			g.node[a]['state'] = 1 if pylab.random() < p_i else 0
	else:
		g.node[a]['state'] = 0 if pylab.random() < p_r else 1

def observe():
	global g
	pylab.cla()
	nx.draw(g, cmap = pylab.cm.binary, vmin = 0, vmax = 1, node_color = [g.node[i]['state'] for i in g.nodes()])
	

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [p_i_setter, p_r_setter]).start(func=[init, observe, update])

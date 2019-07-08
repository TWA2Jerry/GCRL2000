import matplotlib
matplotlib.use('TkAgg')
import networkx as nx, pylab
import random as rd

p_i = 0.5
p_r = 0.2
p_s = 0.5

def p_s_setter(val = p_s):
	global p_s
	p_s = val
	return val

def init():
	global g
	g = nx.karate_club_graph()
	g.pos = nx.spring_layout(g)
	for i in g.nodes():
		g.node[i]['state'] = 1 if pylab.random() < p_i else 0
	

def update():
	global g
	i = rd.choice(list(g.nodes()))
	if g.node[i]['state'] == 0:
		for j in list(g.neighbors(i)):
			if g.node[j]['state'] == 1:
				if pylab.random() < p_s:
					g.remove_edge(i,j)
				elif pylab.random() < p_i:
					g.node[i]['state'] = 1
	else:
		if pylab.random() < p_r:
			g.node[i]['state'] = 0

def observe():
	global g
	pylab.cla()
	nx.draw(g, cmap = pylab.cm.binary, vmin = 0, vmax =1, node_color = [g.node[i]['state'] for i in g.nodes()])

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [p_s_setter]).start(func=[init, observe, update])		
	

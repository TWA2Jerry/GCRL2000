import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd



def initialize():
	global g, nextg
	g = nx.barabasi_albert_graph(200, 5)
	g.pos = nx.spring_layout(g)
	for i in g.nodes():
		g.node[i]['state'] = 1 if random() < .5 else 0
	nextg = g.copy()

def observe():
	global g
	cla()
	nx.draw(g, cmap = cm.binary, vmin = 0, vmax = 1, node_color = [g.node[i]['state'] for i in list(g.nodes())], pos = g.pos)

p_i = 0.5 # infection probability
p_r = 0.5 # recovery probability

def p_i_setter(val = p_i):
	global p_i
	p_i = val
	return val

def p_r_setter(val = p_r):
	global p_r
	p_r = val
	return val
	

def update():
	global g, nextg
	for a in list(g.nodes()):
    		if g.node[a]['state'] == 0: # if susceptible
        		b = rd.choice(list(g.neighbors(a)))
        		if g.node[b]['state'] == 1: # if neighbor b is infected
          				nextg.node[a]['state'] = 1 if random() < p_i else 0
    		else: # if infected
        		nextg.node[a]['state'] = 0 if random() < p_r else 1
	g, nextg = nextg, g
	g.pos = nx.spring_layout(g)	

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [p_i_setter, p_r_setter]).start(func=[initialize, observe, update])

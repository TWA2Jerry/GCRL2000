import matplotlib
matplotlib.use('TkAgg')
import networkx as nx, pylab
import random as rd

p_s = 0.5

def init():
	global g
	g = nx.karate_club_graph()
	for i in g.nodes():
		g.node[i]['state'] = 1 if pylab.random() < 0.5 else 0
	g.pos = nx.spring_layout(g)
	
def update():
	global g
	i = rd.choice(list(g.nodes()))
	if g.degree[i] > 0:
		for j in list(g.neighbors(i)):
			if g.node[i]['state'] != g.node[j]['state']:
				if pylab.random() < p_s:
					g.remove_edge(i, j)
	listener = rd.choice(list(g.nodes))
	if(g.degree[listener] > 0):
		speaker = rd.choice(list(g.neighbors(listener)))
		g.node[listener]['state'] = g.node[speaker]['state']

def observe():
	global g
	pylab.cla()
	nx.draw(g, cmap = pylab.cm.binary, vmin = 0, vmax = 1, node_color = [g.node[i]['state'] for i in g.nodes()], pos = g.pos)
	
import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update]) 

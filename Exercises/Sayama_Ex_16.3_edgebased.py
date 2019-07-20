import matplotlib
matplotlib.use('TkAgg')
import networkx as nx, pylab
import random as rd

def init():
	global g
	g = nx.karate_club_graph()
	for i in g.nodes():
		g.node[i]['state'] = 1 if pylab.random() < 0.5 else 0
	
def update():
	global g
	chosenedge = rd.choice(list(g.edges()))
	if(pylab.random() < 0.5):
		listener = chosenedge[0]
		speaker = chosenedge[1]
	else:
		listener = chosenedge[1]
		speaker = chosenedge[0]
	g.node[listener]['state'] = g.node[speaker]['state']
	
def observe():
	global g
	pylab.cla()
	nx.draw(g, cmap = pylab.cm.binary, vmin = 0, vmax = 1, node_color = [g.node[i]['state'] for i in g.nodes()])
	
import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])
	

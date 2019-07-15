import matplotlib
matplotlib.use('TkAgg')
import networkx as nx, pylab


Dt = 0.01
alpha = 0.1
omega = 0.1
lamb = 0.1

def init():
	global g, nextg
	g = nx.karate_club_graph()
	for i in g.nodes():
		g.node[i]['state'] = pylab.randint(1,11)
	nextg = g.copy()	
	g.pos = nx.spring_layout(g)

def update():
	global g, nextg
	for i in g.nodes():
		c = g.node[i]['state']
		nextg.node[i]['state'] = c+(1j*omega*c+alpha*(\
		sum((g.node[j]['state'])**lamb for j in list(g.neighbors(i)))-g.degree(i)*c))*Dt
	g, nextg = nextg, g
	g.pos = nx.spring_layout(g)
	
		
def observe():
	global g
	pylab.cla()
	nx.draw(g, node_color = [g.node[i]['state'] for i in list(g.nodes())], pos = g.pos)	
	pylab.show()

import pycxsimulator
pycxsimulator.GUI().start(func = [init, observe, update])

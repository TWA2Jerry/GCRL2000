import matplotlib
matplotlib.use("TkAgg")
import pylab 
import networkx as nx

n_m = 100 #number of movable things
n_n = 1 #number of non-movable things
r = 0.1

class agent:
	pass

def init():
	global agents
	agents = []	
	for i in range(n_m):
		ag = agent()
		ag.x = pylab.random()
		ag.y = pylab.random()
		ag.can_move = True
		ag.type = 1 #1 means that while the thing might be stuck, it was once moveable
		agents.append(ag)
	ag = agent()
	ag.x = 0.5
	ag.y = 0.5
	ag.can_move = False
	ag.type = 0 #0 means that the thing is and always will be of the immovable type
	agents.append(ag)	

def update():
	global agents
	for ag in agents:
		if ag.can_move == True:
			immovable = [nb for nb in agents if (nb.x-ag.x)**2+(nb.y-ag.y)**2 < r**2 and nb.type == 0 and nb != ag]
			if len(immovable) > 0:
				ag.can_move=False
			else:
				ag.x = pylab.random()
				ag.y = pylab.random()

def observe():
	global agents
	pylab.cla()
	pylab.plot([nb.x for nb in agents], [nb.y for nb in agents], "ko")
	pylab.axis("image")
	pylab.axis([0,1,0,1])
	pylab.show()

import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])

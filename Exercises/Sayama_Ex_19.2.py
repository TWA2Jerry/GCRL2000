import matplotlib
matplotlib.use("TkAgg")
import networkx as nx, pylab

n = 1000 #number of agents
r = 0.1
th = 0.5

def n_setter(val = n):
	global n
	n = val
	return val

def r_setter(val = r):
	global r
	r = val
	return val

class agent:
	pass
	

def init():
	global agents
	agents = []
	for i in range(n):
		ag = agent()
		ag.x= pylab.random()
		ag.y=pylab.random()
		ag.color = 1 if pylab.random() < 0.5 else 0
		agents.append(ag)
	print(len(agents))
	
	

def update():
	global agents
	ag = agents[pylab.randint(n)]
	neighbourhood = [nb for nb in agents if (nb.x-ag.x)**2+(nb.y-ag.y)**2 < r**2 and nb != ag]
	num_similar = 0
	for j in neighbourhood:
		if j.color == ag.color:
			num_similar += 1
	if len(neighbourhood) > 0:
		ratio = num_similar/float(len(neighbourhood))
		if ratio < th:
			ag.x = pylab.random()
			ag.y = pylab.random()

def observe():
	global agents
	pylab.cla()
	white = [nb for nb in agents if nb.color == 0]
	black = [nb for nb in agents if nb.color == 1]
	pylab.plot([nb.x for nb in white], [nb.y for nb in white], "go")
	pylab.plot([nb.x for nb in black], [nb.y for nb in black], "ko")
	pylab.axis("image")
	pylab.axis([0,1,0,1])
	pylab.show()		

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [n_setter, r_setter]).start(func=[init, observe, update])		

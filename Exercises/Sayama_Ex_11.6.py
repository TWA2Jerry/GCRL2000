import matplotlib
matplotlib.use('TkAgg')
import pylab, numpy as np

n = 100
p = 0.5
w1 = 0.2
w2 = 0.05
R1 = 1
R2 = 2

def init():
	global config, nextconfig
	config = pylab.zeros([n,n])		
	for x in range(n):
		for y in range(n):
			config[x,y] = 1 if pylab.random() < p else 0
	nextconfig = pylab.zeros([n,n])

def update():
	global config, nextconfig
	for x in range(n):
		for y in range(n):
			strongcount = 0
			weakcount = 0
			for dx1 in range(-R1, R1):
				for dy1 in range(-R1, R1):
					strongcount += w1*config[(x+dx1)%n, (y+dy1)%n]	
			for dx2 in range(-R2, R2):
				for dy2 in range(-R2, R2):
					weakcount += w2*config[(x+dx2)%n, (y+dy2)%n]
			nextconfig[x,y] = 1 if strongcount > weakcount else 0
	config, nextconfig = nextconfig, config
								
	
def observe():
	global config
	pylab.cla()
	pylab.imshow(config, vmin = 0, vmax = 1, cmap = pylab.cm.binary)


import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])

	



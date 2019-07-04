import matplotlib
matplotlib.use('TkAgg')
import pylab, numpy as np

n = 100
p0 = 0.5
R = 1
k = 10

def init():
	global config, nextconfig
	config = pylab.zeros([n,n])
	for x in range(n):
		for y in range(n):
			config[x,y] = 1 if pylab.random() < p0 else 0
			
	nextconfig = pylab.zeros([n,n])
	
def update():
	global config, nextconfig
	for x in range(n):
		for y in range(n):
			if(config[x,y] > 0):
				nextconfig[x,y] = (config[x,y]+1)%k
			else:
				count  = 0
				for dx in range(-R, R):
					for dy in range(-R, R):
						count += config[(x+dx)%n, (y+dy)%n]
				p = count*0.1
				nextconfig[x,y] = config[x,y]+1 if pylab.random() < p else 0
	config, nextconfig = nextconfig, config

def observe():
	global config
	pylab.cla()
	pylab.imshow(config, vmin = 0, vmax = 1, cmap = pylab.cm.binary)

import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe, update])
		

import matplotlib
matplotlib.use('TkAgg')
import pylab, numpy as np

n = 100
pi = 0.1
ph = 0.5
p = 0.1

def init():
	global config, nextconfig
	config = pylab.zeros([n,n])
	for x in range(n):
		for y in range(n):
			c = pylab.random()
			if(c  < pi):
				config[x,y] = 2
			elif(c < ph):
				config[x,y] = 1
			else:
				config[x,y] = 0

	nextconfig = pylab.zeros([n,n])
	

def update():
	global config, nextconfig
	for x in range(n):
		for y in range(n):
			if(config[x,y] == 0):
				healthycount = 0
				for dx in [-1,0,1]:
					for dy in [-1,0,1]:
						if(config[(x+dx)%n, (y+dy)%n] == 1):
							healthycount += 1
				nextconfig[x,y] = 1 if pylab.random() < p*healthycount else 0
			elif(config[x,y] == 1):
				infectedcount = 0
				for dx in [-1, 0,1]:
					for dy in [-1,0,1]:
						if(config[(x+dx)%n, (y+dy)%n] == 2):
							infectedcount += 1
				nextconfig[x,y] = 2 if pylab.random() < p*infectedcount else 0
			else:
				nextconfig[x,y] = 0
	config, nextconfig = nextconfig, config

def observe():
	global config
	pylab.cla()
	pylab.imshow(config, vmin = 0, vmax = 1, cmap = pylab.cm.binary)
	
import pycxsimulator
pycxsimulator.GUI().start(func=[init, observe,update])			
			

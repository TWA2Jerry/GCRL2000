import matplotlib
matplotlib.use('TkAgg')
import pylab, numpy as np
import random

n = 100
p = 0.1
t = 0

def init():
	global config, nextconfig, densitylist, tarray
	config = pylab.zeros([n,n])
	count  = 0
	for x in range(n):
		for y in range(n):
			if(pylab.random() < p):
				config[x,y] = 1

			else:
				config[x,y] = 0
	
			count += config[x,y]
	density = count/(n**2)
	nextconfig = pylab.zeros([n,n])
	densitylist = [density]
	tarray = [t]
	pylab.figure()

def observe():
	global config, nextconfig, densitylist, tarray
	pylab.cla()
	pylab.imshow(config, vmin = 0, vmax = 1, cmap = pylab.cm.binary)
	pylab.plot(tarray, densitylist)
	pylab.show()	


def update():
	global config, nextconfig, densitylist, tarray, t
	count = 0
	for x in range(n):
		for y in range(n):
			panickcount = 0
			for dx in [-1,0,1]:
				for dy in [-1,0,1]:
					panickcount += config[(x+dx)%n, (y+dy)%n]	
			nextconfig[x,y] = 1 if panickcount >= 4 else 0
			count += nextconfig[x,y]	
	config, nextconfig = nextconfig, config
	density = count/(n**2) 
	t += 1
	tarray.append(t)
	densitylist.append(density)

import pycxsimulator
pycxsimulator.GUI().start(func=[init,observe,update])	


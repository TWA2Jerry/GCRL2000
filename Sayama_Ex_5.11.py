import matplotlib
matplotlib.use("TkAgg")
import pylab, numpy as np
import sys

def initialise():
	global t0, xlist, ylist
	xlist = [0.1]
	ylist = [0.1]
	t0 = 0

def init(a,b):
	global xlist, ylist, x,y
	x = a
	y = b
	xlist = [x]
	ylist = [y]

def update():
	global xlist, ylist, x, y
	nextx = x+y
	nexty = x
	x,y = nextx, nexty
	xlist.append(x)
	ylist.append(y)

def observe():
	global xlist, ylist
	pylab.show()

def iterate():
	global t0
	t0 += 3
	for x in np.arange(-2, 2, 0.4):
		for y in np.arange(-2, 2, 0.4):
			init(x,y)
			for t in range(t0+1):
				update()
			pylab.plot(xlist, ylist, "b")
	
import pycxsimulator
pycxsimulator.GUI().start(func=[initialise, iterate, observe])

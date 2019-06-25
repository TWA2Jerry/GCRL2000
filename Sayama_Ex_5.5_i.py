import pylab, numpy as np

def init():
	global x, xpast, xnow
	x = 0.1
	xpast = [x]
	xnow = [0]

def iterate():
	global x, xpast, xnow
	xpast.append(x)
	x = x+0.1
	xnow.append(x)
	xpast.append(x)
	xnow.append(x)

init()

for t in range(50):
	iterate()

pylab.plot(xpast, xnow, "r-")
pylab.show()

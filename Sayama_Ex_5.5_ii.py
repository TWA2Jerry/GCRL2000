import pylab, numpy as np

def init():
	global x, xpast, xnow, xeqpast, xeqnow
	x = 0.1
	xpast = [x]
	xnow = [0]
	xeqpast = []
	xeqnow = []

def iterate():
	global x, xpast, xnow, xeqpast, xeqnow
	xpast.append(x)
	xeqpast.append(x)
	x = 1.1*x
	xnow.append(x)
	xeqnow.append(x)
	xpast.append(x)
	xnow.append(x)

init()



for t in range(50):
	iterate()

	
	

xmax = max(xnow)

pylab.plot(xpast, xnow, "r-")
pylab.plot([0,xmax], [0,xmax], "g--")
pylab.plot(xeqpast,xeqnow, "b-")

pylab.show()

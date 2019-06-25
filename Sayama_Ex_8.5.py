import pylab, numpy as np

r = 4

def init():
	global x, xarray
	x = 0.1
	xarray = [x]
	

def iterate():
	global x, xarray
	xnext = r*x*(1-x)
	x = xnext
	xarray.append(x)

init()

for t in range(50):
	iterate()
	
pylab.plot(xarray)
pylab.xlabel("Time")
pylab.ylabel("x")
pylab.show()

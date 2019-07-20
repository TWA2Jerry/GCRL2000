import pylab, numpy as np

r = 1
K = 5
b = 1
c = 1
d = 1

def initialise():
	global x, y, xarray, yarray
	x = 1
	y = 1
	xarray = [x]
	yarray = [y]

def iterate():	
	global x, y, xarray, yarray
	xnext = x+r*x*(1-x/K)-(1-1/(b*y+1))*x
	ynext =  y-d*y+c*x*y
	x,y = xnext, ynext
	xarray.append(x)
	yarray.append(y)

initialise()

for t in range(100):
	iterate()

pylab.plot(xarray, "b-")
pylab.plot(yarray, "g--")

pylab.show()

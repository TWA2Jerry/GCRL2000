import pylab, numpy as np

rx = 0.5
ry = 0.5
Kx = 500
Ky = 700
a = 1
b = 1

def init():
	global x, y, xarray, yarray
	x = 5
	y = 5
	xarray = [x]
	yarray = [y]

def iterate():
	global x, y, xarray, yarray
	xnext = x+rx*x*(1-x/Kx)-(1-1/(a*y+1))*x
	ynext = y+ry*y*(1-y/Ky)-(1-1/(b*x+1))*y
	x,y = xnext, ynext
	xarray.append(x)
	yarray.append(y)

init()

for t in range(500):
	iterate()

pylab.plot(xarray, "g-")
pylab.plot(yarray, "b--")
pylab.show()

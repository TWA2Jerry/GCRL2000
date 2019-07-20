import pylab, numpy as np


a = 1
b = 1
c = 1
d = 1
Dt = 0.0001
t = 0.

def init():
	global x, y, xarray, yarray, tarray
	x = 0.1
	y = 0.1
	xarray = [x]
	yarray = [y]
	tarray = [t]


def iterate():
	global x, y, xarray, yarray, tarray, t
	xnext = x+(a*x-b*x*y)*Dt
	ynext = y+(-c*y+d*x*y)*Dt
	x,y = xnext, ynext
	xarray.append(x)
	yarray.append(y)
	t += Dt
	tarray.append(t)	

init()
for i in np.arange(0,50, Dt):
	iterate()

pylab.plot(tarray, xarray, "g-")
pylab.plot(tarray, yarray, "b--")
pylab.show() 

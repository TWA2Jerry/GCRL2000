import pylab, numpy as np

r = 0.2
K = 1.0
Dt = 0.1

def init():
	global x, xarray
	x = 0.1
	xarray = [x]

def iterate():
	global x, xarray
	x = x+r*x*(1-x/K)*Dt
	xarray.append(x)

init()
c = np.arange(Dt, 50, step = Dt)

for i in c:
	iterate()

d = np.insert(c, 0, 0)	
pylab.plot(d, xarray)
pylab.show()

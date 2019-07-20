import pylab, numpy as np 

def init(x0, y0):
	global x,y, xarray, yarray
	x = x0
	y = y0
	xarray = [x]
	yarray = [y]

def iterate():
	global x, y, xarray, yarray
	xnext = x+0.1*(x-x*y)
	ynext = y+0.1*(y-x*y)
	x,y = xnext, ynext
	xarray.append(x)
	yarray.append(y)

for x0 in np.arange(2, 4, 0.2):
	for y0 in np.arange(2,4,0.2):
		init(x0, y0)
		for t in range(10):
			iterate()

		pylab.plot(xarray, yarray, "b")
		pylab.xlabel("x")
		pylab.ylabel("y")
pylab.show() 

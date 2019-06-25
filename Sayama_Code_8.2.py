import pylab, numpy

def init(x0, y0):
	global x, y, xarray, yarray
	x = x0
	y = y0
	xarray = [x]
	yarray = [y]

def iterate(r):
	global x,y, xarray, yarray
		

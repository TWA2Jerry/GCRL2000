import pylab, numpy as np

def init():
	global x, xarray
	x = 0.001
	xarray = []

def update():
	global x, xarray
	x = (x**3)-r*x
	
def observe():
	global x, xarray
	xarray.append(x)

rs = np.linspace(0, 50, 1000, endpoint = True)

for r in rs:
	init()
	for t in range(100):
		update()

	for t in range(100):
		update()
		observe()
	pylab.plot([r]*100, xarray, "b.", alpha = 0.3)
	
pylab.show()

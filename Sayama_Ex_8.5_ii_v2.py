import pylab, numpy as np

def init():
	global x, xarray
	x = 0.1
	xarray = [] 

	
def update():
	global x, xarray
	x = r*x*(1-x)

def observe():	
	global x, xarray
	xarray.append(x)

c = np.linspace(0.1, 4, 200, endpoint = True)


for r in c:
	init()
	for t in range(100):
		update()
	for t in range(100):
		update()	
		observe()
	pylab.plot([r]*100, xarray, "b.", alpha = 0.3)

pylab.xlabel("r")
pylab.ylabel("xeq")
	
pylab.show()		

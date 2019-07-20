import pylab, numpy as np

def init():
	global xeq1,xeq2, xeq1array, xeq2array 
	xeq1 = 0.1
	xeq2 = 0.1
	xeq1array = []
	xeq2array = []	

def update():
	global xeq1,xeq2,xeq1array, xeq2array
	xeq1  = 1-1/r

def observe():	
	global xeq1,xeq2,xeq1array, xeq2array
	xeq1array.append(xeq1)
	xeq2array.append(xeq2)	


c = np.linspace(0.1, 4, 25, endpoint = True)


for r in c:
	init()
	for t in range(100):
		update()
	for t in range(100):
		update()	
		observe()
	pylab.plot([r]*100, xeq1array, [r]*100, xeq2array)

pylab.xlabel("r")
pylab.ylabel("xeq")
	
pylab.show()		

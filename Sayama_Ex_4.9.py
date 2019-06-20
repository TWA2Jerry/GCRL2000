import pylab, numpy as np

a = 2
K = 500

def initialise():
	global x, results
	x = 2
	results = [x]
	print(x)

def iterate():
	global x, results
	x = ((-(a-1)/K)*x+a)*x
	results.append(x)

initialise()

t = np.linspace(10, 500, num = 50)

for i in t:
	iterate()

pylab.plot(results)
pylab.show()


import pylab, numpy as np, math

K = 50
a = K+1

def initialise():
	global x, results
	x = 40
	results = [x]
	print(x)

def iterate():
	global x, results
	x = (a-math.sqrt((x-K)**2))
	results.append(x)

initialise()
for t in range(100):
	iterate()

pylab.plot(results)
pylab.show()

import pylab, numpy as np, math

def init():
	global x, xarray, dF, sum
	x = 0.1
	dF = 1-2*x
	sum = np.log(abs(dF))

def update():
	global x, dF, xarray, sum
	x = x+r-x**2
	dF = 1-2*x
	sum += np.log(abs(dF))

rs = np.linspace(0, 2, 100, endpoint = True)
lambdas = []
for r in rs:
	init()
	for t in range(100):
		update()
	lambdas.append(sum/102)

pylab.plot(rs, lambdas, "b-")

pylab.xlabel("r")
pylab.ylabel("Lyapunov exponent")
pylab.show()
	


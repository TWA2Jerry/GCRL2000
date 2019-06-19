import pylab

a  = 1.1

def initialise():
	
	global x, result
	x = 1.
	result = [x]

def observe():
	global x, result
	result.append(x)

def update():
	global x, result
	x = a*x

initialise()

for t in range(30):
	update()
	observe()	

	
pylab.plot(result)
pylab.show()



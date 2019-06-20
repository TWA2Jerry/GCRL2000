import pylab 

def initialise():

	global x, y, sequence
	x = 1
	y = 1
	sequence = [x,y]
def iterate():
	global x, y, sequence
	ynext = x
	xnext = x+y
	x,y = xnext, ynext

	sequence.append(x)

initialise()
for t in range(30):
	iterate()

pylab.plot(sequence)
pylab.show()

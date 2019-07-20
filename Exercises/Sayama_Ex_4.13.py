import pylab, numpy

r = 1
b = 1
c = 1
d = 0.01
K = 5

def init():
	global x, y, xlist, ylist
	x = y = 1
	xlist = [x]
	ylist = [y]

def update():
	global x, y, xlist, ylist
	nextx = x+r*x*(1-x/K)-(1-1/(b*y+1))*x
	nexty = y-d*y+c*x*y
	x, y = nextx, nexty	
def observe():
	global x,y,xlist, ylist
	xlist.append(x)
	ylist.append(y)

init()
for t in range(100):
	update()
	observe()

pylab.subplot(1,2,1)
pylab.plot(xlist, "b-")
pylab.plot(ylist,"g--")
pylab.subplot(1,2,2)
pylab.plot(xlist, ylist)
pylab.show()

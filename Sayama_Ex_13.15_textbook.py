import matplotlib
matplotlib.use('TkAgg')
import pylab, numpy as np

n = 100
Dh = 1. /n
Dt = 0.01

Da = 0.001
Db = 0.001

xvalues, yvalues = pylab.meshgrid(pylab.arange(0,1,Dh), pylab.arange(0,1,Dh))


def init():
	global a,b,nexta,nextb
	a = np.exp(-((xvalues-0.45)**2 + (yvalues-0.45)**2)/(0.3**2))
	b = np.exp(-((xvalues-0.55)**2 + (yvalues-0.55)**2)/(0.1**2))
	nexta = pylab.zeros([n,n])
	nextb = pylab.zeros([n,n])


def update():
	global a, b, nexta, nextb
	for x in range(n):
		for y in range(n):
			aC, aL, aR, aU, aD = a[x,y], a[(x-1)%n, y], a[(x+1)%1, y], a[x, (y+1)%n], a[x, (y-1)%n]
			bC, bL, bR, bU, bD = b[x,y], b[(x-1)%n, y], b[(x+1)%1, y], b[x, (y+1)%n], b[x, (y-1)%n]
			aLapNum = ((aR+aL)+(aU+aD)-4*aC)/((2*Dh)**2)
			bLapNum = ((bR+bL)+(bU+bD)-4*bC)/((2*Dh)**2)
			nexta[x,y] = aC+(Da*(((aR-aL)*(bR-bL)+(aU-aD)*(bU-bD))/(4*Dh**2)+bC*aLapNum))*Dt
			nextb[x,y] = bC+(Db*bLapNum)*Dt
	a,b, nexta,nextb = nexta, nextb, a,b

def observe():
	global a, b
	pylab.subplot(1,2,1)
	pylab.cla()
	pylab.imshow(a,vmin = 0, vmax = 1)
	pylab.title('a')
	pylab.subplot(1,2,2)
	pylab.cla()
	pylab.imshow(b, vmin = 0, vmax = 1)
	pylab.title('b')
	
import pycxsimulator
pycxsimulator.GUI(stepSize = 50).start(func = [init, observe, update])

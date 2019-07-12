import matplotlib
matplotlib.use('TkAgg')
import pylab

#Basic parameters
n = 100
Dt = 0.02
Dh = 1. / n

#Diffusion parameters
Du = 0.0001
Dv = 0.0006

#Turing Parameters
a, b,c,d,h,k = 1. , -1., 2. , -1.5, 1., 1.

def a_setter(val = a):
	global a
	a = float(val)
	return val

def b_setter(val = b):
	global b
	b = float(val)
	return val

def c_setter(val = c):
	global c
	c = float(val)
	return val

def d_setter(val = d):
	global d
	d = float(val)
	return val

def h_setter(val = h):
	global h
	h = float(val)
	return val

def k_setter(val = k):
	global k
	k = float(val)
	return val

def Du_setter(val = Du):
	global Du
	Du = float(val)
	return val

def Dv_setter(val = Dv):
	global Dv
	Dv = float(val)
	return val

def init():
	global u, v, nextu, nextv
	u = pylab.zeros([n,n])
	v = pylab.zeros([n,n])
	for x in range(n):
		for y in range(n):
			u[x,y] = 1. + pylab.uniform(-0.03, 0.03)
			v[x,y] = 1. + pylab.uniform(-0.03, 0.03)
	nextu = pylab.zeros([n,n])
	nextv = pylab.zeros([n,n])
	
def update():
	global u, v, nextu, nextv
	for x in range(n):
		for y in range(n):
			uC, uR, uL, uU, uD  = u[x,y], u[(x+1)%n, y], u[(x-1)%n, y], u[x, (y+1)%n], u[x, (y-1)%n]
			vC, vR, vL, vU, vD  = v[x,y], v[(x+1)%n, y], v[(x-1)%n, y], v[x, (y+1)%n], v[x, (y-1)%n]
			uLap = (uR+uL+uU+uD-4*uC)/(Dh)**2
			vLap = (vR+vL+vU+vD-4*vC)/(Dh)**2			
			
			nextu[x,y] = uC+(a*(uC-h)+b*(vC-k)+Du*uLap)*Dt
			nextv[x,y] = vC+(c*(uC-h)+d*(vC-k)+Dv*vLap)*Dt
	u, v, nextu, nextv = nextu, nextv, u, v
	

def observe():
	global u, v
	pylab.subplot(1,2,1)
	pylab.cla()
	pylab.imshow(u, vmin = 0, vmax = 2, cmap = pylab.cm.binary)
	pylab.title('u')
	pylab.subplot(1,2,2)
	pylab.cla()
	pylab.imshow(v, vmin = 0, vmax = 2, cmap = pylab.cm.binary)
	pylab.title('v')

import pycxsimulator
pycxsimulator.GUI(stepSize = 50).start(func=[init, observe, update])


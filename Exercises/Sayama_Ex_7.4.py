import pylab, numpy as np, math

Dt = 0.01
g = 9.8
L = 1

def init(w0, o0):
	global w, o, warray, oarray, t, tarray
	w = w0
	o = o0
	warray = [w]
	oarray = [o]
	t = 0.
	tarray = [t]

def iterate():
	global w, o, warray, oarray, t, tarray
	wnext = w+(-g/L)*math.sin(o)*Dt
	onext = o+(w)*Dt
	o, w = onext, wnext
	oarray.append(o)
	warray.append(w)
	t += Dt
	tarray.append(t)


for w0 in np.arange(0, 7, 1):
	for o0 in np.arange(0,7,1):
		init(w0, o0)
		for i in np.arange(Dt, 50, Dt):
			iterate()
		pylab.plot(oarray, warray)

pylab.show()

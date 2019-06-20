import pylab

def init():
	global px, py, pz, xarray, yarray, zarray
	px = 0.5
	py = 0.30
	pz = 0.20
	xarray = [px]
	yarray = [py]
	zarray = [pz]
	

def iterate():
	global px, py, pz, xarray, yarray, zarray

	if(px > py):
		sxy = (px-py)/100*py

	else:
		sxy = (px-py)/100*px

	if(py > pz):
		syz = (py-pz)/100*pz

	else:
		syz = (py-pz)/100*py

	if(px > pz):
		sxz = (px-pz)/100*pz

	else:
		sxz = (px-pz)/100*px

	px = px+sxy+sxz
	py = py-sxy+syz
	pz = pz-sxz-syz
	xarray.append(px)
	yarray.append(py)
	zarray.append(pz)

init()

for t in range(1000):
	iterate()

pylab.plot(xarray, "b-")
pylab.plot(yarray, "g+")
pylab.plot(zarray, "ro")

pylab.show()

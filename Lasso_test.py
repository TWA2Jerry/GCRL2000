import pylab, numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

def init():
	global x, xarray
	x = 0.1
	xarray = [x]

def iterate():
	global x, xarray
	x = 4*x*(1-x)
	xarray.append(x)

def lists(tau):
	global x, xarray
	varray = []
	xtarray = []
	
	i = 0
	while(i < len(xarray)-1):
		v = [xarray[i]]
		varray.append(v)
		xtarray.append(xarray[i+1])
		i += 1
	return varray, xtarray

init()
print("Initialisation done!")
for t in range(100):
	iterate()

print("Iteration done!")
a,b = lists(1)
poly = PolynomialFeatures(degree = 2, include_bias = False)
c = poly.fit_transform(a)
print(c)
print(b)


reg = linear_model.Lasso()
d = reg.fit(c,b)
y_pred = reg.predict(c)
print(d.coef_)
pylab.plot(a,b, "ro")
pylab.plot(c, y_pred, "b-")
pylab.show()

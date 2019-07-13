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
		v = [xarray[i]+pylab.uniform(-0.03, 0.03)]
		varray.append(v)
		xtarray.append(xarray[i+1]+pylab.uniform(-0.05, 0.05))
		i += tau
	return varray, xtarray

init()
print("Initialisation done!")
for t in range(1000000):
	iterate()

print("Iteration done!")
a,b = lists(1)
poly = PolynomialFeatures(degree = 2, include_bias = False)
c = poly.fit_transform(a)
reg = linear_model.Lasso(alpha = 0.1, tol =0.01)
reg.fit(c,b)
print(reg.coef_)

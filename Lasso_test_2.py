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
	i = 2*tau
	while(i < len(xarray)-1):
		v = [xarray[i], xarray[i-tau], xarray[i-2*tau]]
		varray.append(v)
		xtarray.append(xarray[i+1]+pylab.uniform(-0.05, 0.05))
		i += 1
	return varray, xtarray

init()
print("Initialisation done!")
for t in range(10000):
	iterate()

print("Iteration done!")
a,b = lists(1)
poly = PolynomialFeatures(degree = 2, include_bias = False)
c = poly.fit_transform(a)

reg = linear_model.Lasso(alpha=0.0001, fit_intercept = True)
d = reg.fit(c,b)
y_pred = reg.predict(c)
print(d.coef_)
pylab.plot([i[0] for i in a],b, "ro")
pylab.plot([i[0] for i in a], y_pred, "bo")
pylab.show()

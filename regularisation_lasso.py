import pylab, numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


def init():
	global x, xarray
	x = 0.9
	xarray = [x]


def update():
	global x, xarray
	x = 4*x*(1-x)

def observe():
	global x, xarray
	xarray.append(x+pylab.uniform(-0.05, 0.05))
	
def lists():
	global x, xarray
	varray = []
	xtarget = []
	#This bit needs to iterate through and create two lists: one for the target x, and one for the previous arguments
	#Currently the argument list is just two dimensional
	for i in range(1, len(xarray)-1):
		v = [xarray[i-1], xarray[i]]
		varray.append(v)
		xtarget.append(xarray[i+1])
	return varray, xtarget

init()
for t in range(1000):
	update()
	observe()

varray, xtarget = lists()

#This is drawing on the scikit-learn tutorial
poly = PolynomialFeatures(degree = 2, include_bias = False)
c = poly.fit_transform(varray)

reg = linear_model.Lasso(alpha = 0.1, copy_X = True, fit_intercept = True, max_iter = 10000, normalize = False, positive = False, precompute=False, random_state=None, selection='cyclic',tol=0.0001, warm_start=False)
a = reg.fit(c, xtarget)
print(a.coef_)

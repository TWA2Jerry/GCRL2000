import pylab, numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime

def lists(tau):
	varray = []
	targetarray = []
	times_array = []
	full_prices_array = []
	full_times_array = []
	with open("BHP.csv", "r") as file1:
		lines1 = file1.readlines()
		with open("^AXJO.csv", "r") as file2:
			lines2 = file2.readlines()
			i = tau+1 #So what we're doing is this, we want the data from a while back to predict tau periods into the future, which is why we're giving tau+1, because i-tau will give 1 initially 
			while(i<min(len(lines1), len(lines2))):
				line1 = lines1[i-tau].split(",")
				line2 = lines2[i-tau].split(",")
				targetline = lines1[i].split(",")
				v = [float(line1[4]), float(line2[4])]
				varray.append(v)
				targetarray.append(float(targetline[4]))
				times_array.append(datetime.strptime(targetline[0], "%Y-%m-%d"))
				i += tau
		j = 1
		while(j < len(lines1)):
			line = lines1[j].split(",")
			full_prices_array.append(float(line[4]))
			full_times_array.append(datetime.strptime(line[0], "%Y-%m-%d"))
			j += 1 
	return varray, targetarray, times_array, full_prices_array, full_times_array


a,b,t,p, ft = lists(5)
poly = PolynomialFeatures(degree = 2, include_bias = False)
c = poly.fit_transform(a)
reg = linear_model.Lasso(alpha = 0.001, fit_intercept = False)
d = reg.fit(c,b)

"""
This is to force the price of BHP itself to go to 0
reg.coef_[0] = 0
"""

"""
This is to force everything except the price of BHP to go to 0
for i in range(1, len(reg.coef_)):
	reg.coef_[i] = 0
"""
y_pred = reg.predict(c)
print(reg.coef_)
pylab.plot(ft, p, "g-", label = "Real")
pylab.plot(t, y_pred, "b--", label = "Predicted")
pylab.legend()
pylab.ylim(0,60)
pylab.show()			

import pylab, numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

def lists():
	varray = []
	targetarray = []
	with open("BHP.csv", "r") as file1:
		with open("^AXJO.csv", "r") as file2:
			lines1 = file1.readlines()
			lines2 = file2.readlines()
			i = 1
			while(i<min(len(lines1), len(lines2))-1):
				line1 = lines1[i].split(",")
				line2 = lines2[i].split(",")
				targetline = lines1[i+1].split(",")
				v = [float(line1[4]), float(targetline[1]), float(line2[4])]
				varray.append(v)
				targetarray.append(float(targetline[4]))
				i += 1
	return varray, targetarray


a,b = lists()
poly = PolynomialFeatures(degree = 2, include_bias = False)
c = poly.fit_transform(a)
reg = linear_model.Lasso(alpha = 0.001, fit_intercept = False)
d = reg.fit(c,b)
y_pred = reg.predict(c)
print(d.coef_)
pylab.plot(b, "g-", label = "Real")
pylab.plot(y_pred, "b--", label = "Predicted")
pylab.legend()
pylab.ylim(min(b)-10, max(b)+10)
pylab.show()			

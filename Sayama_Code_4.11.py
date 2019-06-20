import pylab

a = 0.5
b = -0.5

def initialise():
	
	global x,y, x_array, y_array
	x = 1.
	y = 1.
	x_array = [x]
	y_array = [y]


def observe():
	global x,y, x_array, y_array
	x_array.append(x)
	y_array.append(y)


def update():
	global x, y, x_array, y_array
	xnext = a*x+y
	ynext = b*x+y
	x,y = xnext, ynext

initialise()

for t in range(30):
	update()
	observe()	

	
pylab.plot(x_array, y_array)
pylab.show()



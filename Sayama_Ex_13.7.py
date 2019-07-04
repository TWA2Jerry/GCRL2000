import pylab, numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math


xvalues, yvalues = pylab.meshgrid(np.arange(-4,4,0.1), np.arange(-4,4,0.1))

def init():
	global zarray
	zarray = pylab.sin(xvalues*yvalues)

init()
ax = pylab.gca(projection='3d')

ax.plot_surface(xvalues,yvalues,zarray)

pylab.show()

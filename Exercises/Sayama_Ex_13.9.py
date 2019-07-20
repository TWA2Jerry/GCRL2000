import pylab, numpy as np
from mpl_toolkits.mplot3d import Axes3D

xvalues, yvalues = pylab.meshgrid(np.arange(-4,4,0.1), np.arange(-4,4, .1))

zvalues  = -(yvalues**2)*np.sin(xvalues*yvalues)-(xvalues**2)*np.sin(xvalues*yvalues)

ax = pylab.gca(projection='3d')

ax.plot_surface(xvalues, yvalues, zvalues)

pylab.show()

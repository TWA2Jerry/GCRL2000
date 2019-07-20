import pylab, numpy as np
import math
xvalues, yvalues = pylab.meshgrid(np.arange(-4,4, 0.1), np.arange(-4,4,0.1))

vx = yvalues*np.cos(xvalues*yvalues)
vy = xvalues*np.cos(xvalues*yvalues)

pylab.streamplot(xvalues, yvalues, vx, vy)

pylab.show()

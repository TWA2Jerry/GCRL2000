import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

params = { 'figure.figsize': (8,8),
          'axes.labelsize': 40,
          'lines.linewidth': 2,
          #'text.fontsize': 12,
          #'lines.color': 'r',
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
          # 'legend.fontsize': 10,
          # 'title.fontsize': 12,
          # 'text.usetex': False,
          # 'font': 'Helvetica',
          #'mathtext.bf': 'helvetica:bold',
          # 'xtick.major.pad': 6,
          # 'ytick.major.pad': 6,
          # 'xtick.major.size': 5,
          # 'ytick.major.size': 5,
          # 'xtick.minor.size': 3,      # minor tick size in points
          # 'xtick.major.width': 1.,    # major tick width in points
          # 'xtick.minor.width': 1.,    # minor tick width in points
          # 'ytick.minor.size': 3,      # minor tick size in points
          # 'ytick.major.width': 1.,    # major tick width in points
          # 'ytick.minor.width': 1.,    # minor tick width in points
          # 'tick.labelsize': 'small'
           }

plt.rcParams.update(params)



def dynamics(x,t,a=0.2, beta=0.2, gamma=5.7):
	xdot = np.zeros(3)
	xdot[0] = -x[1] - x[2]
	xdot[1] = x[0] + a*x[1]
	xdot[2] = beta + x[2]*(x[0]-gamma)
	return xdot 


x_init = np.random.uniform(0.1,0.5,3)

t_init=0; t_final = 300; t_step = 0.01
tpoints = np.arange(t_init,t_final,t_step)

transient=int(0.8*len(tpoints))

a=0.2; beta=0.2; gamma=5.7; alpha=0.03
y = odeint(dynamics, x_init, tpoints,args=(a,beta,gamma), hmax = 0.01)

plt.figure()
plt.plot(y[:,0],y[:,1],'k')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.xlim([-12,12])
plt.ylim([-12,12])
plt.tight_layout()

plt.show()

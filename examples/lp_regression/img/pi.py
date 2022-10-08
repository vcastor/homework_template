import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')
axis_font = {'size':'16'}
#mpl.rcParams['errorbar.capsize'] = 3
from matplotlib import rcParams
rcParams.update({'font.size': 16})
rcParams.update({'figure.autolayout': True})

### Dibujaremos
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()
ax1 = fig.add_subplot(111)  

####################
x = [-np.pi/2, -np.pi/3, 0, np.pi/3, np.pi/2]
x1 = np.arange(-3,3, 0.01)
y = [0, 0.5, 1, 0.5, 0]
y1 = -0.397*x1**2 + 0.966
y2 = np.cos(x1)

# Space of ploting
plt.xlim((-2.2, 2.2))
plt.ylim((-0.2, 1.2))

# Plot
ax1.plot(x1, y1, '-', c='red',   label=r'$y = -0.397x^2 + 0.966$')
ax1.plot(x1, y2, '-', c='green', label=r'$y = \cos(x)$')
ax1.plot(x,  y,  'o', c='blue',  label='data points, $r^2 = 0.9951$')

# Notes n' legends
leg = ax1.legend(loc='lower center')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

#####################
#plt.show()
pwd = os.popen("pwd").read()
pwd = pwd.rstrip() + "/img/"
fig.savefig(pwd+'pi.pdf')

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
x = [-3, -1, 0, 1, 2]
x1 = np.arange(-4,3,0.01)
y = [4, 1, 0, 2, 5]
y1 = 0.094*x1**3 + 0.799*x1**2 + 0.352*x1 + 0.431

# Space of ploting
plt.xlim((-4,3))
plt.ylim((-2, 10))

# Plot
ax1.plot(x1, y1, '-', c='red',   label=r'$y = 0.094x^3 + 0.799x^2 + 0.352x - 0.431$')
ax1.plot(x,  y,  'o', c='blue',  label='data points, $r^2 = 0.9982$')

# Notes n' legends
leg = ax1.legend(loc='upper left')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

#####################
#plt.show()
pwd = os.popen("pwd").read()
pwd = pwd.rstrip() + "/img/"
fig.savefig(pwd+'7.pdf')

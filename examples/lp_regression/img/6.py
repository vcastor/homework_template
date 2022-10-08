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
x = [1, 2, 3, 5, 6]
x1 = np.arange(0,7,0.01)
y = [1, 4, 4, 1, 2]
y1 = 0.304*x1**3 - 3.462*x1**2 + 11.369*x1 - 7.236

# Space of ploting
plt.ylim((-8,8))
plt.xlim((0, 7))

# Plot
ax1.plot(x1, y1, '-', c='red',   label=r'$y = 0.304x^3 - 3.462x^2 + 11.369x - 7.236$')
ax1.plot(x,  y,  'o', c='blue',  label='data points, $r^2 = 0.9982$')

# Notes n' legends
leg = ax1.legend(loc='lower right')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

#####################
#plt.show()
pwd = os.popen("pwd").read()
pwd = pwd.rstrip() + "/img/"
fig.savefig(pwd+'6.pdf')

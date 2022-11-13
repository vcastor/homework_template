##############################################
### Raw data

import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl 
mpl.style.use('classic')

###############################################
### Abrir data

x  = []
hf = []
cc = []
ci = []

archivo = open('dzp.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3])
    x.append(float(columns[0]))
    hf.append(float(columns[1]))
    cc.append(float(columns[2]))
    ci.append(float(columns[3]))
archivo.close()

plt.plot(x,hf, color='red', marker='.', label=r'Hartree-Fock')
plt.plot(x,cc, color='blue', marker='.', label=r'Coupled Cluster')
plt.plot(x,ci, color='green', marker='.', label=r'Configuration Interaction')

###############################################
### Espacio de dibujo

plt.xlim((1.0, 6.0))
plt.ylim((-328.32,-328.0))

###############################################
### Notas

#plt.title('titulo')
leg = plt.legend(loc='center right')
plt.xlabel('Distance $\mathrm{(\AA)}$')
plt.ylabel(r'E $\mathrm{(E_h)}$')

# Shrink current axis by 20%
#ax = plt.subplot(111)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


###############################################
### Imprimir

plt.savefig('dzp.pdf')
plt.show()


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

x       = []
hfbsse  = []
ccbsse  = []
cibsse  = []
hf      = []
cc      = []
ci      = []

archivo = open('bsse.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6])
    x.append(float(columns[0]))
    hfbsse.append(float(columns[1]))
    ccbsse.append(float(columns[2]))
    cibsse.append(float(columns[3]))
    hf.append(float(columns[4]))
    cc.append(float(columns[5]))
    ci.append(float(columns[6]))
archivo.close()

plt.plot(x,hfbsse, color='red', marker='.', label=r'HF Counter-Poise correction')
plt.plot(x,hf, color='red', linestyle='-.', label=r'HF without correction')
plt.plot(x,ccbsse, color='green', marker='.', label=r'CC-SD Counter-Poise correction')
plt.plot(x,cc, color='green', linestyle='-.', label=r'CC-SD without correction')
plt.plot(x,cibsse, color='blue', marker='.', label=r'CI-SD Counter-Poise correction')
plt.plot(x,ci, color='blue', linestyle='-.', label=r'CI-SD witout correction')

###############################################
### Espacio de dibujo

plt.xlim((1.3, 6.0))
plt.ylim((-328.32,-327.88))

###############################################
### Notas

#plt.title('titulo')
leg = plt.legend(loc='upper right')
plt.xlabel('Distance $\mathrm{(\AA)}$')
plt.ylabel(r'E $\mathrm{(E_h)}$')


###############################################
### Imprimir

plt.savefig('bsse.pdf')
plt.show()


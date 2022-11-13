### Raw data

import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl 
mpl.style.use('classic')

### Abrir data

x       = []
#hfdzp   = []
#hftzp   = []
#hfqzp   = []
ccdzp   = []
cctzp   = []
cclim   = []
cidzp   = []
citzp   = []
ciqzp   = []
cilim   = []

archivo = open('basis_limit.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6]), float(columns[7])#, float(columns[8]), float(columns[9]), float(columns[10])
    x.append(float(columns[0]))
    #hfdzp.append(float(columns[1]))
    #hftzp.append(float(columns[2]))
    #hfqzp.append(float(columns[3]))
    ccdzp.append(float(columns[1]))
    cctzp.append(float(columns[2]))
    cclim.append(float(columns[3]))
    cidzp.append(float(columns[4]))
    citzp.append(float(columns[5]))
    ciqzp.append(float(columns[6]))
    cilim.append(float(columns[7]))
archivo.close()

#plt.plot(x,hfdzp, color='red', marker='.', label=r'HF Sapporo-DZP')
#plt.plot(x,hftzp, color='red', marker='x', label=r'HF Sapporo-TZP')
#plt.plot(x,hfqzp, color='red', marker='+', label=r'HF Sapporo-QZP')
plt.plot(x,ccdzp, color='red', marker='.', label=r'CC-SD Sapporo-DZP')
plt.plot(x,cctzp, color='red', marker=',', label=r'CC-SD Sapporo-TZP')
plt.plot(x,cclim, color='red', linestyle='-.', label=r'CC-SD Sapporo-Limit')
plt.plot(x,cidzp, color='blue', marker='.', label=r'CI-SD Sapporo-DZP')
plt.plot(x,citzp, color='blue', marker=',', label=r'CI-SD Sapporo-TZP')
plt.plot(x,ciqzp, color='blue', marker='+', label=r'CI-SD Sapporo-QZP')
plt.plot(x,cilim, color='blue', linestyle='-.', label=r'CI-SD Sapporo-Limit')

### Espacio de dibujo

plt.xlim((0.5, 3.0))
plt.ylim((-0.4,-0.12))

### Notas

#plt.title('titulo')
#leg = plt.legend(loc='upper right')
plt.xlabel('Distance $\mathrm{(\AA)}$')
plt.ylabel(r'E $\mathrm{(E_h)}$')

plt.tight_layout(rect=[0,0,0.75,1])
leg = plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
# Shrink current axis by 20%
#ax = plt.subplot(111)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])

# Put a legend to the right of the current axis
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


### Imprimir

plt.savefig('basis_limit_.pdf')
plt.show()


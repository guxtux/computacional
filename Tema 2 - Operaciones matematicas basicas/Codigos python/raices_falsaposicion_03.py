# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:14:39 2020

@author: gusto
"""

from raices_falsaposicion_01 import FalsPos
import matplotlib.pyplot as plt
import numpy as np

#%%
#Programa principal

def f(x):
    return np.exp(x) - 3*x**2

a = np.array([0., 3.])
b = np.array([1., 5.])
raices = []
for i in range(2):
    raiz, bandera = FalsPos(f, a[i], b[i])
    
    raices.append(raiz)
    if bandera == 0:
        print('Se encontró la raíz en x = {0:1.10f}'.format(raiz))
    elif bandera == 1:
        print('No hay raíces en el intervalo ({0:1.3f}, {1:1.3f})'.format(a, b))
    else:
        print('Se excedió el número de iteraciones')
#%%

#%%
#Rutina de graficación
    
x0 = np.linspace(-5, 5, 200)
#x1 = np.linspace(a, b, 200)

def ejes():
    plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    plt.axvline(x=0, ls='dashed', lw=0.7, color='k')


plt.figure(1)
plt.plot(x0, f(x0))
plt.title('Gráfica de la función')
plt.axis([-5, 5, -20, 20])
ejes()

plt.figure(2)
plt.plot(x0, f(x0))
plt.plot(raices[0], 0, 'bo')
plt.plot(raices[1], 0, 'ro')
plt.title('Gráfica de la función con las raíces')
plt.axis([0, 5, -10, 10])
plt.text(1, 2, '$x_{0} = $' +str(round(raices[0],5)))
plt.text(4, 2, '$x_{1} = $' +str(round(raices[1],5)))
ejes()

plt.show()
#%%
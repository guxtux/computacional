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
    return np.cos(x) - x

a, b = 0., 1

raiz, bandera = FalsPos(f, a, b)

if bandera == 0:
    print('Se encontró la raíz en x = {0:1.10f}'.format(raiz))
elif bandera == 1:
    print('No hay raíces en el intervalo ({0:1.3f}, {1:1.3f})'.format(a, b))
else:
    print('Se excedió el número de iteraciones')
#%%

#%%
#Rutina de graficación
    
x0 = np.linspace(-2*np.pi, 2*np.pi, 200)
x1 = np.linspace(a, b, 200)

def ejes():
    plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    plt.axvline(x=0, ls='dashed', lw=0.7, color='k')


plt.figure(1)
plt.plot(x0, f(x0))
plt.title('Gráfica de la función en el intervalo $(-2 \, \pi, 2 \, \pi)$')
plt.xlim(-2*np.pi, 2*np.pi)
ejes()

plt.figure(2)
plt.plot(x1, f(x1))
plt.title('Gráfica de la función en el intervalo $(0, 1)$')
plt.xlim(0, 1)
ejes()

plt.figure(3)
plt.plot(x1, f(x1))
plt.plot(raiz, 0, 'ro')
plt.title('Gráfica de la función con la raíz')
plt.xlim(0, 1)
plt.text(0.7, 0.4, 'x = ' +str(round(raiz,10)))
ejes()

plt.show()
#%%
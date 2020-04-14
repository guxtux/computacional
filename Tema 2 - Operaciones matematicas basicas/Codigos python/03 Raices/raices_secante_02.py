# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:19:57 2020

@author: gusto
"""

from raices_secante_01 import Secante
import matplotlib.pyplot as plt
import numpy as np

#%%
#Programa principal

def f(x):
    return x - np.sin(x) - 0.25

x0 = 1.
a, b = 0., 2.

raiz, bandera = Secante(f, a, b, x0)
    
if bandera == 0:
    print('Se encontró la raíz en x = {0:1.10f}'.format(raiz))
elif bandera == 1:
    print('No hay raíces en el intervalo ({0:1.3f}, {1:1.3f})'.format(a, b))
else:
    print('Se excedió el número de iteraciones')
#%%

#%%
#Rutina de graficación
    
xf = np.linspace(-5, 5, 200)

def ejes():
    plt.plot(xf, f(xf), 'b')
    plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    plt.axvline(x=0, ls='dashed', lw=0.7, color='k')


plt.figure(1)
ejes()
plt.title('Gráfica de la función')
plt.axis([-3, 3, -3, 3])


plt.figure(2)
ejes()
plt.plot(raiz, 0, 'ro')
plt.title('Gráfica de la función con la raíz')
plt.axis([0, 1.5, -0.5, 0.5])
plt.text(1, 0.1, '$x_{0} = $' +str(round(raiz,5)))
ejes()

plt.show()
#%%
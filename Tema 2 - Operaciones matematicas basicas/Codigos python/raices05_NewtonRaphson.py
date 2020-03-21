# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:41:46 2020

@author: gusto
"""

from ModuloRaices import buscaraiz, newtonRaphson
import matplotlib.pyplot as plt
import numpy as np

def f(x): return np.sin(x) + 3 * np.cos(x) - 2
def df(x): return np.cos(x) - 3 * np.sin(x)

intervalo1 = []
intervalo2 = []

inicio, final, dx = -2., 2. , 0.01

a1, b1 = buscaraiz(f, inicio, final, 0.1)
print('Una raiz está en [{0:}, {1:}]'.format(round(a1, 2), round(b1, 2)))
intervalo1.append(a1)
intervalo1.append(b1)

inicio = b1

a2, b2 = buscaraiz(f, inicio, final, 0.1)
print('Una raiz está en [{0:}, {1:}]'.format(round(a2, 2), round(b2, 2)))
intervalo2.append(a2)
intervalo2.append(b2)

raiz1 = newtonRaphson(f, df, intervalo1[0], intervalo1[-1], 1.e-4)
print(raiz1)

raiz2 = newtonRaphson(f, df, intervalo2[0], intervalo2[-1], 1.e-4)
print(raiz2)

x = np.linspace(-2,2)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.plot(x, f(x), color='g')
plt.plot(raiz1, 0, 'ro', label='Raiz 1 = ' + str(round(raiz1, 3)))
plt.plot(raiz2, 0, 'bo', label='Raiz 2 = ' + str(round(raiz2, 3)))
plt.legend(loc='lower right')
plt.title('Gráfica que muestra las dos raíces de la función')
plt.show()
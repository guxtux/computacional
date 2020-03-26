# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:14:32 2020

@author: gusto
"""

from ModuloRaices import buscaraiz
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x**2 - 1)

def ejes():
    plt.plot(x0, f(x0))
    plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
    plt.axis([-4, 4, -3, 15])

a, b, dx = -2., 2., 0.1

x0 = np.linspace(-5, 5, 100)

intervalo1 = []
intervalo2 = []
raices = []

inicio = a
final = 0.

a1, b1 = buscaraiz(f, inicio, final, dx)

inicio = final
final = b
a2, b2 = buscaraiz(f, inicio, final, dx)

raiz1 = optimize.bisect(f, a1, b1)
raiz2 = optimize.bisect(f, a2, b2)

print('La raíz está en x = {0:1.6f}'.format(raiz1))
print('La raíz está en x = {0:1.6f}'.format(raiz2))

raices.append(raiz1)
raices.append(raiz2)

plt.figure(1)
ejes()
plt.title('Grafica de la función')


plt.figure(2)
plt.plot(raices[0], 0, 'ro')
plt.plot(raices[1], 0, 'ro')
plt.text(-1.5, -1.5, '$x_{0} = -1.0$')
plt.text(1.5, 0.5, '$x_{1} = 1.0$')
plt.title('Raíces de la función usando optimize.bisect', style='italic')
ejes()


plt.show()
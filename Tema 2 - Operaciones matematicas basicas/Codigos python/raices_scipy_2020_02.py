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
    return (x**3 - 1)

def ejes():
    plt.plot(x0, f(x0))
    plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
    plt.axis([-2, 2, -5, 5])

x0 = np.linspace(-5, 5, 100)

raiz = optimize.newton(f, 1.5)
#raiz2 = optimize.bisect(f, a2, b2)
#
print('La raíz está en x = {0:}'.format(raiz))
#print('La raíz está en x = {0:1.6f}'.format(raiz2))
#
#raices.append(raiz1)
#raices.append(raiz2)

plt.figure(1)
ejes()
plt.title('Grafica de la función')


plt.figure(2)
plt.plot(raiz, 0, 'ro')
plt.text(0.25, -1.5, '$x_{0} = $' + str(raiz))
#plt.text(1.5, 0.5, '$x_{1} = 1.0$')
plt.title('Raíces de la función usando optimize.newton', style='italic')
ejes()


plt.show()
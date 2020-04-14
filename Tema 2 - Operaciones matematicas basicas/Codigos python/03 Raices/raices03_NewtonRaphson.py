# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:16:44 2012

@author: IIFCES
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752
def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538

def newtonRaphson(x, tol=1e-09):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x,i
    print('Son demasiadas iteraciones\n')

raiz, numIter = newtonRaphson(2.0)

x0 = np.linspace(0., 5., 200)

#%%
#Calcula las raíces de la función usando scipy

polinomio = [1., -6.4, 6.45, 20.538, -31.752]
xp = sp.arange(0, 5,.02)
y = sp.polyval(polinomio, xp)
raices = sp.roots(polinomio)
s = sp.polyval(polinomio, raices)
#%%
print('Raiz = {0:}'.format(raiz))
print('Numero de iteraciones = {0:d}'.format(numIter))

#%%
#Rutina de graficación

plt.plot(x0, f(x0))
plt.plot(raices, s, 'ro')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.title('Gráfica de la función $f(x)$')
plt.axis([0, 5, -10, 10 ])
plt.show()
#%%
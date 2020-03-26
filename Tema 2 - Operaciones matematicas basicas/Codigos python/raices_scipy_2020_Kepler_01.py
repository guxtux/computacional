# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:39:52 2020

@author: gusto
"""

from math import pi, sin, cos
from scipy.optimize import newton
import matplotlib.pyplot as plt

def Func(E):
  global e, M
  f = E - e * sin(E) - M
  return f

def ejes():
    plt.plot(x, y)
    plt.xlabel('E')
    plt.ylabel('f(E)')
    plt.xlim([0, 1])
    plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
    
def graficacion1():
    plt.figure(1)
    ejes()
    plt.title('Gráfica de la función de Kepler')
    
    
    plt.figure(2)
    plt.plot(raiz, 0, 'ro')
    plt.text(0.2, 0.050, '$x_{0}$ = ' + str(raiz))
    plt.text(0.2, 0.035, 'en t = ' + str(t))
    plt.title('Gráfica de la función de Kepler con la raíz $x_{0}$')
    ejes()
    
    
    plt.show()
    
#%%
# Valores
    
pi2 = 2e0 * pi
n = 101
x = [0]*(n+1); y = [0]*(n+1)

e  = 0.9672671e0
T = 75.96e0
t0 = 1986.1113e0

t = 1986.2491e0
M = pi2 / T * (t-t0)
Emax = 1e0
h = Emax / (n-1)
#%%

#%%
# Valor de la raíz de f(E), inciso 1 del problema

for i in range(1, n+1):
  E = (i-1)*h
  x[i] = E
  y[i] = Func(E)

raiz = newton(Func, 0.1, lambda E: 1e0-e*cos(E))

print('La raíz se encuentra en x = {0:} en t = {1:}'.format(raiz, t))
#%%

graficacion1()

#%%
# Cálculo de M(t), solución al inciso 2 del problema

h = T / (n-1)

x[1] = t0; y[1] = E = 0e0

for i in range(2, n+1):
   t = t0 + (i-1)*h
   M = pi2 / T * (t - t0)
   E = newton(Func, E, lambda E: 1e0-e*cos(E))                # solve Kepler's equation
   x[i] = t; y[i] = E

#%%
plt.figure(3)
plt.plot(x[1:], y[1:])
plt.title('Período completo del cometa Halley')
plt.xlabel('t (años)')
plt.ylabel('E')
plt.axis([1980, 2065, 0, 7])
plt.show()
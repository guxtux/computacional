# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:07:33 2020

@author: gusto
"""

from numpy import zeros, array, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(y, t, R, L) : 
    C = 0.001
    E = 1.0
            
    F = zeros(2)
    F[0] = y[1]
    F[1] = -(R/L)*y[1] - (1.0/(L*C))*y[0] + E/L
    return F

t = linspace(0.0, 5.0, 200)
y0 = array([0., 0.])
h = 0.01

L = 200.0
R = [0., 50, 100, 500]

for r in R:
    sol = odeint(F, y0, t, args=(r, L))
    plt.plot(t,sol[:,1], label='R = ' + str(r) + ' $\Omega$')

plt.axhline(y=0, lw=0.75, ls='dashed', color='k')
plt.legend(loc='best')
plt.title('Solución de la EDO para diferentes valores de $R$')
plt.xlim([0,5])
plt.show()

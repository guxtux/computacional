# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:45:17 2020

@author: gusto
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def F(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b * omega - c * np.sin(theta)]
    return dydt

b = 0.25
c = 5.0

y0 =  [np.pi - 0.1, 0.0]

t = np.linspace(0., 10., 101)

sol = odeint(F, y0, t, args=(b, c))

plt.figure(1)
plt.plot(t, sol[:,0], 'b', label='theta(t)')
plt.plot(t, sol[:,1], 'g', label='omega(t)')
plt.xlabel('t')
plt.xlim([0, 10])
plt.title('Solucion de la EDO con odeint')
plt.legend(loc='best')
plt.grid()
plt.show()

plt.figure(2)
plt.plot(sol[:,0], sol[:,1])
plt.axhline(y = 0, ls='dashed', lw = 0.7, color = 'k')
plt.axvline(x = 0, ls='dashed', lw = 0.7, color = 'k')
plt.title('Diagrama fase del pendulo')
plt.show()
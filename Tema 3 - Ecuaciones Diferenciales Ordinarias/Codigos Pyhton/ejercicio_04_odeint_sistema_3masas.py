# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:17:44 2020

@author: gusto
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(y, t) : 
    F = np.zeros(6, dtype='float64')
    F[0] = y[3]
    F[1] = y[4]
    F[2] = y[5]
    F[3] = (-0.1 * y[3] - y[0] + 0.1 * y[4] + y[1] + 1.)
    F[4] = (0.1 * y[3] + y[0] - 0.1 * y[4] - 2. * y[1] + y[2])
    F[5] = (y[1] - 0.1 * y[5] - 2. * y[2])
    return F

t = np.linspace(0, 61, 200)
y0 = np.array([0., 0., 0., 0., 0., 0.])

sol = odeint(F, y0, t)

plt.plot(t, sol[:,0], label="$M_{1}$")
plt.plot(t, sol[:,1], label="$M_{2}$")
plt.plot(t, sol[:,2], label="$M_{3}$")
plt.legend(loc='upper right')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.axis([0, 60, -0.5, 6])
plt.axhline(y=0, lw=0.75, ls='dashed', color='k')
plt.title("Desplazamiento en el sistema de tres masas")
plt.show()
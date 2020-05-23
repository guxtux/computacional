# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:30:31 2020

@author: gusto
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.81
eps = 1e-10


def F(y, t):
    F = np.zeros(4, dtype='float64')
    F[0] = y[0]
    F[1] = y[1]
    F[2] = y[3]
    F[3] = -g
    return F

def velocidad(v, t):
    sol = odeint(F, v, t)
    return sol

def alturabola(v, t):
    altura = v*t - 0.5*g*t**2
    return altura

#v = [x, y, dx, dy]
v1 =  [0.0, 0.0, 0.0, 40.0]
v2 =  [0.0, 0.0, 0.0, 60.0]
#v3 =  [0.0, 0.0, 0.0, 60.0]
t = np.linspace(0., 10., 101)

v1calc = velocidad(v1, t)
v2calc = velocidad(v2, t)
#altura3 = altura(v3, t)

valor_v1 = v1calc[:,2][-1]
valor_v2 = v2calc[:,2][-1]
#h3 = altura3[:,2][-1]

#vn = [v1[3], v2[3], v3[3],]
#hn = [h1, h2, h3]

vn = [v1[3], v2[3]]
hn = [valor_v1, valor_v2]
print(hn)

ajuste = np.interp(0.0, hn, vn)
print("La velocidad inicial que se requiere es {0:1.10f} m/s".format(ajuste))

plt.plot(t, alturabola(v1[3], t), color='r', label='v1 =' + str(v1[3]))
plt.plot(t, alturabola(v2[3], t), color='g', label='v2 =' + str(v2[3]))
plt.plot(t, alturabola(ajuste, t), color='k', label='v = ' + str(round(ajuste,2)))
plt.xlim([0, 10])
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.xlabel('tiempo [s]')
plt.ylabel('altura [m]')
#plt.title('Soluciones con los valores iniciales de velocidad')
plt.title('Solución al problema de lanzamiento con el método de disparo')
plt.legend(loc='lower left')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:27:04 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
from Metodos_Directos import Euler1


g = 9.81e0

def Func(t, u, v):
   return -g/l * np.sin(u) - k * v

l = 1e0
k = 0e0
u0 = 0.5e0*np.pi
du0 = 0e0
tmax = 20e0
ht = 0.01e0

salida = open("pendulo_euler.txt","w")
salida.write("t \t u \t du\n")

t = 0e0
u = u0; du = du0

salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(t, u, du))

while (t+ht <= tmax):
   (u, du) = Euler1(t, ht, u, du, Func)
   t += ht

   salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(t, u, du))

salida.close()

data01 = np.loadtxt('pendulo_euler.txt', delimiter='\t', skiprows=1)
plt.plot(data01[:,1], data01[:,2], color='r')
plt.xlabel('$u [rad]$')
plt.ylabel('$u^{\prime} [rad]$')
plt.title('Método de Euler $h=0.01$')
plt.show()

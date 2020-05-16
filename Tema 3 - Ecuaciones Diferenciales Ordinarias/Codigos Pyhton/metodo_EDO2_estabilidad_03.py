# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:27:04 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
from Metodos_Directos import Verlet1


g = 9.81e0

def Func(t, u, v):
   return -g/l * np.sin(u) - k * v

l = 1e0
k = 0e0
y = 0.5e0*np.pi
dy = 0e0
d2y = 0e0
tmax = 20e0
ht = 0.01e0

salida = open("pendulo_verlet.txt","w")
salida.write("t \t u \t du\n")

t = 0e0


salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(t, y, dy))

while (t+ht <= tmax):
   (y, dy, d2y) = Verlet1(t, ht, y, dy, d2y, Func)
   t += ht

   salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(t, y, dy))

salida.close()

data01 = np.loadtxt('pendulo_verlet.txt', delimiter='\t', skiprows=1)
plt.plot(data01[:,1], data01[:,2], color='g')
plt.xlabel('$u [rad]$')
plt.ylabel('$u^{\prime} [rad]$')
plt.title('Método de Verlet $h=0.01$')
plt.show()

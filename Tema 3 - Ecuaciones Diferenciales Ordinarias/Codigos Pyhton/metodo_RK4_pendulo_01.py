# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:02:59 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
from Metodos_Directos import RungeKutta

g = 9.81e0

def Func(t, u, f):
   f[1] =  u[2]
   f[2] = -g/l * np.sin(u[1]) - k * u[2]


l = 1e0
k = 0e0
u0 = 0.5e0*np.pi
du0 = 0e0
tmax = 20e0
ht = 0.001e0

n = 2
u = [0]*(n+1)

salida = open("pendulo.txt","w")
salida.write("t \t u \t du\n")

t = 0e0
u[1] = u0; u[2] = du0
salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(t, u[1], u[2]))

nT = 0
t1 = t2 = 0e0
us = u[1]
while (t+ht <= tmax):
   RungeKutta(t, ht, u, n, Func)
   t += ht

   if (u[1]*us < 0e0):
      if (t1 == 0): t1 = t
      else: t2 = t; nT += 1
   us = u[1]

   salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(t, u[1], u[2]))

T = 2e0*(t2-t1) / nT
T0 = 2e0*np.pi*np.sqrt(l/g)
print("u0 = {0:7.5f} \t T/T0 = {1:7.5f}".format(u0, T/T0))

salida.close()

data = np.loadtxt('pendulo.txt', delimiter='\t', skiprows=1)

plt.figure(1)
plt.plot(data[:,0], data[:,1], color='r')
plt.title('Solución numérica $u(t)$ al problema de Cauchy para un péndulo no lineal con el método RK4', wrap=True)
plt.xlabel('$t(s)$')
plt.ylabel('$u[rad]$')
plt.xlim([0, 20])

plt.figure(2)
plt.plot(data[:,2], data[:,1], color='b')
plt.xlabel('$u[rad]$')
plt.ylabel('$u^{\prime} [rad]$')
plt.title('Trayectoria del péndulo en el espacio fase')

plt.show()
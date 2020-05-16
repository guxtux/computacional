# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:22:57 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt

data01 = np.loadtxt('pendulo01.txt', delimiter='\t', skiprows=1)
data02 = np.loadtxt('pendulo02.txt', delimiter='\t', skiprows=1)
data03 = np.loadtxt('pendulo03.txt', delimiter='\t', skiprows=1)

plt.plot(data01[:,0], data01[:,1], color='r', label='$u_{0}=0.1$')
plt.plot(data02[:,0], data02[:,1], color='b', label='$u_{0}=\pi/2$')
plt.plot(data03[:,0], data03[:,1], color='k', label='$u_{0}=3$')
#plt.title('Gráfica del espacio fase con el método predictor-corrector de Euler')
plt.xlabel('$t(s)$')
plt.ylabel('$u[rad]$')
plt.legend(loc='best')
plt.xlim([0, 20])
plt.title('Comparación de la solución con diferentes desplazamientos iniciales')
plt.show()
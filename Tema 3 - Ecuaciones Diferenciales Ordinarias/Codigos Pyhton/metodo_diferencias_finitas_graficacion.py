# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:35:13 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def ajuste(tn, t, y, colorforma='b'):
    f = interp1d(tn, y, kind='quadratic')
    y_smooth=f(t)
    plt.plot (t,y_smooth, colorforma)

# 
#
def grafica_n(tn, fy, aprox, n):
    ajuste(tn, t, aprox)
    ajuste(tn, t, fy, 'r')
    plt.plot(tn, aprox, 'bs', label='aproximación')
    plt.plot(tn, fy, 'ro', label='función')
    plt.title('Solución al problema mediante diferencias finitas con $N= ' + str(n) + '$')
    plt.legend(loc='best')
    plt.xlim([0,1])

t = np.linspace(0.0, 1.0, 200)

datos = np.loadtxt('Datos_N_20.txt', delimiter='\t', skiprows=1)


grafica_n(datos[:,1], datos[:,2], datos[:,3], 20)
plt.show()
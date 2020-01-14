# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:53:12 2012

@author: est5
"""

#Ajusta sin(x) en [0,2pi] con el polinomio de interpolacion de Lagrange de orden
#4 y 8, utilizando puntos con igual separacion (5 y 9 puntos respectivamente).
#Grafica los polinomios de interpolaciòn junto con sin(x) y las distribuciones.

import matplotlib.pyplot as plt
import numpy as np
from math import *
n = 4
x = np.array([0,.4*pi,.8*pi,1.2*pi,1.6*pi,2.*pi])
f = np.array([sin(0.),sin(.4*pi),sin(pi*.8),sin(1.2*pi),sin(1.6*pi),sin(2.*pi)])
xa = eval(raw_input('Da el valor de x'))
yres = 0
for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
plt.plot(x,f)
plt.plot(xa)
plt.show()
print 'El polinomio valuado en P(',xa,')=',yres

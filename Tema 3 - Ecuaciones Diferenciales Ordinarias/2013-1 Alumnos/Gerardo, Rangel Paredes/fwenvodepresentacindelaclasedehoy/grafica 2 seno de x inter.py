# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from math import*
import numpy as np
from numpy import*
import matplotlib.pyplot as plt 
n = 8
x = linspace(0, 2*pi, 9)                          
f = np.array([0,0.7071067787841887,
 1.0,0.7071067813225559, 
 0.,-0.7071067833168894, 
-1.0, -0.7071067838609232,
 0])
xa = linspace(0, 2*pi, 19)
yres = 0
for i in range(0, n + 1):
    z = 1.0
    for j in range(0, n + 1):
        if i != j:
            z = z*(xa- x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
print "El polinomio de oreden 4 evaluado en P(",xa,") = ", yres
plt.plot([x] and [xa], [f] and [yres], "ro")
plt.show()

    
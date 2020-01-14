# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from math import*
import numpy as np
from numpy import*
import matplotlib.pyplot as plt 
n = 4
x = linspace(0, 2*pi, 5)                          
f = np.array([0, 1.0, 0.,-1.0, 0])
xa = linspace(0, 2*pi, 9)
yres = 0
for i in range(0, n + 1):
    z = 1.0
    for j in range(0, n + 1):
        if i != j:
            z = z*(xa- x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
plt.plot([x] and [xa], [f] and [yres], "ro")
plt.show()



    

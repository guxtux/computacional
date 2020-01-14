# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from numpy import*
import numpy as np
from math import*
import matplotlib.pyplot as plt
n = 4
x = linspace(0., pi/2, 7.)
f = np.array([0., 0.06775866868477086, 0.26179939199595076, 0.5553603629806289, 0.9068996804542877, 1.2643939512195963, 1.57079633])
xa = linspace(0., pi/2, 15)
yres = 0
for i in range(0, n+1):
    z = 1.0
    for j in range(0, n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
plt.plot([x] and [xa], [f] and [yres], "ro")
plt.show()
    




    
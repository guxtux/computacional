# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from numpy import*
import numpy as np
from math import*
n = 4
x = linspace(0., pi/2, 7.)
f = np.array([0., 0.06775866868477086, 0.26179939199595076, 0.5553603629806289, 0.9068996804542877, 1.2643939512195963, 1.57079633])
xa = eval(raw_input("ingrese el valor para interpolar: "))
yres = 0
z = sin(xa)
for i in range(0, n+1):
    z = 1.0
    for j in range(0, n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
print "El polinomio evaluado en P(",xa,") = ", yres
er = yres - z
print "El error de la funcion en la interpolacion es: ", er
    




    

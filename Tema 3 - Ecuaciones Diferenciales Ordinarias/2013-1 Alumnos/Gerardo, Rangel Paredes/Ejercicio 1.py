# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:46:28 2012

@author: gabriela
"""

import numpy as np
n = 2
x = np.array( [ -30,0,30 ] )
f = np.array( [ 6870,6728,6615 ] )
xa =131.9


yres = 0
for i in  range(0,n+1):
    z = 1.0
    for j in range(0,n+1):
        if i!=j:
            z = z*(xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
print "El polinomio evaluado en P(',xa,') = ",yres



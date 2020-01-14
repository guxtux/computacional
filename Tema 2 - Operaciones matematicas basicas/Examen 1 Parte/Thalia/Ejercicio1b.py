# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:47:18 2013

@author: usuario
"""
from numpy import *

n=2
x0=array([0.0])
x=array([-1.2, 0.3, 1.1])
f=array([-5.76, -5.61, -3.69])

for k in x0:
    yres=0
    for i in range (0, n+1):
        z=1.0
        for j in range (0, n+1):
            if i != j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]
    print 'El valor de y en x=',k,' es',yres
    


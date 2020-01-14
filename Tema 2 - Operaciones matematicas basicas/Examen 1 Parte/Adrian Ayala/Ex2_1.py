# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:17:33 2013

@author: acesimbrote
"""

from numpy import *
import Neville

n = 1
x = array([-1.2,0.3,1.1])
x0 = array([0.])
f = array([-5.76,-5.61,-3.69])

def neville (x, f, x0):
    m=len(x)
    y=f.copy()
    for k in range (1,m-1):
        y[0:m-k]=((x0-x[k:m])*y[0:m-k]+(x[0:m-k]-x0)*y[1:m-k+1])/(x[0:m-k]-x[k:m])
    return y[0]


print 'El polinomio usando Neville es P(',x0[0],')= ', neville(x,f,x0) 

for k in x0:
    yres = 0
    for i in range(0,n+1):
        z = 1.0
        for j in range(0,n+1):
            if i != j:
                z = z * (k-x[j])/(x[i]-x[j])
                yres = yres + z*f[i]
    print ' El polinomio usando Lagrange es P(',k,') = ' ,yres

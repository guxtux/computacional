# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:56:44 2013

@author: usuario
"""
from numpy import *

def neville (xDatos, yDatos, x):
    m=len(xDatos)
    y=yDatos.copy()
    for k in range (1,m):
        y[0:m-k]=((x-xDatos[k:m]*y[0:m-k])+(xDatos[0:m-k]-x)*y[1:m-k+1])/(xDatos[0:m-k]-xDatos[k:m])
    return y[0]
    
xDatos=array([-1.2, 0.3, 1.1])
yDatos=array([-5.76, -5.61, -3.69])

print 'El valor de y en x=0 es'
print neville (xDatos, yDatos, 0.)

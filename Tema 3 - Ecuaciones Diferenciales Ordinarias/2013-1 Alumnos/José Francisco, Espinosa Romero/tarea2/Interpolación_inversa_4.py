# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:27:49 2012

@author: pako
"""

import numpy as np

def coeficientes(xDatos, yDatos):
    m=len(xDatos)
    a=yDatos.copy()
    for k in range(1,m):
        a[k:m]=(a[k:m]-a[k-1])/(xDatos[k:m]-xDatos[k-1])
    return a

def evalPol(a,xDatos,x):
    n=len(xDatos)-1
    p=a[n]
    for k in range(1,n+1):
        p=a[n-k]+(x-xDatos[n-k])*p
    return p

yDatos=np.array([-0.06604,-0.02724,0.01282,0.05383],float)
xDatos=np.array([4.,3.9,3.8,3.7],float)
a=coeficientes(yDatos,xDatos)
y=(0.0)
x=evalPol(a,yDatos,y)

print 'La raíz es:',x

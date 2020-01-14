# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 04:12:54 2012

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

res=open('IntNewton(ej2).dat','w')
xDatos=np.array([-3.,2.,-1.,3.,1.])
yDatos=np.array([0.,-5.,-4.,12.,0.])
a=coeficientes(xDatos,yDatos)

for x in np.arange(-4.0,4.0,0.2):
    y=evalPol(a,xDatos,x)
    res.write('%3.1f %9.5f\n' %(x,y))
res.close() 
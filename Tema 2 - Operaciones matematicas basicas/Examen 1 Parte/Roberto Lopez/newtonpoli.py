# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:27:38 2013

@author: est5
"""

## module newtonpoli
def evalPoli(a,xDatos,x):
    n=len(xDatos)-1
    p=a[n]
    for k in range(1,n+1):
        p=a[n-k] + (x-xDatos[n-k])*p
    return p

def coeffts(xDatos,yDatos):
    m=len(xDatos)
    a=yDatos.copy()
    for k in range(1,m):
        a[k:m]=(a[k:m]-a[k-1])/(xDatos[k:m]-xDatos[k-1])
    return a
    
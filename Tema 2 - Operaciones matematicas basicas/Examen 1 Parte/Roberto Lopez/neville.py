# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:32:52 2013

@author: est5
"""

## module neville
def neville(xDatos,yDatos,x):
    m=len(xDatos)
    y=yDatos.copy()
    for k in range(1,m):
        y[0:m-k]=((x-xDatos[k:m])*y[0:m-k]+(xDatos[0:m-k]-x)*y[1:m-k+1])/ \
        (xDatos[0:m-k]-xDatos[k:m])
    return y[0]
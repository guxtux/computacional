# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar  7 20:07:19 2013
MÓDULO DE INTERPOLACIÓN
"""
##module interpol

def coeffts(xDatos,yDatos):
    m=len(xDatos)
    a=yDatos.copy()
    for k in range (1,m):
        a[k:m]=(a[k:m]-a[k-1])/(xDatos[k:m]-xDatos[k-1])
    return a
    
def newton(xDatos,yDatos,x):
    a=coeffts(xDatos,yDatos)
    n=len(xDatos)-1
    p=a[n]
    for k in range(1,n+1):
        p=a[n-k]+(x-xDatos[n-k])*p
    return p

def neville(xDatos,yDatos,x):
    m=len(xDatos)
    y=yDatos.copy()
    for k in range (1,m):
        y[0:m-k]=((x-xDatos[k:m])*y[0:m-k]+\
        (xDatos[0:m-k]-x)*y[1:m-k+1])/(xDatos[0:m-k]-xDatos[k:m])
    return y[0]

def lagrange(xDatos,yDatos,x):
    y=0.
    m=len(xDatos)
    for k in range(0,m):
        L=1.
        for l in range(0,m):
            if l!=k:
                L=L*(x-xDatos[l])/(xDatos[k]-xDatos[l])
        y=y+L*yDatos[k]
    return y

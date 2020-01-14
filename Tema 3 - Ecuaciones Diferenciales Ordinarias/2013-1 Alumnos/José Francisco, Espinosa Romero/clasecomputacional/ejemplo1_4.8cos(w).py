# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:47:00 2012

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

resultados=open('DatosNewton(ej1).dat','w')
xDatos=np.array([0.15,2.3,3.15,4.85,6.25,7.95])
yDatos=np.array([4.79867,4.49013,4.2243,3.47313,2.66674,1.51900])
a=coeficientes(xDatos,yDatos)

print "x    y-Interpolada    y-Exacta"
print "------------------------------"

for x in np.arange(0.0,8.0,0.5):
    y=evalPol(a,xDatos,x)
    yExacta=4.8*np.cos(np.pi*x/20.0)
    print '%3.1f %9.5f %9.5f' %(x,y,yExacta)
    resultados.write('%3.1f %9.5f %9.5f\n' %(x,y,yExacta))
resultados.close()
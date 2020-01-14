# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:39:45 2012

@author: est5
"""

from numpy import*

def coeficientes(xdatos, ydatos):
    m = len(xdatos)
    a = ydatos.copy()
    
    for k in range(1, m):
      a[k:m] = (a[k:m] - a[k-1])/(xdatos[k:m] - xdatos[k-1])
    return a
def evaluafuncion(a, xdatos, x):
    n = len(xdatos)-1
    p = a[n]
    
    for k in range(1, n+1):
        p = a[n-k] + (x - xdatos[n-k])*p
    return p

resultados = open("datosfuncion.dat", "w")

xdatos = array([-250,-200,-100,0,100,300])
ydatos = array([0.0163,0.318,0.699,0.870,0.941,1.04])

a = coeficientes(xdatos,ydatos)

print "....x....yInterpol...."
print"......................."

for x in arange(200,600,200):
    y = evaluafuncion(a,xdatos,x)
    print"%3.1f %9.5f" %(x,y)
    resultados.write("%3.1f %9.5f\n" %(x,y))

resultados.close()
    
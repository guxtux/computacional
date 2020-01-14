# -*- coding: utf-8 -*-
"""
EJERCICIO 2.

USANDO EL METODO DE NEWTON, ENCUENTRA UN POLINOMIO QUE SE AJUSTE A 
LOS SIGUIENTES PUNTOS X,Y (XDATOS, YDATOS)

@author: marisolchavez
"""
#USANDO EL METODO DE NEWTON

import numpy as np
from math import *



def coeficientes(xDatos, yDatos):
    m = len(xDatos)
    a = yDatos.copy()
    
    for k in range(1,m):
        a[k:m] = (a[k:m]-a[k-1])/(xDatos[k:m]-xDatos[k-1])     
    return a
    

def evaluaPoli(a,xDatos,x):
    n = len(xDatos)-1
    p=a[n]
    
    for k in range(1,n+1):
        p = a[n-k]+(x - xDatos[n-k])*p
        
    return p
    
    


xDatos = np.array([-3.0, -1.0, 1.0, 2.0, 3.0])
yDatos = np.array([0.0, -4.0, 0.0, -5.0, 12.0])

a=coeficientes(xDatos, yDatos)

for i in range(0,5):
    print "el coeficiente a", i+1, "=", a[i]


print "x    yInterpol   "
print "_________________"


for x in np.arange(-3.0, 4.0, 1.0):
    y= evaluaPoli(a,xDatos,x)
    print "%3.1f %9.5f "  %(x,y)

"""
Y entonces el polinomio esta dado por:

P(x)=a1+a2(x-x1)+a3(x-x1)(x-x2)+a4(x-x1)(x-x2)(x-x3)+a5(x-x1)(x-x2)(x-x3)(x-x4)

Desarrollando y agrupando terminos:
    
P(x)=x^4(a5)+x^3(a4-a5(x1+x2+x3+x4))+x^2(a3-a4(x1+x2+x3)+a5(x1x2+x1x3+x1x4+x2x3+x2x4+x3x4))+x(a2-a3(x1+x2)+a4(x1x2+x1x3+x2x3)-a5(x1x2x3+x1x2x4+x1x3x4+x2x3x4))+a1-a2x1+a3x1x2-a4x1x2x3+a5x1x2x3x4

renombrando:
P(x)=x^4(a5)+x^3(a4-a5(c1))+x^2(a3-a4(c2)+a5(c3))+x(a2-a3(c4)+a4(c5)-a5(c6))+a1-a2(c7)+a3(c8)-a4(c9)+a5c10
"""
c1=xDatos[0]+xDatos[1]+xDatos[2]+xDatos[3]
c2=xDatos[0]+xDatos[1]+xDatos[2]
c3=xDatos[0]*xDatos[1]+xDatos[0]*xDatos[2]+xDatos[0]*xDatos[3]+xDatos[1]*xDatos[2]+xDatos[1]*xDatos[3]+xDatos[2]*xDatos[3]
c4=xDatos[0]+xDatos[1]
c5=xDatos[0]*xDatos[1]+xDatos[0]*xDatos[2]+xDatos[1]*xDatos[2]
c6=xDatos[0]*xDatos[1]*xDatos[2]+xDatos[0]*xDatos[1]*xDatos[3]+xDatos[0]*xDatos[2]*xDatos[3]+xDatos[1]*xDatos[2]*xDatos[3]
c7=xDatos[0]
c8=xDatos[0]*xDatos[1]
c9=xDatos[0]*xDatos[1]*xDatos[2]
c10=xDatos[0]*xDatos[1]*xDatos[2]*xDatos[3]

print "el polinomio que se ajusta es:"


print a[4], "X^4+", a[3]-a[4]*c1, "x^3+", a[2]-a[3]*c2+a[4]*c3, "X^2+",a[1]-a[2]*c4+a[3]*c5-a[4]*c6, "X+",a[0]-a[1]*c7+a[2]*c8-a[3]*c9+a[4]*c10 
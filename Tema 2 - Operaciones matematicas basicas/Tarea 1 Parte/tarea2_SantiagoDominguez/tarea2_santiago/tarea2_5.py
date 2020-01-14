# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:36:58 2013

@author: san
"""

import math as mt
#La energia libre de Gibbs en un mol de hidrogeno a una temperatura T es:
#"G=-RTln(T/T0)^5/2" en joule

R=8.311441
T0=4.44418
G=-1e5
m=13.3e3

def f(x): return - R*x*(mt.log(x/T0)) - G
def df(x): return -R*((mt.log((x/T0)**2.5 )) + 2.5* (T0**1.5)/x**2.5)
def newtonraphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonraphson(2100)

print 'La temperatura= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
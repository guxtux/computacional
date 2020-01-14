# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:00:31 2012

@author: pako
"""

from math import *

def G(T): return -8.311441*2.5*T*log(T/4.44418)+1e5
def dG(T): return -8.311441*2.5*(1+log(T/4.44418))

def NewtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-G(x)/dG(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print "Son demasiadas iteraciones\n"

raiz,numIter=NewtonRaphson(100.0)

print "Temperatura = %4.5f Kelvin" %(raiz)

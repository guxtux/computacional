# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:26:14 2012

@author: pako
"""

from math import *

def f(t): return 2510.*log((2.8e6)/((2.8e6)-(13.3e3)*t))-9.81*t-335
def df(t): return (2510.*13.3e3)/((2.8e6)-(13.3e3)*t)-9.81

def NewtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print "Son demasiadas iteraciones\n"

raiz,numIter=NewtonRaphson(0.0)

print "Tiempo en alcanzar la velocidad del sonido= %4.5f segundos" %(raiz)

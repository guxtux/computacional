# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:50:03 2013

@author: san
"""

from numpy import *
#La ecuacion de equilibrio quimico en la produccion de metanol a partir
#de CO y H2, es: "E(3-2E)^2/(1-E)^3=249.Determinar E

def s(x): return x*(3-2*x)**2
def h(x): return (1-x)**3
def f(x): return (s(x)/h(x)) - 249.2
def j(x): return 9 + (2*x)-(12*x**2)+(4*x**3)
def k(x): return (1-x)**4
def df(x): return j(x)/k(x)

def newtonraphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonraphson(0.8)

print 'E= ' , raiz1
print 'Numero de iteraciones1= ', numIter1

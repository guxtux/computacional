# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:23:17 2013

@author: acesimbrote
"""


#de acuerdo a la grafica se ve que tenemos raices en x=+-5e7
from numpy import *
import matplotlib.pyplot as plt

def s(x): return x*(3-2*x)**2
def h(x): return (1-x)**3
def f(x): return (s(x)/h(x)) - 249.2
def j(x): return 9 + (2*x)-(12*x**2)+(4*x**3)
def k(x): return (1-x)**4
def df(x): return j(x)/k(x)

def newtonRaphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonRaphson(0.8)

print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1


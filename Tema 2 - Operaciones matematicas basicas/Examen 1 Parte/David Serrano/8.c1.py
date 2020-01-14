# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:38:41 2013

@author: Deivid
"""
from numpy import *
import matplotlib.pyplot as plt
def f(x): return -x**3+x+1
def df(x): return -3*x**2+1
y=linspace(-5.0,5.0)
def newtonRaphson(x,tol=1e-4):

    for i in range(50):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'

raiz1 , numIter1=newtonRaphson(1.3)


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1

plt.plot (f(y))
plt.show ()
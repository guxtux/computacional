# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:37:12 2013

@author: Deivid
"""

from numpy import *
import matplotlib.pyplot as plt
def f(x): return tan(x)-x+1 
def df(x): return 1/((cos(x))**2) - 1
y=linspace(0.0,3.0*pi)
def newtonRaphson(x,tol=1e-4):

    for i in range(50):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'

raiz1 , numIter1=newtonRaphson(7.7)
raiz2 , numIter2=newtonRaphson(4.4)


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
print 'Raiz2= ' , raiz2
print 'Numero de iteraciones2= ', numIter2


plt.plot (f(y))
plt.show ()
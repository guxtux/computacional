# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:39:44 2013

@author: Deivid
"""

from numpy import *
import matplotlib.pyplot as plt
def f(x): return 16*x**5-20*x**3+x**2+5*x-0.5
def df(x): return 80*x**4-60*x**2+2*x+5
y=linspace(-2.0,2.0)
def newtonRaphson(x,tol=1e-4):

    for i in range(50):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'

raiz1 , numIter1=newtonRaphson(-0.9)
raiz2 , numIter2=newtonRaphson(-0.6)
raiz3 , numIter3=newtonRaphson(-0.1)
raiz4 , numIter4=newtonRaphson(0.5)
raiz5 , numIter5=newtonRaphson(0.9)


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
print 'Raiz2= ' , raiz2
print 'Numero de iteraciones2= ', numIter2
print 'Raiz3= ' , raiz3
print 'Numero de iteraciones3= ', numIter3
print 'Raiz4= ' , raiz4
print 'Numero de iteraciones4= ', numIter4
print 'Raiz5= ' , raiz5
print 'Numero de iteraciones5= ', numIter5



plt.plot (f(y))
plt.show ()
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:18:42 2013

@author: Acesimbrote
"""

from numpy import *
import matplotlib.pyplot as plt
from funciones import *

def df(x): return cos(x) - 0.3*e**x
y=linspace(0,20.0)
def newtonRaphson(x,tol=1e-4):

    for i in range(50):
        dx = -f2(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'

raiz1 , numIter1=newtonRaphson(.5)
raiz2 , numIter2=newtonRaphson(1.07)


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
print 'Raiz2= ' , raiz2
print 'Numero de iteraciones2= ', numIter2

plt.plot (f2(y))
plt.show ()

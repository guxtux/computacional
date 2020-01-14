# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:01:56 2013

@author: acesimbrote
"""

from numpy import *
import matplotlib.pyplot as plt
from funciones import *

def df(x): return 1/((cos(x))**2) - 1
y=linspace(0.0,3.0*pi)
def newtonRaphson(x,tol=1e-4):

    for i in range(50):
        dx = -f1(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'

raiz1 , numIter1=newtonRaphson(7.7)
raiz2 , numIter2=newtonRaphson(4.4)


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
print 'Raiz2= ' , raiz2
print 'Numero de iteraciones2= ', numIter2


plt.plot (f1(y))
plt.show ()
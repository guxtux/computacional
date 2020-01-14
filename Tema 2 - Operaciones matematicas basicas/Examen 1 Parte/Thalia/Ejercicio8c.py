# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 06:16:16 2013

@author: usuario
"""
from numpy import *
from math import *
import matplotlib.pyplot as plt

x=arange(0., 2., 0.01)
def f(x): return -(x)**3+x+1
def df(x): return -3*x**2+1

def newtonRaphson (x, tol=0.0001):
    for i in range (30):
        dx= -f(x)/df(x)
        x= x+dx
        if abs(dx)<tol: return x, i
    print 'Son demasiadas iteraciones\n'


plt.plot (x, f(x), 'y-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices positivas de un polinomio de grado 3')
plt.show()   

raiz, numiter= newtonRaphson (1.)
print 'Tiene una raiz triple en x igual a'
print raiz

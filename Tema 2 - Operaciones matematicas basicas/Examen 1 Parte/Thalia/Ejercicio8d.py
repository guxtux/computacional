# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 06:21:15 2013

@author: usuario
"""
from numpy import *
from math import *
import matplotlib.pyplot as plt

x=arange(0., 1., 0.001)
def f(x): return 16*x**5-20*x**3+x**2+5*x-0.5
def df(x): return 5*16*x**4-60*x**2+2*x+5

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
plt.title('Raices positivas de un polinomio de grado 5')
plt.show() 
  
raiz1, numiter1= newtonRaphson (0.1)
raiz2, numiter2= newtonRaphson (0.5)
raiz3, numiter2= newtonRaphson (0.9)
print 'Las raíces positivas del Polinomio son en x igual a'
print raiz1
print raiz2
print raiz3

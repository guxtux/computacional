# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 06:37:30 2013

@author: usuario
"""
from numpy import *
import matplotlib.pyplot as plt

x=arange(0., 2., 0.01)
def f(x): 
    return sin(x)-0.3*exp(x)
def df(x): 
    return cos(x)-0.3*exp(x)

def newtonRaphson (x, tol=0.0001):
    for i in range (30):
        dx= -f(x)/df(x)
        x= x+dx
        if abs(dx)<tol: return x, i
    print 'Son demasiadas iteraciones\n'

plt.plot (x, f(x), 'g-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices positivas de f(x)=sin(x)-0.3exp(x)')
plt.show()   

raiz1, numiter1 = newtonRaphson (0.5)
raiz2, numiter2 = newtonRaphson (1.0)
print 'Las raíces están en x igual a '
print raiz1
print raiz2

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 05:59:45 2013

@author: usuario
"""
import numpy as np
import matplotlib.pyplot as plt
from math import *

x=np.arange(0., 8., 0.01)
def f(x): return np.tan(x)-x+1
def df(x): return acos(x)**2-1

def newtonRaphson (x, tol=0.0001):
    for i in range (1000):
        dx= -f(x)/df(x)
        x= x+dx
        if abs(dx)<tol: return x, i
    print 'Son demasiadas iteraciones\n'


plt.plot (x, f(x), 'y-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices positivas de f(x)=tan(x)-x+1')
plt.show()   

raiz, numiter= newtonRaphson (4.)
print 'Las raíces positivas están en x igual a'
print raiz

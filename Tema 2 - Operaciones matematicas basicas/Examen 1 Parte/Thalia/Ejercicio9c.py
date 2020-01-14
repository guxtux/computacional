# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:56:04 2013

@author: usuario
"""
from numpy import *
from Raices import *
import matplotlib.pyplot as plt

x=arange(-3.4,-3.1, 0.001)
def f(x): return x+(1/((x+3)*x))

plt.plot (x, f(x), 'g-')
plt.grid (True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices de la funcion f(x)')
plt.show()

def metsec (a, b, tol=0.001):    
    for i in range (30):
        dr= -f(a)*((b-a)/(f(b)-f(a)))
        a= a+dr
        if abs(dr)<tol: return a, i
    print 'Son demasiadas iteraciones\n'

a, c, dx = (-3.5, -3., 0.01)
print 'El intervalo 1 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print raiz


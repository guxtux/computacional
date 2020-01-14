# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:31:07 2013

@author: usuario
"""
from numpy import *
from Raices import *
import matplotlib.pyplot as plt

x=arange(0., 4, 0.01)
def f(x): return log(x)-0.2*x**2+1

plt.plot (x, f(x), 'b-')
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

a, c, dx = (0.,3.5, 0.2)
print 'El intervalo 1 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print raiz


a, c, dx = (c, 3.5, 0.2)
print 'El intervalo 2 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print 'La raíz 2 es:'
print raiz


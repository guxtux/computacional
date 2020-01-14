# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:48:56 2013

@author: usuario
"""
from numpy import *
from Raices import *
import matplotlib.pyplot as plt

x=arange(-6., 51, 0.1)
def f(x): return 0.1*x**3-5*x**2-x+4+exp(-x)

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

a, c, dx = (-6.,50, 0.2)
print 'El intervalo 1 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print raiz


a, c, dx = (c, 50, 0.2)
print 'El intervalo 2 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print 'La raíz 2 es:'
print raiz

a, c, dx = (c, 50, 0.2)
print 'El intervalo 3 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print 'La raíz 3 es:'
print raiz

a, c, dx = (c, 50, 0.2)
print 'El intervalo 4 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
raiz, numiter=metsec(a,c)
print 'La raíz 4 es:'
print raiz



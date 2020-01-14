# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 05:42:21 2013

@author: usuario
"""
from math import *
from numpy import *
import matplotlib.pyplot as plt
from Raices import *

x=arange(0.0, 1., 0.01)
ejex=[]
ejex1=[]
ejex2=[]
ejey=[]
ejey1=[]
ejey2=[]

def f(x):
    return 16*x**5-20*x**3+x**2+5*x-0.5   
    
a, b, dx = (0.0, 1., 0.2)
print 'El intervalo 1 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 1 es:'
print bisect (f, x1, x2, switch=1, epsilon=1.0e-3)
t=bisect (f, x1, x2, switch=1, epsilon=1.0e-3)

a, b, dx = (x2, 1., 0.2)
print 'El intervalo 2 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 2 es:'
print bisect (f, x1, x2, switch=1, epsilon=1.0e-3)
t1=bisect (f, x1, x2, switch=1, epsilon=1.0e-3)

a, b, dx = (x2, 1., 0.2)
print 'El intervalo 2 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 2 es:'
print bisect (f, x1, x2, switch=1, epsilon=1.0e-3)
t2=bisect (f, x1, x2, switch=1, epsilon=1.0e-3)

ejex.append(t)
ejey.append(0.0)
ejex1.append(t1)
ejey1.append(0.0)
ejex2.append(t2)
ejey2.append(0.0)

plt.plot (x, f(x), 'y-', ejex, ejey, 'go', ejex1, ejey1, 'go', ejex2, ejey2, 'go')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices positivas de un polinomio')
plt.show() 
# -*- coding: utf-8 -*-

"""
Created on Sun Mar 24 04:17:28 2013

@author: usuario
"""
from math import *
from numpy import *
import matplotlib.pyplot as plt
from Raices import *

x=arange(0.0, 3*pi, 0.1)

def f(x):
    return tan(x)-x+1

plt.plot (x, f(x), 'm-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices de la funcion\n f(x)=tan(x)-x+1')
plt.show()    
    
a, b, dx = (4., 3*pi, 0.2)
print 'El intervalo 1 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 1 es:'
print bisect (f, x1, x2, switch=1, epsilon=1.0e-3)

a, b, dx = (6., 3*pi, 0.2)
print 'El intervalo 2 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 2 es:'
print bisect (f, x1, x2, switch=1, epsilon=1.0e-3)

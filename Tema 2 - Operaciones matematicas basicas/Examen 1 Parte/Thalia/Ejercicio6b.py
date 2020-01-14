# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 05:30:12 2013

@author: usuario
"""
from math import *
from numpy import *
import matplotlib.pyplot as plt
from Raices import *

x=arange(0.0, 2, 0.1)
ejex=[]
ejey=[]
ejex1=[]
ejey1=[]

def f(x):
    return sin(x)-0.3*exp(x)
      
a, b, dx = (0.0, 2, 0.2)
print 'El intervalo 1 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 1 es:'
print bisect (f, x1, x2, switch=0, epsilon=1.0e-3)
t=bisect (f, x1, x2, switch=0, epsilon=1.0e-3)

a, b, dx = (x2, 2, 0.2)
print 'El intervalo 2 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'La raíz 2 es:'
print bisect (f, x1, x2, switch=0, epsilon=1.0e-3)
t1=bisect (f, x1, x2, switch=0, epsilon=1.0e-3)

ejex.append(t)
ejey.append(0.)
ejex1.append(t1)
ejey1.append(0.)

plt.plot (x, f(x), 'g-', ejex, ejey, 'mo', ejex1, ejey1, 'mo')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices positivas de la funcion\n f(x)=sin(x)-0.3exp(x)')
plt.show()  
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 05:35:55 2013

@author: usuario
"""
from math import *
from numpy import *
import matplotlib.pyplot as plt
from Raices import *

x=arange(0.0, 3, 0.1)
ejex=[]
ejey=[]

def f(x):
    return -(x)**3+x+1

plt.plot (x, f(x), 'b-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices de la funcion\n f(x)=-x3+x+1')
plt.show()    
    
a, b, dx = (0., 3., 0.2)
print 'El intervalo 1 es:'
x1, x2 = buscaraiz( f, a, b, dx)
print x1, x2
print 'Tiene una raíz triple en:'
print bisect (f, x1, x2, switch=1, epsilon=1.0e-3)
t=bisect (f, x1, x2, switch=1, epsilon=1.0e-3)

ejex.append(t)
ejey.append(0.)

plt.plot (x, f(x), 'b-', ejex, ejey, 'yo')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices de la funcion\n f(x)=-x3+x+1')
plt.show()  


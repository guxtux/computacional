# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:50:31 2013

@author: usuario
"""
from numpy import *
from Raices import *
import matplotlib.pyplot as plt

x=arange (0.0, 5., 0.01)
def f(x): return 0.5*exp(x/3)-sin(x)

plt.plot (x, f(x), 'm-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Raices de la funcion\n f(x)=0.5exp(x/3)-sin(x)')
plt.show()

def falsposmod (f, a, c, switch=1, epsilon= 1.0e-9):
    fa=f(a)
    if fa==0.0: return a
    fc=f(c)
    if fc==0.0: return b
    if fa*fc > 0.0: print 'La raiz no se ha identificado en un intervalo'
    n= ceil (log(abs(c-a)/epsilon)/log (2.0))
    for i in arange (n):
        b= (a*fc-c*fa)/(fc-fa); fb=f(b)
        if (switch == 0) and (abs(fb)>abs(fa)) and (abs(fb)>abs(fc)):
            return None
        if fb==0.0: return b
        if fa*fb<0.0:
            a=b; fa=fb
        else:
            c=b; fc=fb
            if i==2:
                if fa==fa: return fa/2
                if fc==fc: return fc/2
    return (a*fc-c*fa)/(fc-fa)

a, c, dx = (0.,2, 0.2)
print 'El intervalo 1 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
print 'La raíz 1 es:'
print falsposmod (f, a, c, switch=1, epsilon=1.0e-9)

a, c, dx = (c, 2, 0.2)
print 'El intervalo 2 es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
print 'La raíz 2 es:'
print falsposmod (f, a, c, switch=1, epsilon=1.0e-9)       
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:30:40 2013

@author: usuario
"""
from numpy import *
from Raices import *
import matplotlib.pyplot as plt

x=arange (-3.,3., 0.01)
ejex=[]
ejey=[]

def f(x): return (x**3)+(2*x)-1

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

a, c, dx = (-3.,3., 0.2)
print 'El intervalo es:'
a, c = buscaraiz( f, a, c, dx)
print a, c
print 'Tiene una raíz triple en x igual a:'
print falsposmod (f, a, c, switch=1, epsilon=1.0e-9)
t=falsposmod (f, a, c, switch=1, epsilon=1.0e-9)

ejex.append(t)
ejey.append(0.0)

plt.plot (x, f(x), 'y-', ejex, ejey, 'ko')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Raices positivas de un Polinomio\n de grado 3')
plt.show()

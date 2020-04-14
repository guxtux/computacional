# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:43:03 2012

@author: IIFCES
"""

from math import tan

def buscaraiz(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2
        
def f(x): return x**3 - 10*x**2 + 5.

a, b, dx = (0.0,1.5, 0.2)

x1, x2 = buscaraiz(f,a,b,dx)
 
while True:
    xmed=(x1+x2)/2
    if f(xmed)==0.0:
        break
    if (f(x1)*f(xmed))<0:
        x2=xmed
    else:
        x1=xmed
    error=abs(x2-x1)
    if error<0.0001:
        break
print 'La raiz es',xmed
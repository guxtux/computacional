# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:45:25 2012

@author: IIFCES
"""
from numpy import *

def buscaraiz(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None#,None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2
            
            
def f(x): return x**3 - 10*x**2 + 5.


a, b, dx = (0.0,1.5, 0.2)

x1, x2 = buscaraiz(f,a,b,dx)

print u'La raíz está en el intervalo: '
print '(', x1, ',', x2, ')'
    




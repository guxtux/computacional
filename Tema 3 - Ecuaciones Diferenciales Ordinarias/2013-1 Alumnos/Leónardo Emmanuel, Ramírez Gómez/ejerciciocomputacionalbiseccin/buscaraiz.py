# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:42:09 2012

@author: est5
"""

def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2
        
def f(x): return x**3-10*x**2+5

a,b,dx=(0.0,1.5,0.001)
print 'El intervalo es:'
x1,x2=buscaraiz(f,a,b,dx)
print x1,x2
xmed=(x1+x2)/2.
print 'la raiz es'
print xmed
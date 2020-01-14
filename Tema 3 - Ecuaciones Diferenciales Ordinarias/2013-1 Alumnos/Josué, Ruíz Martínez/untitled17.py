# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:41:45 2012

@author: est5
"""

from math import *
def buscaraiz(f,a,b,dx):
    x1=a;f1=f(a)
    x2=a+dx;f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2;f1=f2
        x2=x1+dx;f2=f(x2)
    else:
        return x1,x2
def f(x): return x-tan(x)
a,b,dx=(0.0,20.1,20/7.0)
x1,x2=buscaraiz(f,a,b,dx)
print x1,x2
xmed=(x1+x2)/2
while xmed<20:
    x1=x2 
    x2=x2+dx
    xmed=(x1+x2)/2
    while (f(x1)*f(xmed))<0:
        x2=xmed
    else:
        x1=xmed
    j=1.0*10**-4 
    i=abs(x1-x2)
    if i<j:
        break
    print 'la raiz es', xmed

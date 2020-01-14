# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:22:12 2012

@author: pako
"""

from math import *

def bisecta(f,a,b):
    x1=a; f1=f(a)
    x2=b; f2=f(b)
    x3=(a+b)/2.; f3=f(x3)
    while abs(x1-x2)>1e-4:
        if f1*f3<0.0: 
            x2=x3; f2=f(x2)
            x3=(x1+x2)/2.; f3=f(x3)
            #print x1,x2
        elif f2*f3<0.0:
            x1=x3; f1=f(x1)
            x3=(x1+x2)/2.; f3=f(x3)
            #print x1,x2
    return x1
    
def f(x): return x**3-10*x**2+5.
a,b=0.0,1.5
print 'La raíz es:'
raiz=bisecta(f,a,b)
print raiz
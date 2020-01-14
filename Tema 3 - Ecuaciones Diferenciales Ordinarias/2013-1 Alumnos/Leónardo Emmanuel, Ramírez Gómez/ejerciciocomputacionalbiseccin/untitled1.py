# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:47:25 2012

@author: est5
"""

#deltax=0.2 f(x)=x3-10x2+5


#x-tan(x)  0<=x<=20
#tolerancia 1x10**-4

from math import *
def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2
        
def f(x): return x-tan(x)
a=0.0
dx=0.0001
b=20.0
while a<20:
    x1,x2=buscaraiz(f,a,b,dx)
    print 'El intervalo es:'
    print x1,x2
    a=a+dx
    
    

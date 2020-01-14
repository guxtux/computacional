# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/pako/.spyder2/.temp.py
"""
from math import *

def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else: return x1,x2

def f(x): return x**3-10*x**2+5
a,b,dx=(0.0,1.5,0.2)
print 'El intervalo es:'
x1,x2=buscaraiz(f,a,b,dx)
print x1,x2

def g(x): return x-tan(x)
a,b,dx=(0.0,20,0.2)
print 'El intervalo es:'
x1,x2=buscaraiz(g,a,b,dx)
print x1,x2
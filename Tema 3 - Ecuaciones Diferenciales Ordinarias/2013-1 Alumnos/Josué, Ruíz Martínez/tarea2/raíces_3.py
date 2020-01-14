# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:19:52 2012

@author: pako
"""

from math import *

def f(x): return sin(x)-0.1*x
def df(x): return cos(x)-0.1

def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return b,b
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else: return x1,x2

def bisecta(f,a,b):
    x1=a; f1=f(a)
    x2=b; f2=f(b)
    x3=(a+b)/2.; f3=f(x3)
    if f1==0.0: return x1
    else:
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

a,b,dx=(-20.,20.,0.02)
raiz=0.0
while raiz<b:
    x1,x2=buscaraiz(f,a,b,dx)
    raiz=bisecta(f,x1,x2)
    if x1!=x2:
        print 'El intervalo en el que hay una raiz es: (',x1,',',x2,')'
        print 'La raiz es:',raiz
        a=x2
        if a<=b:
            print "\nEl nuevo intervalo es: (",a,",",b,")"
    else: print "No hay más raícez en el intervalo\n"

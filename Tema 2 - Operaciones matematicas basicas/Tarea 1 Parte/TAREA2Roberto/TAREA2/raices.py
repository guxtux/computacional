# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:25:05 2013

@author: est5
"""
##module raices
def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None,None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2

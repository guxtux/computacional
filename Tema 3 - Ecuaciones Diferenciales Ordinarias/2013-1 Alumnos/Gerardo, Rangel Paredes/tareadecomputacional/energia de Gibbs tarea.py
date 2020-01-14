# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from math import*
def f(x): return -8.311441*x*log((x/(4.44418))**((5.)/(2.))) + 100000
def df(x): return 10.2147 - 8.31144*log(x**((5.)/(2.)))

def newtonRaphson(x, tol=1e-5):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol : return x, i
        print "son demasiadas iteraciones\n"

raiz, numlter = newtonRaphson(8)

print "Raiz =", raiz
print "Numero de iteraciones = ", numlter



   




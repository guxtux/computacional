# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
def f(x): return 249.2*(1-x)**3 - x*(3-2*x)**2
def df(x): return -3*249.2*(1-x)**2 + (3-2*x)**2 + 4*x*(3-2*x)

def newtonRaphson(x, tol=1e-5):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol : return x, i
        print "son demasiadas iteraciones\n"

raiz, numlter = newtonRaphson(0.7)

print "Raiz = ", raiz
print "Numero de iteraciones = ", numlter

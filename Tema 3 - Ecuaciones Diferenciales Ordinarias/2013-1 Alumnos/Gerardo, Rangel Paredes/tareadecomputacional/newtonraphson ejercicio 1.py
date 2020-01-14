# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
def f(x): return x**4 + 0.9*x**3 - 2.3*x**2 + 3.6*x - 25.2
def df(x): return 4.0*x**3 + 2.7*x**2 - 4.6*x + 3.6

def newtonRaphson(x, tol=1e-5):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol : return x, i
        print "son demasiadas iteraciones\n"

raiz, numlter = newtonRaphson(-1.0)

print "Raiz =", raiz
print "Numero de iteraciones = ", numlter

    
        
   




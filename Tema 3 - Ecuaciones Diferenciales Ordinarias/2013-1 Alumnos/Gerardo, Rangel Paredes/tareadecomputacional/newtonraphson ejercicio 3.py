# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from math import*
def f(x): return sin(x) - 0.1*x
def df(x): return cos(x) - 0.1

def newtonRaphson(x, tol=1e-5):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol : return x, i
        print "son demasiadas iteraciones\n"

raiz1, numlter1 = newtonRaphson(-8.5)
raiz2, numlter2 = newtonRaphson(-7.0)
raiz3, numlter3 = newtonRaphson(-3.0)
raiz4, numlter4 = newtonRaphson(0.5)
raiz5, numlter5 = newtonRaphson(3.0)
raiz6, numlter6 = newtonRaphson(7.0)
raiz7, numlter7 = newtonRaphson(9.0)

print "Raiz1 =", raiz1
print "Raiz2 =", raiz2
print "Raiz3 =", raiz3
print "Raiz4 =", raiz4
print "Raiz5 =", raiz5
print "Raiz6 =", raiz6
print "Raiz7 =", raiz7
print "Numero de iteraciones = ", numlter1
print "Numero de iteraciones = ", numlter2
print "Numero de iteraciones = ", numlter3
print "Numero de iteraciones = ", numlter4
print "Numero de iteraciones = ", numlter5
print "Numero de iteraciones = ", numlter6
print "Numero de iteraciones = ", numlter7

    
        
   




# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:02:45 2012

@author: est5
"""

def f(x): return  x**4 + 2*x**3 - 7*x**2 + 3 #def de la funcion
def df(x): return 4.0*x**3 + 6.0*x**2 - 14.0*x 

def newtonRaphson(x, tol=1e-03):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x,i
    print "Son demasiadas iteraciones\n"
    
raiz1, numlter1 = newtonRaphson(-4.0)
raiz2, numlter2 = newtonRaphson(-1.0)
raiz3, numlter3 = newtonRaphson(0.5)
raiz4, numlter4 = newtonRaphson(1.5)

print "Raiz 1 = ", raiz1; print "Raiz 2 = ", raiz2; print "Raiz 3 = ", raiz3; print "Raiz 4 = ", raiz4
print "Numero de iteraciones para 1 = ", numlter1; print "Numero de iteraciones para 2 = ", numlter2; print "Numero de iteraciones para 3 = ", numlter3; print "Numero de iteraciones para 4 = ", numlter4
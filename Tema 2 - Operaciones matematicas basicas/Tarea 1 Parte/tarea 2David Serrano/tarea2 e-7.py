# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:51:39 2013

@author: Deivid
"""
#de acuerdo a la grafica se ve que tenemos raices en x=+-5e7
from numpy import *
import matplotlib.pyplot as plt

g=77000.0
L=1000.0
s=1100.0
a=g*L
c=a/2
b=2/a
def f(x): return (b*x)*sinh(c/x) - s/L
def df(x): return b*sinh(c/x)-cosh(c/x)*(c/(x**2.0))*(b*x)

def newtonRaphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonRaphson(-5e7)
#la raiz negativa no tiene mucho sentido en el problema
raiz2 , numIter2=newtonRaphson(5e7)

max=raiz2*cosh(c/raiz2)


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
print 'Raiz2= ' , raiz2
print 'Numero de iteraciones2= ', numIter2
print 'la tracción maxima en el cable es: ',max

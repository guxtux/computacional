# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:07:59 2012

@author: marisolchavez
"""

"""
Ejercicio 2 

Por el metodo de Newton-raphson
En este metodo se tiene que proponer un punto X cercano a donde se creen
que se encuentran las raices
"""

from math import *
import numpy as np


def f(x): return x**4 + 2.0*x**3 - 7.0*x**2 + 3.0 #el polinomio
    
def df(x): return 4.0*x**3 + 6.0*x**2 - 14.0*x # derivada del polinomio
 
   
# Ahora viendo la grafica proponemos unos X0 iniciales cercanos a las raices
x0=[-4.0,-0.5,1.0,1.5] 


def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx = -f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print "Son demasiadas iteraciones\n"
    
for i in range(4)   :
    raiz,numiter = newtonRaphson(x0[i]) 

    print "Raiz  = ", raiz
    print "Numero de iteraciones = ", numiter


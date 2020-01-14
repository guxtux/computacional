# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:43:18 2012

@author: marisolchavez
"""

"""
Ejercicio 1 

Por el metodo de Newton-raphson
En este metodo se tiene que proponer un punto X cercano a donde se creen
que se encuentran las raices
"""


from math import *
import numpy as np



def f(x): return x**4 + 0.9*x**3 - 2.3*x**2 + 3.6*x - 25.2 #el polinomio
    
def df(x): return 4.0*x**3 + 2.7*x**2 - 4.6*x + 3.6 # derivada del polinomio
    

# Ahora viendo la grafica proponemos unos X0 iniciales cercanos a las raices
x0 = [-3.0,2.0]  

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx = -f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print "Son demasiadas iteraciones\n"
    
for i in range(2)   :
    raiz,numiter = newtonRaphson(x0[i]) 

    print "Raiz  = ", raiz
    print "Numero de iteraciones = ", numiter
   


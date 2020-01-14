# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:43:47 2012

@author: marisolchavez
"""


"""
Ejercicio 3 

Por el metodo de Newton-raphson
En este metodo se tiene que proponer un punto X cercano a donde se creen
que se encuentran las raices
"""

from math import *
import numpy as np


def f(x): return np.sin(x)-0.1*x #el polinomio
    
def df(x): return np.cos(x)-0.1 #la derivada del polinomio
 
   
# Ahora viendo la grafica proponemos unos X0 iniciales cercanos a las raices

x0=[-8.0,-7.0,-3.0,0.0,3.0,7.0,8.0] 

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx = -f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print "Son demasiadas iteraciones\n"
    
for i in range(7)   :
    raiz,numiter = newtonRaphson(x0[i]) 

    print "Raiz  = ", raiz
    print "Numero de iteraciones = ", numiter


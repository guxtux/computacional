# -*- coding: utf-8 -*-
"""
PROBLEMA 2
La ecuacion de equilibrio quimio en la produccion de metanol a partir de CO
y H2 es:
    
    x(3-2x)^2/(1-x)^3=249.2
    
donde x es el grado de equilibrio de la reaccion. Determinar x.

@author: marisolchavez
"""


"""
 

Por el metodo de Newton-raphson
En este metodo se tiene que proponer un punto X cercano a donde se creen
que se encuentran las raices
"""

from math import *
import numpy as np


def f(x): return 756.6*x-759.6*(x**2.0)+253.2*(x**3.0)-249.2 #el polinomio ya desarrollado
    
def df(x): return 756.6-2*759.6*x+3*253.2*(x**2.0) #la derivada del polinomio
 
   
# Ahora viendo la grafica proponemos un X0 inicial cercano a la raiz

x0=[1.0] 

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx = -f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print "Son demasiadas iteraciones\n"
    
for i in range(1)   :
    raiz,numiter = newtonRaphson(x0[i]) 

    print "La Raiz real  = ", raiz
    print "Numero de iteraciones = ", numiter

#Solo para comprobarel resultado:
    
def poli(x): return (x*(3.0-2.0*x)**2)/((1.0-x)**3)

print "f(x)=", poli(raiz)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:23:17 2013

@author: acesimbrote
"""


#de acuerdo a la grafica se ve que tenemos una raiz en x=.8
from numpy import *
import matplotlib.pyplot as plt

def u(x): return x*(3-2*x)**2
def v(x): return (1-x)**3
def up(x): return ((3-2*x)**2)+8*x-12
def vp(x): return -3*((1-x)**2)
def f(x): return u(x)/v(x)-249.2
def df(x): return (up(x)*v(x)-vp(x)*u(x))/((v(x))**2)

def newtonRaphson(x,tol=1e-4):
    for i in range(10):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'  
    
raiz1 , numIter1=newtonRaphson(0.8)
print 'El grado de equilibrio de la eacción es:  ' , raiz1
print 'Numero de iteraciones= ', numIter1


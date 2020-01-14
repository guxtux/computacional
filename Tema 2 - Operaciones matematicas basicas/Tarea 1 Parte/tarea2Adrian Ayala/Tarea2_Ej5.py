# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:14:08 2013

@author: acesimbrote
"""


import math as mt
import matplotlib.pyplot as plt

R=8.311441
T0=4.44418
G=-1e5
m=13.3e3

def h(x): return mt.log(M0/(M0-m*x))
def f(x): return - R*x*(mt.log(x/T0)) - G
def df(x): return -R*((mt.log((x/T0)**2.5 )) + 2.5* (T0**1.5)/x**2.5)



def newtonRaphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonRaphson(1900)
#la raiz negativa no tiene mucho sentido en el problema


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1

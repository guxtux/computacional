# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:27:54 2013

@author: acesimbrote
"""


import math as mt
import matplotlib.pyplot as plt

g=9.81
u=2510
M0=2.8e6
m=13.3e3

def h(x): return mt.log(M0/(M0-m*x))
def f(x): return u*h(x)- g*x - u 
def df(x): return (u*m/(M0-m*x))-g



def newtonRaphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonRaphson(-600.8)
#la raiz negativa no tiene mucho sentido en el problema


print 'Raiz1= ' , raiz1
print 'Numero de iteraciones1= ', numIter1

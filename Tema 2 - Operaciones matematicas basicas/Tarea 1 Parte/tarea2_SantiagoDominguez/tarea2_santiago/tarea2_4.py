# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:15:56 2013

@author: san
"""

import math as mt
#La velocidad v de un cohete Saturno V en vuelo vertical cercano a la
#superficie de la Tierra puede aproximarse por "v=uln(M0/M0-mt) - gt"

g=9.81
u=2510
M0=2.8e6
m=13.3e3

def h(x): return mt.log(M0/(M0-m*x))
def f(x): return u*h(x)- g*x - 335 
def df(x): return (u*m/(M0-m*x))-g



def newtonraphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
tiempo , numIter1=newtonraphson(-500.0)


print 'tiempo(s)= ' , tiempo*(-1)
print 'Numero de iteraciones1= ', numIter1
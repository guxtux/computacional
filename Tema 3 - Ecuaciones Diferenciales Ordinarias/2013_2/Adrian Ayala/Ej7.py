# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:50:39 2013

@author: acesimbrote
"""

from numpy import *
import matplotlib.pyplot as plt

y=10.
a=-1./25.
h=1.
t=0.
A=[]

#La función a resolver
def f(y,t): return a*y

#La solución exacta 
def p(y,t): return 10*(exp(-1/25)*t)

for i in range(100):
    k1=h*f(y,t)
    t=t+h
    k2=h*f(y+k1,t)
    y=y+(0.5)*(k1+k2)
    A.append(y)

print  A[56],A[57]
plt.plot(A)
plt.show()

#Resolviendo la ecuación diferencial, encontramos que el valor del tiempo
#en el que la concentración llega a un décimo de su valor inicial es 
#aproximadamente t=57.56, lo cual concuerda con los valores impresos

#Para el inciso b

y=0.
h=1.
t=0.
b=-3./20.
c=1./10.
B=[]

def g(y,t): return b*y+c*(10.*(exp(-t/25.)))   

for i in range(100):
    k1=h*g(y,t)
    t=t+h
    k2=h*g(y+k1,t)
    y=y+(0.5)*(k1+k2)
    B.append(y)
    

print max(B)
plt.plot(B)
plt.show()

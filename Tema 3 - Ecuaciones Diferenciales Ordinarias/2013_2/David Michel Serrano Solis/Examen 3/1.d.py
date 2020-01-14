# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:54:20 2013

@author: acesimbrote
"""
#Para este ejercicio vemos dos posibilidades 

from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

t=0
y=1.0
h=0.01
n=5
u= linspace(t,n,n/h)

def f(y,t): return -y**2   # si y(t)>0
def h(y,t): return y**2    # si y(t)<0

#Valor exacto de la ecuación
def g(t): return 1/(t+1)   # si y(t)>0
def r(t): return -1/(t-1)  # si y(t)<0

#o=Euler_adelante(f,y,t,len(u),h)
#m=Euler_adelante(h,y,t,len(u),h)
#print 'El valor aproximado para y(5)= ', o[len(o)-1]
#print 'El valor aproximado para y(5)= ', m[len(m)-1]
plt.figure(1)
plt.subplot(211)
plt.plot(g(u),'r.')
plt.subplot(212)
plt.plot(r(u),'m-.')
#plt.plot(o,'b')
#plt.plot(m,'f:')
plt.show()
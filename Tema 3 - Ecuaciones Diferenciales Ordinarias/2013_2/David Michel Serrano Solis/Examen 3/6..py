# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:59:07 2013

@author: acesimbrote
"""

from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

t=0
y=10e5
h=0.05
n=1
lam=0.1044
 
u= linspace(t,n,n/h)

def f(y,t): return -lam*y

def g(t): return 10e5*exp(-lam*t) 

o=Euler_adelante(f,y,t,len(u),h)
print 'El valor aproximado para N(1hora)= ', o[len(o)-1]


plt.plot(g(u),'r.')
plt.plot(o,'b')
plt.show()

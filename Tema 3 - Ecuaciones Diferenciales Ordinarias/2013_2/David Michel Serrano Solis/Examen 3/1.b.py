# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:14:24 2013

@author: acesimbrote
"""

from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

t=0
y=1.0
h=0.01
n=5
u= linspace(t,n,n/h)

def f(y,t): return exp(-t)-3*y

#Valor exacto de la ecuación diferencial (resuelta por factor integrante)

def g(t): return 0.5*exp(-3*t)*(exp(2*t)+1) 

o=Euler_adelante(f,y,t,len(u),h)
print 'El valor aproximado para y(5)= ', o[len(o)-1]


plt.plot(g(u),'r.')
plt.plot(o,'b')
plt.show()
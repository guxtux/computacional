# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:16:28 2013

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

def f(y,t): return sin(t)-sqrt(abs(y))
def h(y,t): return sin(t)

#Valor exacto de la ecuación


o=Euler_adelante(f,y,t,len(u),h)
m=Euler_adelante(h,y,t,len(u),h)
#print 'El valor aproximado para y(5)= ', o[len(o)-1]
#print 'El valor aproximado para y(5)= ', m[len(m)-1]


plt.plot(o,'b')
plt.plot(m,'f:')
plt.show()
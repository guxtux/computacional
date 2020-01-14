# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:34:14 2013

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

def f(y,t): return (t**2)-y
def g(t): return (t**2)-(2*t)+2-(3/2)*exp(-t)

o=Euler_adelante(f,y,t,len(u),h)
print 'El valor aproximado para y(5)= ', o[len(o)-1]


plt.plot(g(u),'r.')
plt.plot(o,'b')
plt.show()
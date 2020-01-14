# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:21:10 2013

@author: acesimbrote
"""


from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

t=0
y=0.5
h=0.001
n=6
g=9.81
m=pi*(1./50)**2.
u= linspace(t,n,n/h)

def f(y,t): return (m*sqrt(2.*g*y))/((0.25)*(y**2.))
L=[]

o=Euler_adelante(f,y,t,len(u),h)
   
plt.plot(o,'b')
plt.show()
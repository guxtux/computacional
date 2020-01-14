# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:35:53 2013

@author: acesimbrote


Para el método de Euler hacia adelante tenemos Yn+1= Yn + hf(Yn,tn) como
fórmula general, entonces Y1=Y0 + hf(y0,t0); Y2=Y1 + hf(y1,t1)... etc. 
"""

#
from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

t=0
y=1.24
h=0.03

n=array([0,5,h])
print n

def f(y,t): return (3*y-0.5*exp(t))/(2*cos(t))

o=Euler_adelante(f,y,t,len(n),h)
print o
 

plt.plot(o,'b')
plt.show()




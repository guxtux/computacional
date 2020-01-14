# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:34:47 2013

@author: acesimbrote
"""

from numpy import *
import matplotlib.pyplot as plt

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
    


plt.plot(B)
plt.show()
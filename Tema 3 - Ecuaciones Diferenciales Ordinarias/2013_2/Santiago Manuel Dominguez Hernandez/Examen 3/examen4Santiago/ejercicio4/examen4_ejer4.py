# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:09:26 2013

@author: san
"""


from matplotlib.pylab import*    
from math import*
import  numpy as np


h=0.001
t=np.linspace(0,10,115)
y=np.linspace(0,10,115)
z=np.linspace(0,10,115)

def f1(y,z,t):
    return z
def f2(y,z,t):
    return -2*9.8*y - 0.8*z
yn=np.zeros(115)
zn=np.zeros(115)
for n in range(114):
    yn[0]=0.001
    zn[0]=0
    t[n]=n*h
    yn[n+1]=yn[n]+h*f1(yn[n],zn[n],t[n])
    zn[n+1]=zn[n]+h*f2(yn[n],zn[n],t[n])
print yn 
plot(t,yn)
plot(t,zn)
show()   
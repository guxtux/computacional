# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:24:05 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np


h=0.001
r1=0.02
r2=0.25**2
r3=sqrt(2.*9.89)
r4=(r1*r3)/(3.*pi*r2)
r5=sqrt(0.5)
t=np.linspace(0,5,300)
yn=np.linspace(0,0.0001,300)
def f(y,t):
    return -r4*sqrt(1.0/(y**3))
yn=np.zeros(300)
F=np.zeros(300)
for n in range(299):
    yn[0]=0.5
    yn[n+1]=yn[n]+h*f(yn[n],t[n])
print yn
for i in range(299):
    F[i]=sqrt(r5-r4*t[i]/(2.0))
print F
plot(t,F)
plot(t,yn)
show()   

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 03:04:55 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np


h=0.01
t=np.linspace(0,5,50)
x=np.linspace(0,5,50)
def f(x,t):
    return exp(-t)-3*x
xn=np.zeros(50)
for n in range(49):
    xn[0]=1
    xn[n+1]=xn[n]+h*f(x[n],t[n])
print xn 
plot(t,xn)
show()   

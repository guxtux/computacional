# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:37:01 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np


h=0.05
t=np.linspace(0,1,50)
x=np.linspace(0,1,50)
def f(x,t):
    return 0.1044*x
xn=np.zeros(50)
for n in range(49):
    xn[0]=10e5
    t[n]=n*h
    xn[n+1]=xn[n]+h*f(xn[n],t[n])
print xn 
plot(t,xn)
show()   

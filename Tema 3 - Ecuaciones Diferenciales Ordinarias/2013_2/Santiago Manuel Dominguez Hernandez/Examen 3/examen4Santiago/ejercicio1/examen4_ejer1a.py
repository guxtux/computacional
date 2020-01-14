# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:08:55 2013

@author: san
"""
from matplotlib.pylab import*    
from math import*
import  numpy as np


h=0.01
t=np.linspace(0,5,115)
xn=np.linspace(0,5,115)
def f(x,t):
    return 1 - t*x
xn=np.zeros(115)
for n in range(114):
    xn[0]=1
    xn[n+1]=xn[n]+h*f(xn[n],t[n])
print xn 
plot(t,xn)
show()   

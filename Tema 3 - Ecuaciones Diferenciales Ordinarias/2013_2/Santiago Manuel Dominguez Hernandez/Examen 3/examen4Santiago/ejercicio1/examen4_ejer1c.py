# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 03:12:57 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np


h=0.01
t=np.linspace(0,5,115)
x=np.linspace(0,5,115)
def f(x,t):
    return t**2-x
xn=np.zeros(115)
for n in range(114):
    xn[0]=0.5
    xn[n+1]=xn[n]+h*f(x[n],t[n])
print xn 
plot(t,xn)
show()   

# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:59:34 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np
h=1.0
b1=0.5
b2=-2./50.
t=np.linspace(0,50,150)
y=np.linspace(0,50,150)
k1=np.zeros(150)
k2=np.zeros(150)
yn=np.zeros(150)
def f1(y,t):
    return b2*y
def f2(y,k,t):
    return b2*y

for i in range(149):

    yn[0]=10.
    k1[i]=h*f1(yn[i],t[i])
    k2[i]=h*f2(yn[i],k1[i],t[i+1])
    yn[i+1]=yn[i]+b1*(k1[i]+k2[i])
print yn

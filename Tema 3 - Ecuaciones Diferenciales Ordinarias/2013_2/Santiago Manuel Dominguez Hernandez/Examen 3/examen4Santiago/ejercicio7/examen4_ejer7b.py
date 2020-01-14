# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:45:16 2013

@author: San
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np
h=1
b1=0.5
b2=-2./50.
b3=3./20.
b4=1./10.
t=np.linspace(0,100,50)
y=np.linspace(0,100,50)
z=np.linspace(0,100,50)
k1=np.zeros(50)
k2=np.zeros(50)
l1=np.zeros(50)
l2=np.zeros(50)
yn=np.zeros(50)
zn=np.zeros(50)
def f1(y,z,t):
    return b2*y
def f2(y,z,t):
    return -b3*z+b4*y


for i in range(49):
#    t[i]=h*i
    zn[0]=0.0
    yn[0]=10.
    k1[i]=h*f1(yn[i],zn[i],t[i])
    l1[i]=h*f2(yn[i],zn[i],t[i])    
    k2[i]=h*f1(yn[i]+k1[i],zn[i]+l1[i],t[i+1])
    l2[i]=h*f2(yn[i]+k1[i],zn[i]+l1[i],t[i+1])
    zn[i+1]=z[i]+b1*(k1[i]+k2[i])
    yn[i+1]=y[i]+b1*(l1[i]+l2[i])
print yn
print zn
plot(t,zn)
show()   
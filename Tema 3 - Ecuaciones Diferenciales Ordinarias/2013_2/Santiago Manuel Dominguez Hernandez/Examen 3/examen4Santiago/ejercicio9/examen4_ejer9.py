# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:07:05 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np
h=0.01
b1=0.5
b2=0.005
b3=pi*2
b4=2.
b5=1./6.
t=np.linspace(0,300,50)
y=np.linspace(0,300,50)
z=np.linspace(0,300,50)
k1=np.zeros(50)
k2=np.zeros(50)
k3=np.zeros(50)
l1=np.zeros(50)
l2=np.zeros(50)
l3=np.zeros(50)
yn=np.zeros(50)
zn=np.zeros(50)
xV=np.zeros(50)
yV=np.zeros(50)
def f1(y,z,t):
    return -b2*sqrt(y**2+z**2)*y
def f2(y,z,t):
    return -b3*-b2*sqrt(y**2+z**2)*z
    


for i in range(49):
    zn[0]=150.
    yn[0]=150.
    k1[i]=h*f1(yn[i],zn[i],t[i])
    l1[i]=h*f2(yn[i],zn[i],t[i])    
    k2[i]=h*f1(yn[i]+b1*k1[i],zn[i]+b1*l1[i],t[i+1]+h*b1)
    l2[i]=h*f2(yn[i]+b1*k1[i],zn[i]+b1*l1[i],t[i+1]+h*b1)
    k3[i]=h*f1(yn[i]-k1[i]*b4*k2[i],zn[i]-l1[i]+b4*l2[i],t[i]+h)
    l3[i]=h*f2(yn[i]-k1[i]*b4*k2[i],zn[i]-l1[i]+b4*l2[i],t[i]+h)
    zn[i+1]=zn[i]+b5*(k1[i]+4.0*k2[i]+k3[i])
    yn[i+1]=yn[i]+b5*(l1[i]+4.0*l2[i]+l3[i])
print zn
plot(t,zn)
show()   
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 01:26:46 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np
h=0.01
b1=0.5
fac=0.5
b5=1/6.
M=5.0
f0=1.
K=3.2
w=(K/M)**2
t=np.linspace(0,20,50)
y=np.linspace(0,300,50)
z=np.linspace(0,300,50)
k1=np.zeros(50)
k2=np.zeros(50)
k3=np.zeros(50)
k4=np.zeros(50)
l1=np.zeros(50)
l2=np.zeros(50)
l3=np.zeros(50)
l4=np.zeros(50)
yn=np.zeros(50)
zn=np.zeros(50)
xV=np.zeros(50)
yV=np.zeros(50)
def f1(y,z,t):
    return z
def f2(y,z,t):
    return -w**2*y-2.*fac*w*z
    


for i in range(49):
    if t[i]<10 :
        F=f0/M
    elif t[i]>10:
        F=0.0
    else:
        zn[0]=3.0
        yn[0]=0.
        k1[i]=h*f1(yn[i],zn[i],t[i])
        l1[i]=h*(f2(yn[i],zn[i],t[i])+F)    
        k2[i]=h*f1(yn[i]+b1*k1[i],zn[i]+b1*l1[i],t[i]+h*b1)
        l2[i]=h*(f2(yn[i]+b1*k1[i],zn[i]+b1*l1[i],t[i]+h*b1)+F)
        k3[i]=h*f1(yn[i]-k1[i]*b1*k2[i],zn[i]-l1[i]+b1*l2[i],t[i]+h)
        l3[i]=h*(f2(yn[i]-k1[i]*b1*k2[i],zn[i]-l1[i]+b1*l2[i],t[i]+h*b1)+F)
        k4[i]=h*f1(yn[i]+k3[i],zn[i]+l3[i],t[i]+h)
        l4[i]=h*(f2(yn[i]+k3[i],zn[i]+l3[i],t[i]+h)+F)
        zn[i+1]=zn[i]+b5*(k1[i]+b1*k2[i]+b1*k3[i]+k4[i])
        yn[i+1]=yn[i]+b5*(l1[i]+b1*l2[i]+b1*l3[i]+l4[i])
print zn
print yn
plot(t,zn)
show()   
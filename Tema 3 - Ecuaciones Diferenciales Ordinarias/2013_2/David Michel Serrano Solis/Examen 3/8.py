# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:07:56 2013

@author: Deivid
"""
from numpy import *
import matplotlib.pyplot as plt   
c=0.005
t=0.
g=9.9
u=150.0
v=150.0
x=0.
y=0.
h=0.1
V=sqrt((u**2.)+(v**2.))
X=[]
Y=[]

    
for i in range(100):
    k1=-h*V*c*u
    l1 = (-g-c*V*v)*h
    t=t+h
    V=sqrt((u+k1)**2.+(v+l1)**2.)
    k2 = -c*V*(u+k1)*h
    l2 = (-g-c*V*(v+l1))*h
    UU=u+(k1+k2)/2.
    VV=v+(l1+l2)/2. 
    x= x+ 0.5*(u+UU)*h
    y= y+ 0.5*(v+VV)*h
    X.append(x)
    Y.append(y)


plt.plot(X,Y)
plt.show()

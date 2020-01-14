# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:45:04 2013

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
    V=sqrt((u+(0.5)*k1)**2.+(v+(0.5)*l1)**2.)
    k2 = -c*V*(u+k1)*(3./2.)*h
    l2 = (-g-c*V*(v+l1))*(3./2.)*h
    V=sqrt((u-k1+2*k2)**2+(v-l1+2*l2)**2)
    k3=-c*V*(u-k1+2.*k2)*2.*h
    l3 = (-g-c*V*(v-l1+2.*l2))*2.*h
    UU=u+(1./6)*(k1+4*k2+k3)
    VV=v+(1./6)*(l1+4*l2+l3) 
    x= x+ 0.5*(u+UU)*h
    y= y+ 0.5*(v+VV)*h
    X.append(x)
    Y.append(y)
    
plt.plot(X,Y)
plt.show()
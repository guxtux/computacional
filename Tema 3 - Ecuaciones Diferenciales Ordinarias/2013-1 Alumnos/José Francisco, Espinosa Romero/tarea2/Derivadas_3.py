# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:09:14 2012

@author: pako
"""

import numpy as np
from math import *

def x(a):
    r=90.*(cos(a)+sqrt(2.5**2-sin(a)**2))
    return r

def d2f(f,x,h):
    d2f=(f[x+h]-2*f[x]+f[x-h])/(5*pi/180)**2
    return d2f

a=np.arange(0,185*pi/180,5*pi/180)
X=[]

for i in range (37):
    X.append(x(a[i]))

X=np.array(X)
v=50.
print X,"\n"

d2x=v*(-3*X[0]+4*X[1]-X[2])/(2*5*pi/180)
print "derivada de b en %3.1f grados = %3.5f" %(a[0]*180/pi,d2x)
for i in range(1,36):
    d2x=v*d2f(X,i,1)
    print "derivada de b en %3.1f grados = %3.5f" %(a[i]*180/pi,d2x)
    i+=1
d2x=v*(3*X[36]-4*X[35]+X[34])/(2*5*pi/180)
print "derivada de b en %3.1f grados = %3.5f" %(a[36]*180/pi,d2x)
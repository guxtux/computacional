# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/jeanhakunamatata/.spyder2/.temp.py
"""
import numpy as np
from math import *
from numpy import *

def coeficientes (xDatos, yDatos):
    m=len(xDatos)
    c=yDatos.copy()
    
    for k in range(1,m):
        c[k:m]=(c[k:m] - c[k-1])/(xDatos[k:m] - xDatos[k-1])
        
    return c


xDatos= array([-30.0, 0.0, 30.0])
yDatos= array([6870.0, 6728.0, 6615.0])

c= coeficientes(xDatos, yDatos)


def df(theta): return 2*c[0]*theta + c[1]

a, b=(0.0, 1000.0)

theta1=a; theta2=b
while True:
    thetamedia=(theta1+theta2)/2
    if f(thetamedia)==0.0:
        break
    if (f(tetha1)*f(thetamedia))<0:
        theta2=tethamedia
    else:
        theta1=thetamedia

    error=1.0*10**-4
    
    if abs(theta1-theta2)<error:
        break

print 'El mínimo es:'
print theta1
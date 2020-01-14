# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:10:27 2013

@author: acesimbrote
"""
import matplotlib.pyplot as plt
from numpy import *

#Condiciones iniciales
y0=0.2
z0=0.
h=0.001

#Constantes y arreglos
g=9.81
y1=[]
z1=[]
t=[]
I=[0,10]
A=[]

def y(x,t): return -2*g*x
def m(): return 0

def euler(y,z,h,I,y0,v0):
    y1.append(y0)
    z1.append(z0)
    t.append(intervalo[0])
    i=0
    while t[i]<=I[1]:
        z0=z0+h*z(y0,t[i])
        z1.append(z0)
        y0=y0+h*z0
        y1.append(z0)
        t.append(t[i]+h)
        i=i+1
    return z1,y1,t

a,b,c=euler(m,y,h,I,y0,z0)
for x in t:
    A.append(cos(sqrt(2*9.81)*x))
    
plt.plot(b,a,b,A)
plt.show()



    
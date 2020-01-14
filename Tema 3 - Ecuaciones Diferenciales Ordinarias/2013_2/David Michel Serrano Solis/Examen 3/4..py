# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:41:17 2013

@author: Deivid
"""
from numpy import *
import matplotlib.pyplot as plt
g=9.81
L=1.0
t=0.0
h=0.001
y=0
x1=0.001
H=[]
T=[]
def f(x,y,t): return ((-2.*g*x)-(0.8*y))/L
def Euler_adelante(f,x1,y,t,h):
    for i in range(10000):
        xn=f(x1,y,t)
        xn=x1+h*xn
        t=t+h
        x1=xn
        H.append(x1)
        T.append(t)
    return H
H=Euler_adelante(f,x1,y,t,h)
print max(H)
print min(H)
plt.plot (T,H)
plt.show()
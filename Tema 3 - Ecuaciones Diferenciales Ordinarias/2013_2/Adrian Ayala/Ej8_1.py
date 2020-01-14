# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:49:09 2013

@author: acesimbrote
"""

from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

#CONSTANTES
k=3.2    #Kg/s
M=5      #Kg
w=k/M    #1/s
S=0.5
g=9.9
c=0.005


#Condiciones iniciales. 
#Para estas estoy considerando una distancia y=2 metros, 

t=0.
tf=20.
u=150.
v=150.
h=0.1

def f(v,u,t): return -c*sqrt((u**2)+(v**2))*u   
def g(v,u,t): return -c*sqrt((u**2)+(v**2))*v-g   
def j(u,t): return u
def i(v,t): return v

A=[]
B=[]

for e in range(100):
    
    k1=h*f(u,v,t)
    I1=h*g(u,v,t)
    t=t+h
    k2=h*f(u+k1,v+I1,t)
    I2=h*g(u+k1,v+I1,t)
    u=u+(I1+I2)*0.5
    v=v+(k1+k2)*0.5
    A.append(u)
    B.append(v)


plt.plot(A,'b')
plt.plot(B,'r')
#plt.plot(Q,'r')
plt.show()
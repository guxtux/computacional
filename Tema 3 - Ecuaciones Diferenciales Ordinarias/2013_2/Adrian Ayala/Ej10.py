# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:09:43 2013

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


#Condiciones iniciales. 
#Para estas estoy considerando una distancia y=2 metros, 

t=0.
tf=10.
z=0.
y=2.
h=0.1

def f(y,z,t): return z   
def g(y,z,t): return -(2*S*w)*z -(w**2)*y 

A=[]
B=[]

while t<=tf:
    k1=h*f(y,z,t)
    I1=h*g(y,z,t)
    k2=h*f(y+(k1/2.),z+(I1/2.),t+(h/2.))
    I2=h*g(y+(k1/2.),z+(I1/2.),t+(h/2.))
    k3=h*f(y+(k2/2.),z+(I2/2.),t+(h/2.))
    I3=h*g(y+(k2/2.),z+(I2/2.),t+(h/2.))
    k4=h*f(y+k3,z+I3,t+h)
    I4=h*g(y+k3,z+I3,t+h)
    t=t+h
    y=y+(1/6.)*(k1+2*k2+2*k3+k4)
    z=z+(1/6.)*(I1+2*I2+2*I3+I4)
    A.append(y)
    B.append(z)

plt.plot(A,'b')
plt.plot(B,'r')
#plt.plot(Q,'r')
plt.show()
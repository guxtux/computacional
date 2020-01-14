# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:31:37 2013

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
z=0.
y=2.
h=0.01

def f(y,z,t): return z   
def g1(y,z,t): return -(2*S*w)*z -(w**2)*y
def g2(y,z,t): return -(2*S*w)*z -(w**2)*y +2*t 
def g3(y,z,t): return -(2*S*w)*z -(w**2)*y +2(1-t)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]


while t<=1:
    k1=h*f(y,z,t)
    I1=h*g1(y,z,t)
    k2=h*f(y+(k1/2.),z+(I1/2.),t+(h/2.))
    I2=h*g1(y+(k1/2.),z+(I1/2.),t+(h/2.))
    k3=h*f(y+(k2/2.),z+(I2/2.),t+(h/2.))
    I3=h*g1(y+(k2/2.),z+(I2/2.),t+(h/2.))
    k4=h*f(y+k3,z+I3,t+h)
    I4=h*g1(y+k3,z+I3,t+h)
    t=t+h
    y=y+(1/6.)*(k1+2*k2+2*k3+k4)
    z=z+(1/6.)*(I1+2*I2+2*I3+I4)
    A.append(y)
    B.append(z)

m=linspace(1,2,100)
h=0.01
t1=0
y1=2
z1=0

for i in m:
    k1=h*f(y1,z1,t1)
    I1=h*g2(y1,z1,t1)
    k2=h*f(y1+(k1/2.),z1+(I1/2.),t1+(h/2.))
    I2=h*g2(y1+(k1/2.),z1+(I1/2.),t1+(h/2.))
    k3=h*f(y1+(k2/2.),z1+(I2/2.),t1+(h/2.))
    I3=h*g2(y1+(k2/2.),z1+(I2/2.),t1+(h/2.))
    k4=h*f(y1+k3,z1+I3,t1+h)
    I4=h*g2(y1+k3,z1+I3,t1+h)
    t1=t1+h
    y1=y1+(1/6.)*(k1+2*k2+2*k3+k4)
    z1=z1+(1/6.)*(I1+2*I2+2*I3+I4)
    C.append(y1)
    D.append(z1)

h=0.01
t2=0
y2=2
z2=0

while t2>=1000:
    k1=h*f(y2,z2,t2)
    I1=h*g3(y2,z2,t2)
    k2=h*f(y2+(k1/2.),z2+(I1/2.),t2+(h/2.))
    I2=h*g3(y2+(k1/2.),z2+(I1/2.),t2+(h/2.))
    k3=h*f(y2+(k2/2.),z2+(I2/2.),t2+(h/2.))
    I3=h*g3(y2+(k2/2.),z2+(I2/2.),t2+(h/2.))
    k4=h*f(y2+k3,z2+I3,t2+h)
    I4=h*g3(y2+k3,z2+I3,t2+h)
    t2=t2+h
    y2=y2+(1/6.)*(k1+2*k2+2*k3+k4)
    z2=z2+(1/6.)*(I1+2*I2+2*I3+I4)
    E.append(y2)
    F.append(z2)

#plt.figure(1)
#plt.subplot(211)
#plt.plot(J,'b')
#plt.subplot(212)
#plt.plot(S,'r')
#plt.show()

plt.figure(1)
plt.plot(A,'b')
plt.plot(B,'r')
plt.figure(2)
plt.plot(C,'b')
plt.plot(D,'r')
plt.figure(3)
plt.plot(E,'b')
plt.plot(F,'r')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:46:36 2012

@author: pako
"""
import numpy as np
from math import*
import matplotlib.pyplot as plt

f=-0.93*1.2*0.5/250
v0=67.0
g=9.81

def x(w,t):
    f=-0.93*1.2*0.5/250
    v0=67.0
    a=f*cos(w)
    x1=(v0/f)*(exp(a*t)-1)
    return x1
    
def y(w,t):
    f=-0.93*1.2*0.5/250
    v0=67.0
    g=9.81
    b=f*sin(w)
    y1=(((v0/f)-g/(b**2))*(exp(b*t)-1))+g*t/b
    return y1
    
c=np.arange(0.0,15,0.1)
plt.figure(1)
plt.ylabel('Altura [m]')
plt.xlabel('Distancia [m]')
plt.title('Trayectoria de la motocicleta como funcion del angulo de inclinacion')

h=0.0
j=0
w=pi/4
while h>=0:  
        plt.plot(x(w,c[j]),y(w,c[j]),'bs')
        h=y(w,c[j])
        j=j+1
w=pi/6.0
while w<=pi/2.0:
    j=0
    h=0.0
    while h>=0:  
        plt.plot(x(w,c[j]),y(w,c[j]),'r.')
        h=y(w,c[j])
        j=j+1
    w=w+(pi/6.0)
w=pi/8.0
while w<=pi/2.0:
    j=0
    h=0.0
    while h>=0:  
        plt.plot(x(w,c[j]),y(w,c[j]),'y.')
        h=y(w,c[j])
        j=j+1
    w=w+(pi/8.0)
w=pi/10.0
while w<=pi/2.0:
    j=0
    h=0.0
    while h>=0:  
        plt.plot(x(w,c[j]),y(w,c[j]),'g.')
        h=y(w,c[j])
        j=j+1
    w=w+(pi/10.0)
plt.show()

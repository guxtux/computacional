# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:28:18 2012

@author: pako
"""

import numpy as np
from math import*
import matplotlib.pyplot as plt

y0 = eval(raw_input("Altura inicial de la gota de agua en metros: "))
v0 = eval(raw_input("Velocidad inicial de la gota de agua en m/s: "))
#m = eval(raw_input("Masa de la gota en gramos: "))
#k = eval(raw_input("Coeficiente de la fuerza resistiva: "))
g,i=9.81,0
t=np.arange(0.0,5,0.2)
a=[0.1,1,5.9,100]
#b=m/k
def yr(t,a):
    y1=y0+a*g*t+(a*a-a*v0/g)*(np.exp(-g*t/a)-1)
    return  y1
    
def vr(t,a):
    v1=a*g+(v0-a*g)*np.exp(-g*t/a)
    return v1
    
def yl(t):
    yl=y0+v0*t+g*t*t/2
    return yl
    
def vl(t):
    vl=v0+g*t
    return vl

while i<len(a):
    
    plt.figure(i)
    
    plt.subplot(211)
    plt.title('Distancia vs Tiempo')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Distancia [m]')
    plt.plot(t,yr(t,a[i]),'g--',t,yl(t),'m--')
    
    plt.subplot(212)
    plt.title('Velocidad vs Tiempo')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Velocidad [m/s]')
    plt.plot(t,vr(t,a[i]),'g--',t,vl(t),'m--')
    
    plt.show()
    
    i+=1

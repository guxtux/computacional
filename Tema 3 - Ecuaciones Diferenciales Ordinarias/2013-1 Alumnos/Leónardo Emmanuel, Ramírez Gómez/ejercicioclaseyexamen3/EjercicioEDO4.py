# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:13:23 2012

@author: est5
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#Se definen las variables y las condiciones iniciales
Yn=[]
h=.25
q=3000.
A=.25
p=300.
c=900.
s=5.67*10**-8
v=.001
hc=30.
e=.8
T=473.
t=0.

#Se hace los calculos
for i in range(100):
    t=t+h
    k1=(e*s*((297**4)-(T**4))+hc*(297.-T))*A/(p*c*v)
    k2=(e*s*((297**4)-((T+k1/2.)**4))+hc*(297.-T+k1/2.))*A/(p*c*v) 
    k3=(e*s*((297**4)-((T+k2/2.)**4))+hc*(297.-T+k2/2.))*A/(p*c*v)
    k4=(e*s*((297**4)-((T+k3)**4))+hc*(297.-T+k3))*A/(p*c*v)    
    T=T+(1/6.)*(k1+2.*k2+2.*k3+k4)
    Yn.append(T)
print Yn
#Graficamos las soluciones
t=arange(0,100)
plt.plot(t,Yn)
plt.xlabel("t(s)")
plt.ylabel("y(t)")
plt.show()

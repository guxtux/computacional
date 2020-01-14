# -*- coding: utf-8 -*-
"""
CALENTAMIENTO
Calcula la temperatura si T inicial es 25ºC y q=3000

T´=(1/(rho*c*v))*(q-epsilon*sigma*A*((T**4.0)-298**4.0)-hc*A*(T-298.0))
T(0)=473

@author: marisolchavez
"""
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt


tiem=np.zeros([1001])
tem=np.zeros([1001])

#Constantes que se utilizan
rho=300
v=0.001
A=0.25
c=900
hc=30
epsilon=0.8
sigma=5.67e-8
q=3000.0




h=0.1
t=0.0
tiem[0]=t


T=298.0
tem[0]=T



#Comienza el metodo RK4

#f(t)=T'(t)
def f(T): return (1/(rho*c*v))*(q-epsilon*sigma*A*((T**4.0)-298**4.0)-hc*A*(T-298.0))

t=eval(raw_input('Hasta que segundo quieres la temperatura: ' ))



for i in range(0,1001):
   
    t=i*h
    tiem[i]=t
    K1=h*f(T) 
    K2=h*f(T+K1/2.0)
    K3=h*f(T+K2/2.0)
    K4=h*f(T+K3)
      

    T=T+(K1+2.0*K2+2.0*K3+K4)/6.0
    tem[i]=T
      
    print "La temperatura en " ,t, "segundos es: ", tem[t/h], "Kelvin"

plt.plot(tiem,tem)
plt.show()

    

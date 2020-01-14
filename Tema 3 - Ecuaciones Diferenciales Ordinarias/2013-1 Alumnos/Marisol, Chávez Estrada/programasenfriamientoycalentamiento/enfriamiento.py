# -*- coding: utf-8 -*-
"""
ENFRIAMIENTO
Calcula el valor de T para el intervalo 0<t<100 segundos, usa h=0.25

T´=(A/(rho*c*v))*(epsilon*sigma*(297.0**4-T**4.0)+hc*(297-T))
T(0)=473

@author: marisolchavez
"""
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt


tiem=np.zeros([401])
tem=np.zeros([401])

#Constantes que se utilizan
rho=300
v=0.001
A=0.25
c=900
hc=30
epsilon=0.8
sigma=5.67e-8




h=0.25
t=0.0
tiem[0]=t


T=473.0
tem[0]=T
print "",tiem[0],tem[0]


#Comienza el metodo RK4

#f(t)=T'(t)
def f(T): return (A/(rho*c*v))*(epsilon*sigma*(297.0**4-T**4.0)+hc*(297-T))


for i in range(0,401):
   
    t=i*h
    tiem[i]=t
    K1=h*f(T) 
    K2=h*f(T+K1/2.0)
    K3=h*f(T+K2/2.0)
    K4=h*f(T+K3)
      

    T=T+(K1+2.0*K2+2.0*K3+K4)/6.0
    tem[i]=T
    print "",tiem[i],tem[i]

plt.plot(tiem,tem)
plt.show()
 
    




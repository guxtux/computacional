# Runge-Kutta 4o orden 1/3 simpson, temperatura
"""
@author: Calderon Apolinar Marco A
"""
from math import *
import matplotlib.pyplot as plt
def f(T):
    ro=300.0
    h=0.25
    v=0.001
    A=0.25
    c=900.0
    hc=30.0
    eps=0.8
    sig=5.67e-8
    return h*(A/ro*c*v)*(eps*sig*(297**4-T**4)+hc*(297-T))
ti=[]
T=[]
f0=473.0
t=0.0
while t<=100.0:
    k1=f(f0)
    k2=f(f0+0.5*k1)
    k3=f(f0+0.5*k2)
    k4=f(f0+0.5*k3)
    f0=f0+(1.0/6.0)*(k1+0.5*k2+0.5*k3+k4)
    ti.append(t)
    T.append(f0)
    t=t+0.25
    
plt.plot(ti,T)
plt.show()


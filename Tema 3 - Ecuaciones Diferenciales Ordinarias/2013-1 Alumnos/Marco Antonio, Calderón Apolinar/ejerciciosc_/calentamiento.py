# ejercicio extra de calentamiento
"""
@author: Calderon Apolinar Marco A
"""

from math import *
import matplotlib.pyplot as plt
def f(T):
    ro=300.0
    h=0.1
    v=0.001
    A=0.25
    c=900.0
    hc=30.0
    eps=0.8
    sig=5.67e-8
    q=3000
    return h*(1.0/ro*c*v)*(q-eps*sig*A*(T**4-298**4)-hc*A*(T-298))
ti=[]
T=[]
f0=25.0
t=0.0
min=eval(raw_input('hasta que minuto se desea la temperatura' ))
while t<=min:
    k1=f(f0)
    k2=f(f0+0.5*k1)
    k3=f(f0+0.5*k2)
    k4=f(f0+0.5*k3)
    f0=f0+(1.0/6.0)*(k1+0.5*k2+0.5*k3+k4)
    ti.append(t)
    T.append(f0)
    t=t+0.1
    
plt.plot(ti,T)
plt.show()
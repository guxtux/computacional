import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#Se definen las variables y las condiciones iniciales
Yn=[]
h=.1
q=3000.
A=.25
p=300.
c=900.
s=5.67*10**-8
v=.001
hc=30.
e=.8
T=298.
t=0.

#Se hace los calculos
for i in range(400):
    t=t+h
    k1=h*((1./(p*c*v))*(((q-e*s*A*(T**4-298.**4)) - hc*A*(T-298.)))) 
    k2=h*((1./(p*c*v))*(((q-e*s*A*((T+k1/2.)**4-298.**4))-hc*A*(T+k1/2.-298.))))
    k3=h*((1./(p*c*v))*(((q-e*s*A*((T+k2/2.)**4-298.**4))-hc*A*(T+k2/2.-298.))))
    k4=h*((1./(p*c*v))*(((q-e*s*A*((T+k3)**4-298.**4))-hc*A*(T+k3-298.))))
    T=T+(1/6.)*(k1+2.*k2+2.*k3+k4)
    Yn.append(T)
print Yn
#Graficamos las soluciones
t=arange(0,400)
plt.plot(t,Yn)
plt.xlabel("t(s)")
plt.ylabel("y(t)")
plt.show()
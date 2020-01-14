# Circuito RLC con diferentes Resistencias
"""
@author: Calderon Apolinar Marco A
"""
import matplotlib.pyplot as plt
def I(i,q,R):
    L=200.0
    C=0.001
    E=1.0
    return -(R/L)*i-(1.0/(L*C))*q+(E/L)
def fun(r):
 q0=0.0
 i0=0.0
 t=0.0
 ti=[]
 qs=[]
 iss=[]
 h=0.1
 while t<=5:
    k1=h*I(i0,q0,r)
    l1=h*i0
    k2=h*I(i0+0.5*k1,q0+0.5*l1,r)
    l2=h*(i0+0.5*k1)
    k3=h*I(i0+0.5*k2,q0+0.5*l2,r)
    l3=h*(i0+0.5*k2)
    k4=h*I(i0+k3,q0+l3,r)
    l4=h*(i0+k3)
    i0=i0+(1.0/6.0)*(k1+2*k2+2*k3+k4)
    q0=q0+(1.0/6.0)*(l1+2*l2+2*l3+l4)
    ti.append(t)
    qs.append(q0)
    iss.append(i0)
    t=t+0.1
 return ti,iss

x,y=fun(0) 
l,m=fun(50)
k,o=fun(100)
n,b=fun(300)
plt.plot(x,y,'r',l,m,'b',k,o,'g',n,b,'y')
plt.xlabel('tiempo')
plt.ylabel('corriente')
plt.show()
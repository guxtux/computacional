# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "MOVIMIENTO DE UN SISTEMA MASA-RESORTE FORZADO POR FUERZAS"
print "DEPENDIENTES DEL TIEMPO F(t), USANDO EL MÉTODO RK4."
from ecdif import *

def dY(Y,t):
    y,dy=Y
    d2y=f(t)/m -w**2*y -2.*z*w*dy
    return np.array([dy,d2y])

#Constantes [MKS]:    
m=5.                    #Masa
k=3.2                   #Constante del resorte
w=sqrt(k/m)             #Frecuencia no amortiguada
z=0.5                   #Factor de amortiguamiento
t0=0.; tn=10.; h=.1     #Extremos de t y paso h [s]
y0=0.; dy0=0.           #Condiciones iniciales [MKS]
Y0=np.array([y0,dy0])
T=np.arange(t0,tn+h,h)

#Problema 10: Fuerza escalonada
def f(t):
    if 0<=t<=1: return 1
    else: return 0
F=[]
for t in T:
    F.append(f(t))
y,dy=rk(4,dY,Y0,t0,tn,h).T

plt.title(u"Movimiento masa-resorte con fuerza escalonada")
plt.plot(T,F,label=u"Fuerza F(t) [N]")
plt.plot(T,dy,label=u"Velocidad de la masa dy/dt [m/s]")
plt.plot(T,y,"r",label=u"Posición de la masa y(t) [m]")
plt.xlabel(u"Tiempo t [s]")
plt.ylabel(u"Fuerza F(t) [N], Velocidad dy/dy [m/s], Posición y(t) [m]")
plt.ylim(-2,2)
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()

#Problema 11a: Fuerza triangular rara
def f(t):
    if 0<=t<1: return 2*t
    elif 1<=t<=2: return 2*(1-t)
    else: return 0
F=[]
for t in T:
    F.append(f(t))
y,dy=rk(4,dY,Y0,t0,tn,h).T

plt.title(u"Movimiento masa-resorte con fuerza triangular rara")
plt.plot(T,F,label=u"Fuerza F(t) [N]")
plt.plot(T,dy,label=u"Velocidad de la masa dy/dt [m/s]")
plt.plot(T,y,"r",label=u"Posición de la masa y(t) [m]")
plt.xlabel(u"Tiempo t [s]")
plt.ylabel(u"Fuerza F(t) [N], Velocidad dy/dy [m/s], Posición y(t) [m]")
plt.ylim(-2,2)
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()

#Problema 11b: Fuerza triangular corregida
def f(t):
    if 0<=t<1: return 2*t
    elif 1<=t<=2: return 2*(1-t)+2
    else: return 0
F=[]
for t in T:
    F.append(f(t))
y,dy=rk(4,dY,Y0,t0,tn,h).T

plt.title(u"Movimiento masa-resorte con fuerza triangular corregida")
plt.plot(T,F,label=u"Fuerza F(t) [N]")
plt.plot(T,dy,label=u"Velocidad de la masa dy/dt [m/s]")
plt.plot(T,y,"r",label=u"Posición de la masa y(t) [m]")
plt.xlabel(u"Tiempo t [s]")
plt.ylabel(u"Fuerza F(t) [N], Velocidad dy/dy [m/s], Posición y(t) [m]")
plt.ylim(-2,2)
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()

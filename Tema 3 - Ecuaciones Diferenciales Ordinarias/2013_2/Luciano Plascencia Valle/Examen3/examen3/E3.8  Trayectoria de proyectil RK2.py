# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "TRAYECTORIA DE UN PROYECTIL EN UN MEDIO RESISTIVO"
print "USANDO EL MÉTODO RK2"
from ecdif import *
from integral import *

def dV(V,t):
    Vx,Vy=V
    v=np.hypot(Vx,Vy)
    dVx=-c*v*Vx
    dVy=-c*v*Vy-g
    return np.array([dVx,dVy])

def vx(t): return evalf(T,Vx,t,h)
def vy(t): return evalf(T,Vy,t,h)

c=0.005                 #Coeficientes de arrastre
g=9.9                   #Aceleración por la gravedad [m/s**2]
t0=0.; tn=12.2; h=.2    #Extremos de t y paso h [s]
x0=y0=0.                #Condiciones iniciales [MKS]
vx0=150.;vy0=150.
V0=np.array([vx0,vy0])

#Cálculo de las velocidades resolviendo el sistema de EDO dV.
Vx,Vy=rk(2,dV,V0,t0,tn,h).T     

#Cálculo de las posiciones integrando las velocidades.
X,Y=[x0],[y0]
T=np.arange(t0,tn+h,h)
for i in range(1,len(T)):
    x=simpson(vx,t0,T[i],i)
    y=simpson(vy,t0,T[i],i)
    X.append(x)
    Y.append(y)

#Gráfica de trayectoria, posiciones y velocidades
plt.figure()
plt.title(u"Trayectoria del proyectil usando RK2")
plt.plot(X,Y,"ro-",label="Trayectoria y(x)")
plt.xlabel(u"x [m]")
plt.ylabel(u"y(x) [m]")
XYmin=min(0,min(X),min(Y))
XYmax=max(0,max(X),max(Y))
plt.xlim(0,XYmax)
plt.ylim(XYmin,XYmax)
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()

plt.figure()
plt.title(u"Velocidad del proyectil usando RK2")
plt.plot(T,Vx,label=u"Velocidad horizontal vx(t)")
plt.plot(T,Vy,label=u"Velocidad vertical vy(t)")
plt.plot(T,np.hypot(Vx,Vy),label="Rapidez V(t)")
plt.xlabel(u"Tiempo t [s]")
plt.ylabel(u"Velocidades vx,vy [m/s]")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()

plt.figure()
plt.title(u"Posición del proyectil usando RK2")
plt.plot(T,X,label=u"Posición horizontal x(t)")
plt.plot(T,Y,label=u"Posición vertical y(t)")
plt.xlabel(u"Tiempo t [s]")
plt.ylabel(u"Posiciones x,y [m]")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()

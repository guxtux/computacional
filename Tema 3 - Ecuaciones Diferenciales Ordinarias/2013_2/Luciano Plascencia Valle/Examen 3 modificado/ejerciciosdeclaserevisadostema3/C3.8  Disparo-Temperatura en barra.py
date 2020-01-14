# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu May  2 18:32:33 2013
MÉTODO DEL DISPARO
BARRA DE LONGITUD=10m CON TEMPERATURA EN LAS FRONTERAS
T(0)=0, T(10)=200
Sup. z(0)=dT(0)/dx=10. "Disparamos" este valor desde la condición de
frontera T(0)=0 y lo vamos modificando (se puede usar interpolación)
hasta obtener la otra condición de frontera T(10)=200.
"""
from scipy import integrate
import pylab as p
import numpy as np

def dY(Y,x=0.):
    dT,T=Y
    d2T=a*(T-Ta)
    return np.array([d2T,dT])

x0,xf=0,10.     #Condiciones de frontera
a=.01           #Coef. de transmisión [m**-2]
Ta=20.          #Temperatura ambiente
T0=0.
dT0=17.945      #Este es el valor q hay q ajustar con "disparos"
Y0=[dT0,T0]
X=np.linspace(x0,xf,11)
Y=integrate.odeint(dY,Y0,X).T
print " x    T(x)  dT/dx"
for i in X:
    print "%2i  %6.2f  %5.2f" %(X[i],Y[1,i],Y[0,i])

p.plot(X,Y[1],"ro-")
p.xlabel("Distancia x")
p.ylabel(u"Temperatura T")
p.title(u"Temperatura T vs. distancia x")
p.grid()
p.show()
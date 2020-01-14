# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:53:52 2013

@author: alberto
"""

#Importamos numpy y matplotlib 
import matplotlib.pyplot as plt
from numpy import *

#Definimos la funcion imprimeSoln como vimos en clase
def imprimeSoln(X,Y,freq):
    def imprimeEncabezado(n):
        print "\n   Tiempo [s]",
        print "   Posicion [rad]",
        print "   Velocidad [rad/s]",
        print
    def imprimeLinea(x,y,n):
        print "%13.4e" %x,
        for i in range(n):
            print "%13.4e" %y[i],
        print
    m=len(Y)
    try: n=len(Y[0])
    except TypeError: n=1
    if freq==0:
        freq=m
    
    imprimeEncabezado(n)
    for i in range(0,m,freq):
        imprimeLinea(X[i],Y[i],n)
    if i != m-1:
        imprimeLinea (X[m-1],Y[m-1],n)


# Definimos la funcion integra con los respectivos coeficientes del método Runge-Kutta
def integra(F,x,y,xAlto,h):
    
    def rk_4(F,x,y,h):
        k0=h*F(x,y)
        k1=h*F(x+h/2.0, y+k0/2.0)
        k2=h*F(x+h/2.0,y+k1/2.0)
        k3=h*F(x+h,y+k2)
        return (k0+2.0*k1+2.0*k2+k3)/6.0
        
    X=[]
    Y=[]
    X.append(x)
    Y.append(y)
    
    while x<xAlto:
        h=min(h,xAlto-x)
        y=y+rk_4(F,x,y,h)
        x=x+h
        X.append(x)
        Y.append(y)
    return array(X),array(Y)

#Escribimos F(x) en terminos de las constantes del problema y de las condiciones iniciales
def F(x,y):
    F=zeros((2), dtype="float64")
    F[0]=y[1]
    F[1]=-sin(y[0])
    return F

#Establecemos las condiciones iniciales y los parametros del problema.
x=0.0
xAlto=5*pi
y=array([1.0,0.0])
h=0.1
freq=5

#Resolvemos el sistema de ecuaciones.
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

#Implementamos un ciclo para elegir las crestas del movimiento.
P=Y[:,0]
Or=[]
for i in range(0,len(P)):
    if abs(1-P[i])<1e-4:
        z=X[i]
        Or.append(z)
        print "El péndulo se encuentra en su posicion inicial en %1.2f seg" %z
Periodo=Or[1]-Or[0]
#Estamos tomando el tiempo que tarda el pendulo en completar un movimiento completo y regresar a su punto de partida.
print "\n El periodo del pendulo es T= %1.3f seg" %Periodo


#Graficamos la amplitud del movimiento del pendulo.
plt.plot (X,P, "b-", label="Amplitud")
plt.legend(loc="upper right")
plt.ylabel("Posicion [rad]")
plt.xlabel("Tiempo [s]")
plt.plot(X,zeros(len(X)),"k--")
plt.show()
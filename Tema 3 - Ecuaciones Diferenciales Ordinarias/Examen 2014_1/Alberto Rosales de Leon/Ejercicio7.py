# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:05:15 2013

@author: alberto
"""

#Importamos numpy y matplotlib 
import matplotlib.pyplot as plt
from numpy import *

#Definimos la funcion imprimeSoln como vimos en clase
def imprimeSoln(X,Y,freq):
    def imprimeEncabezado(n):
        print "\n   Tiempo [s]",
        print "   PosX [m]",
        print "   PosY [m]",
        print "   VelX [m]",
        print "   VelY [m]",
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
    F=zeros((4), dtype="float64")
    g=9.80665
    CD=0.03
    M=0.25
    F[0]=y[2]
    F[1]=y[3]
    F[2]=-(CD/M)*(y[2])
    F[3]=-(CD/M)*(y[3])-g
    return F

#Establecemos las condiciones iniciales y los parametros del problema.
x=0.0
xAlto=5.0
y=array([0.0,0.0,43.30,25.0])
h=0.01
freq=1

#Resolvemos el sistema de ecuaciones.
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

#Del arreglo original obtenemos la posicion y velocidad.
PosX=Y[:,0]
PosY=Y[:,1]
#Con ello mostramos en pantalla el alcance y tiempo cuando la masa toca el suelo (PosY=0)
for i in range (0,len(X)):
    if (abs(PosY[i])<1e-1 and X[i]>0.1):
        print "\nEl tiempo de vuelo es %1.2f seg" %X[i]
        print "El alcance total es de %1.2f m" %PosX[i]
print "La altura maxima la trayectoria es de %1.2f m" %max(PosY)


#Graficamos la trayectoria de vuelo.
plt.plot (PosX, PosY, "b-", label="Trayectoria")
plt.legend(loc="upper right")
plt.ylabel("Y [m]")
plt.xlabel("X [m]")
plt.plot((0,180),zeros(2),"k--")
plt.show()
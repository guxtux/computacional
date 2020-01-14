# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:31:50 2013

@author: alberto
"""

#Importamos numpy y matplotlib 
import matplotlib.pyplot as plt
from numpy import *

#Definimos la funcion imprimeSoln como vimos en clase.
def imprimeSoln(X,Y,freq):
    def imprimeEncabezado(n):
        print "\n   Tiempo [s]",
        print "   Posicion [m]",
        print "   Velocidad [m/s]",
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
    a=16.0
    g=9.80665
    F[0]=y[1]
    F[1]=g*(1-a*y[0]**3)
    return F

#Establecemos las condiciones iniciales y los parametros del problema.
x=0.0
xAlto=3.0
y=array([0.1,0.0])
h=0.001
freq=100

#Resolvemos el sistema de ecuaciones.
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

#Del arreglo original obtenemos la posicion y velocidad
P=Y[:,0]
V=Y[:,1]

#Implementamos un ciclo para elegir las crestas del movimiento.
Or=[]
Maximo=max(P)
for i in range(0,len(P)):
    if abs(Maximo-P[i])<1e-6:
        z=X[i]
        Or.append(z)
        print "El flotador alcanza la maxima amplitud en %1.3f seg" %z
Periodo=Or[1]-Or[0]
#Estamos tomando el tiempo que tarda el pendulo en completar un movimiento completo y regresar a su punto de partida.
Ampl=(Maximo-0.1)/2.0
print "\n El periodo del flotador es T= %1.3f seg" %Periodo
print " La amplitud de las socilaciones es %1.3f m" %Ampl

#Graficamos la amplitud del movimiento.
plt.plot (X,P, "b-", label="Amplitud")
plt.legend(loc="lower right")
plt.ylabel("Posicion [m]")
plt.xlabel("Tiempo [s]")
plt.plot(X,zeros(len(X)),"k--")
plt.show()
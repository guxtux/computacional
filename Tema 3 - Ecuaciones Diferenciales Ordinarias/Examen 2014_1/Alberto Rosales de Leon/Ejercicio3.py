# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:06:13 2013

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
            print " %13.4e" %y[i],
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

#Escribimos F(x) en terminos de las constantes del problema y de las condiciones iniciales.
def F(x,y):
    F=zeros((2), dtype="float64")
    K=75.0
    M=0.25
    if x>2.0:
        P=20
    else:
        P=10*x
    F[0]=y[1]
    F[1]=(P/M)-(K/M)*y[0]
    return F

#Establecemos las condiciones iniciales y los parametros del problema.
x=0.0
xAlto=5.0
y=array([0.0,0.0])
h=0.01
freq=10

#Resolvemos el sistema de ecuaciones.
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

#Del arreglo original obtenemos la posicion y velocidad.
P=Y[:,0]
V=Y[:,1]
#Calculamos el valor maximo en la amplitud del movimiento.
print "\n El desplazamiento maximo de la masa es %1.3f m" %max(P)

#Graficamos la posicion de la masa respecto al tiempo.
#En la grafica vemos que la amplitud crece con tendencia lineal durante los primeros 2 segundos
#luego comienza un movimiento armonico.
plt.plot (X,P, "b-", label="Amplitud")
plt.legend(loc="lower right")
plt.ylabel("Posicion [m]")
plt.xlabel("Tiempo [s]")
plt.plot(X,zeros(len(X)),"k--")
plt.show()
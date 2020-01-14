# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:43:05 2013

@author: alberto
"""

#Importamos numpy y matplotlib. 
import matplotlib.pyplot as plt
from numpy import *

#Definimos la funcion imprimeSoln como vimos en clase.
def imprimeSoln(X,Y,freq):
    def imprimeEncabezado(n):
        print "\n   Tiempo [s]",
        print "   Ampl [rad]",
        print "   Vel [rad/s]",
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


# Definimos la funcion integra con los respectivos coeficientes del método Runge-Kutta.
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
    g=9.80665
    L=1.0
    A=0.25
    w=2.5
    F[0]=y[1]
    F[1]=-(g/L)*sin(y[0])+(w**2)*(A/L)*cos(y[0])*sin(w*x)
    return F

#Establecemos las condiciones iniciales y los parametros del problema.
x=0.0
xAlto=10.0
y=array([0.0,0.0])
h=0.01
freq=100

#Resolvemos el sistema de ecuaciones.
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

#Del arreglo original obtenemos la posicion y velocidad.
P=Y[:,0]
V=Y[:,1]
#Calculamos la amplitud maxima del movimiento en radianes y grados.
Max=max(P)
MaxGrad=(Max*180.0)/pi
print "\n El desplazamiento maximo es theta= %1.3f rad" %Max
print " El desplazamiento maximo es theta= %1.3f grados" %MaxGrad

#Graficamos la amplitud del movimiento del pendulo.
plt.plot (X,P, "b-", label="Amplitud")
plt.legend(loc="upper right")
plt.ylabel("Posicion [rad]")
plt.xlabel("Tiempo [s]")
plt.plot(X,zeros(len(X)),"k--")
plt.show()
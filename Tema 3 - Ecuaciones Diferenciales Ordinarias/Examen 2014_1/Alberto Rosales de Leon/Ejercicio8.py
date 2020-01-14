# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 01:40:53 2013

@author: alberto
"""

#Importamos numpy y matplotlib 
import matplotlib.pyplot as plt
from numpy import *

#Definimos la funcion imprimeSoln como vimos en clase
def imprimeSoln(X,Y,freq):
    def imprimeEncabezado(n):
        print "\n        x     ",
        print "    Jo [x]  ",
        print "     y [1]  ",
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
    F[1]=-y[1]/x-y[0]
    return F

#Establecemos las condiciones iniciales y los parametros del problema.
x=1e-12
xAlto=6.0
y=array([1.0,0.0])
h=0.01
freq=100

#Resolvemos el sistema de ecuaciones.
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)
#De la tabla tomamos el valor para Jo(5)
print "\n Vemos de la tabla anterior que Jo(5)=-0.17760"

#Definimos los puntos de la funcion de Bessel.
Jo=Y[:,0]

#Graficamos la función de Bessel.
plt.plot (X, Jo, "b-", label="Jo(x)")
plt.plot (5,-0.1769,"ro")
plt.title("Funcion de Bessel")
plt.legend(loc="upper right")
plt.ylabel("Y")
plt.xlabel("X")
plt.plot((0,6),zeros(2),"k--")
plt.show()

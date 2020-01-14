# -*- coding: utf-8 -*-
"""
PROBLEMA 5
Evaluar: Integral de -1 a 1 de: cos(2cos^-1(x))dx
con la regla de 1/3 de Simpson, usando 2,4 y 6 bloques
Explicar los resultados

@author: marisolchavez
"""

from math import *
import numpy as np

def f(x):
    return np.cos(2*np.arccos(x)) 


#Aqui divido el intervalo de -1 a 1 en el numero de bloques n (par)
n=eval(raw_input ("Ingresa el numero n de bloques, (n=2,4,6):"))


x=np.linspace(-1,1,n+1)

h=2.0/n #El valor de h=(b-a)/n = (1-(-1))/n

print "\n         ***Regla de Simpson 1/3***"
if n==2:
    print "\nh=", h
    print "El intervalo -1 a 1 se divide en:\n"
    for i in range (0,n+1):
        print "x",i ,"=", x[i]
    
    y1=(f(x[0])+4*f(x[1])+f(x[2]))*(h/3.0)  #aqui se resuelve para n=2
    print "El valor de la integral para n=4 es: ", y1
    
elif n==4:
    print "\nh=", h
    print "El intervalo -1 a 1 se divide en:\n"
    for i in range (0,n+1):
        print "x",i ,"=", x[i]
        
    y2=(f(x[0])+4*f(x[1])+f(x[2])+f(x[2])+4*f(x[3])+f(x[4]))*(h/3.0)
    print "El valor de la integral para n=4 es: ", y2

elif n==6:
    print "\nh=", h
    print "El intervalo -1 a 1 se divide en:\n"
    for i in range (0,n+1):
        print "x",i ,"=", x[i]

    y3=(f(x[0])+4*f(x[1])+f(x[2])+f(x[2])+4*f(x[3])+f(x[4])+f(x[4])+4*f(x[5])+f(x[6]))*(h/3.0)
    print "El valor de la integral para n=6 es: ", y3
    
else:
    print "Ese numero n no es valido"
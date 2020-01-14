# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 03:08:12 2012

@author: marisolchavez
"""


"""
Ejercicio 5 

Calcular la temperatura en la cual la energía libre de Gibbs es -10^5 J
De nuevo utilice el metodo de Newton-Raphson
"""


#Definimos algunas constantes que se utilizaran

R=8.311441
T0=4.44418

G=-1e5 #esta es la energia que queremos


from math import *
import numpy as np


#La energia libre de Gibbs esta dada por la siguiente funcion:
    #Como queremos saber la temperatura cuando G=-10^5, se incluye G
    
def f(T): return -R*T*np.log((T/T0)**(5.0/2.0))-G 
    
def df(T): return -(5.0/2.0)*R*(1+np.log(T/T0)) # derivada de la funcion
    
 

def newtonRaphson(T,tol=1e-05):
    for i in range(50):
        dT = -f(T)/df(T)
        T=T+dT
        if abs(dT)<tol: return T,i
    print "Son demasiadas iteraciones\n"
    
# Ahora viendo la grafica de -RTln(T/t0)^(5/2) 
# proponemos una T0 cercana a la raiz, es decir una T para cuando G(T)=-10^5J

raiz,numiter = newtonRaphson(900.0) 

print "La temperatura para la cual G=-10^5 es T= ", raiz
print "Numero de iteraciones = ", numiter
   

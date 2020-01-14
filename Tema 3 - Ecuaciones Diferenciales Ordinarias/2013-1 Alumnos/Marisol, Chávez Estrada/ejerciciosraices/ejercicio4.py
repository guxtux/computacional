# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 00:15:12 2012

@author: marisolchavez
"""

"""
Ejercicio 4 

Calcular el tiempo en el cual un cohete alcanza la velocidad del sonido
De nuevo utilice el metodo de Newton-Raphson
"""


#Definimos algunas constantes que se utilizaran

u=2510
M0=2.8e6
dm=13.3e3
g=9.81
v=335 #esta es la velocidad que queremos alcanzar para calcular la t



from math import *
import numpy as np


#La velocidad del cohete esta dada por la siguiente funcion:
    #Como queremos saber el tiempo cuando v=335, se incluye v(t)
    
def f(t): return u*(np.log(M0/(M0-dm*t)))-g*t-v 
    
def df(t): return u*(dm/(M0-dm*t))-g # derivada de la funcion
    

def newtonRaphson(t,tol=1e-05):
    for i in range(50):
        dt = -f(t)/df(t)
        t=t+dt
        if abs(dt)<tol: return t,i
    print "Son demasiadas iteraciones\n"
    
# Ahora viendo la grafica de u*(ln(M0/(M0-dm*t)))-g*t 
# proponemos un t0 cercano a la raiz, es decir un t para cuando y=335

raiz,numiter = newtonRaphson(100.0) 

print "El cohete alcanzara la velocidad del sonido (335 m/s) en el tiempo t= ", raiz
print "Numero de iteraciones = ", numiter
   

# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Feb 26 18:30:31 2013
Examen 1, Ejercicio 2
VALOR DE LA FUNCIÓN EXPONENCIAL DECRECIENTE
"""
from math import *
from decimal import Decimal

error_aceptado=1e-8

def Eabs(x,x_): return abs(x-x_)
    
def e_(x):
    e_x=0.
    k=0
    
    while abs(e_x-exp(-x)) > error_aceptado:
#        parte1 = Decimal(1.0)/factorial(k)        
        e_x=e_x+(-1.)**k*x**k/factorial(k)
        #print k,e_x,abs(e_x-exp(-x))
#        e_x = e_x + (x**k)*parte1
#        print k, parte1       
        k=k+1
    print "e^(-",x,") =",e_x,"en",k,"iteraciones."
        
    return e_x
    
for j in range(-1,3):
    x=10**j
    e_(x)
    
print u"\nNota:\npara x=100, x=1000, el valor fue tan cercano al épsilon absoluto"
print "que no le fue posible a la máquina calcularlo."

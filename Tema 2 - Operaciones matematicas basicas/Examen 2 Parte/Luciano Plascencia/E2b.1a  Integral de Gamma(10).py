# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 11 14:17:04 2013
VALOR DE LA FUNCIÓN 
GAMMA(10)=Integral(t**9*exp(-t)), con t de 0 a Infinito
sin usar cambio de variable, de modo que u=t
"""
from math import *
from varios import *
from integral import *
import scipy.integrate as sci

def f(u): return u**9*exp(-u)
I0=362880
epsilon=1e-15
a=0.
k=0
I=2*I0

while Erel(I0,I)>epsilon:
    k=k+1    
    b=10**k
    n=10*b
    I=simpson(f,a,b,n)
    
print "Valor exacto:                    Gamma(10) = %i" %I0
print "Método de Simpson 1/3 compuesta: Gamma(10) = "+decformat(Eabs(I0,I)) %I
print "Puntos usados en la discretización: %i" %n
print "Límites de integración [a,b] = [%i,%i]" %(a,b)
print "Error absoluto: %.e" %Eabs(I0,I)
print "Error relativo: %.e" %Erel(I0,I)
print "Iteraciones: %i" %k

# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 11 14:17:04 2013
VALOR DE LA FUNCIÓN 
GAMMA(1/2) = Integral(t**(-/2)*e**(-t)), con t de 0 a Infinito
usando el cambio de variable t=u**2, tenemos:
GAMMA(1/2) = Integral(exp(-u**2)), con u de 0 a +Infinito
"""
from math import *
from varios import *
from integral import *
import scipy.integrate as sci

def f(u): return exp(-u**2)
I0=sqrt(pi)
epsilon=1e-15
a=0.
k=0
I=2*I0

while Erel(I0,I)>epsilon:
    k=k+1    
    b=k
    n=100*b
    I=2*simpson(f,a,b,n)

fmt=decformat(Eabs(I0,I))
print "Valor exacto:         Gamma(1/2) = raíz(pi) = "+fmt %I0
print "Método de Simpson 1/3 compuesta: Gamma(1/2) = "+fmt %I
print "Puntos usados en la discretización: %i" %n
print "Límites de integración [a,b] = [%i,%i]" %(a,b)
print "Error absoluto: %.e" %Eabs(I0,I)
print "Error relativo: %.e" %Erel(I0,I)
print "Iteraciones: %i" %k

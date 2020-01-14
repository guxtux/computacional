# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 11 14:17:04 2013
CÁLCULO DE LA INTEGRAL 
I1 = Integral(exp(-x)*log(x)), con x de 0 a Infinito
usando el cambio de variable x=exp(u), tenemos:
I1= Integral(u*exp(u-exp(u))), con u de -Infinito a +Infinito
"""
from math import *
from varios import *
from integral import *
from scipy.integrate import *

def f(u): return u*exp(u-exp(u))
I0=-0.5772156649015328606065
epsilon=1e-7
k=0
I=2*I0

while Erel(I0,I)>epsilon:
    k=k+1
    b=k
    a=-b
    n=2**10
    I=romberg(f,a,b,tol=epsilon)

fmt=decformat(Eabs(I0,I))
print "Valor de referencia: I1 = "+fmt %I0
print "Método de Romberg:   I1 = "+fmt %I
print "Puntos usados en la discretización: %i" %n
print "Límites de integración [a,b] = [%i,%i]" %(a,b)
print "Error absoluto: %.e" %Eabs(I0,I)
print "Error relativo: %.e" %Erel(I0,I)
print "Iteraciones: %i" %k

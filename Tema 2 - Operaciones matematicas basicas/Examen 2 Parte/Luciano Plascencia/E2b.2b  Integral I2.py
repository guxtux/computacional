# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 11 14:17:04 2013
CÁLCULO DE LA INTEGRAL 
I2 = Integral((1+x)/(1-x**3)*log(1/x)), con x de 0 a 1
usando el cambio de variable x=exp(-exp(u)), tenemos:
I2= Integral(exp(2*u-exp(u))*(1+exp(-exp(u)))/(1-exp(-3*exp(u)))),
con u de -Infinito a +Infinito
"""
from math import *
from varios import *
from integral import *
from scipy.integrate import *

def f(u): return exp(2*u-exp(u))*(1+exp(-exp(u)))/(1-exp(-3*exp(u)))
I0=1.46216
epsilon=1e-6
k=0
I=2*I0

while Erel(I0,I)>epsilon:
    k=k+1
    b=k
    a=-b
    n=2**9
    I=romberg(f,a,b,tol=epsilon)

fmt=decformat(Eabs(I0,I))
print "Valor de referencia: I2 = "+fmt %I0
print "Método de Romberg:   I2 = "+fmt %I
print "Puntos usados en la discretización: %i" %n
print "Límites de integración [a,b] = [%i,%i]" %(a,b)
print "Error absoluto: %.e" %Eabs(I0,I)
print "Error relativo: %.e" %Erel(I0,I)
print "Iteraciones: %i" %k

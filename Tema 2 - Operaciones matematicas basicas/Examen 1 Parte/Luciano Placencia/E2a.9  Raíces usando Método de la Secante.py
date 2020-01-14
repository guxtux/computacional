# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 14 18:48:01 2013
CÁLCULO DE RAÍCES CON MÉTODO DE LA SECANTE
Y TOLERANCIA DE 0.001
"""
from math import *
from raices import *
import matplotlib.pyplot as plt
epsilon=0.001

print "CÁLCULO DE RAÍCES POSITIVAS CON MÉTODO DE LA SECANTE"
print "Y TOLERANCIA DE 0.001"

print "\na) f(x) = 0.1*x**3-5*x**2-x+4+exp(-x) = 0"
print "Primero vemos que el polinomio p(x) = 0.1*x**3-5*x**2-x+4 tiene"
print "3 raíces reales:"
#def f(x): return 0.1*x**3-5*x**2-x+4
#(a,b,dx)=(-10,51,0.1)
#x=toda_raiz(f,a,b,dx,epsilon,2,1,2)
print "\n* Como en la parte positiva x>51, domina el polinomio p(x)"
print "pues sobre exp(-x) se pega a 0, no podemos esperar más raíces"
print "de f (x) cuando x --> Infinito."
print "\n* Por otro lado, cuando x es negativa, p(x) --> -Infinito"
print "pero exp(-x) --> +Infinito y domina exp(-x), de modo que"
print "no podemos esperar más raíces de f(x) cuando x --> -Infinito."
print "\n* Por tanto, todas las raíces deben estar no muy lejos del"
print "intervalo (-1,51), donde se encuentran las 3 raíces del polinomio."
print "\nEn efecto, f(x) = p(x) + exp(-x) tiene 4 raíces:"
#
#def f(x): return 0.1*x**3-5*x**2-x+4+exp(-x)
#(a,b,dx)=(-10,60,0.1)
#x=toda_raiz(f,a,b,dx,epsilon,2,1,2)
#
#print "\nb) f(x) = log(x)-0.2*x**2+1 = 0"
#print "Primero vemos que el polinomio p(x) = -0.2*x**2+1 tiene"
#print "2 raíces reales:"
#
#def p(x): return -0.2*x**2+1
#(a,b,dx)=(-3,3,0.1)
#x=toda_raiz(p,a,b,dx,epsilon,2,1,2)
#print "\n* Pero como log(x) no está definido en los reales para x<=0,"
#print "tomaremos dl dominio de f sólo en los reales positivos."
#print "\n* Además, log(x) tiene una raíz en x=1."
#print "\n* Por tanto, es de esperarse que encontremos sólo 2 raíces "
#print "de f(x) en los reales positivos."
#print "\nEn efecto, f(x) = p(x) + exp(-x) tiene 4 raíces:"
#
#def f(x): return log(x)-0.2*x**2+1
#(a,b,dx)=(0.1,5,0.1)
#x=toda_raiz(f,a,b,dx,epsilon,2,1,2)
#
#print "\nc) f(x) = x+1/(x*(x+3)) = 0"
#print "Vemos que f(x) = tiene singularidades en x=-3,x=0."
#print "y sólo tiene una raíz real"
def p(x): return x+1/(x*(x+3))
(a,b,dx)=(-5.05,5.05,0.1)
x=toda_raiz(p,a,b,dx,epsilon,2,1,2)

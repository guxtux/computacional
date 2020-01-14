# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 14 18:48:01 2013
CÁLCULO DE RAÍCES POSITIVAS CON MÉTODO DE BISECCIÓN 
Y TOLERANCIA DE 0.001
"""
from math import *
from raices import *
import matplotlib.pyplot as plt
epsilon=0.001

print "CÁLCULO DE RAÍCES POSITIVAS CON MÉTODO DE BISECCIÓN"
print "Y TOLERANCIA DE 0.001"

print "\na) tan(x)-x+1 = 0,  0 < x < 3*pi"
print "tiene 5 raíces:"
def f(x): return tan(x)-x+1
(a,b,dx)=(0,3*pi,epsilon/10)
x=toda_raiz(f,a,b,dx,epsilon,1,1)

print "\nb) sin(x)-0.3*exp(x) = 0,  x > 0"
print "tiene sólo 2 raíces positivas, como se puede ver en la gráfica."
print "para valores mayores de x la función no vuelve a subir,"
print "pues el valor del término exponencial negativo es mucho mayor"
print "que el término del seno positivo."
def f(x): return sin(x)-0.3*exp(x)
(a,b,dx)=(0,2.5,0.1)
x=toda_raiz(f,a,b,dx,epsilon,1,1)

print "\nc) x**3+x+1"
print "es un polinomio que tiene una sola raíz real, como se puede"
print "ver en la gráfica.  Las otras dos raíces son imaginarias."
def f(x): return -x**3+x+1
(a,b,dx)=(-2,2,0.1)
x=toda_raiz(f,a,b,dx,epsilon,1,1)

print "\nd) 16*x**5-20*x**3+x**2+5*x-0.5"
print "es un polinomio con 5 raíces reales, de las cuales sólo"
print "las tres últimas son positivas:"
def f(x): return 16*x**5-20*x**3+x**2+5*x-0.5
(a,b,dx)=(-1.1,1.1,0.1)
x=toda_raiz(f,a,b,dx,epsilon,1,1)

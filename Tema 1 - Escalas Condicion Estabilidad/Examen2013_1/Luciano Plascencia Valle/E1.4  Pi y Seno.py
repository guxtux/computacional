# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Feb 26 20:30:40 2013
Examen 1, Ejercicio 4
"""
print "CÁLCULO DE PI USANDO POLÍGONOS ITERADOS DE 2**n LADOS"

from math import *

def Eabs(x,x_): return abs(x-x_)
def Erel(x,x_): return abs((x-x_)/x)

#Sea s[n]=Sen(theta[n])
s=[0,0,1]
p=[0,0,2]
print "Seno(theta[n]), p[n], Err. Relativo (p[n] con 4Arctan(1))"
for n in range(3,21):
    s.append(s[n-1]/sqrt(2*(1+sqrt(1-(s[n-1])**2))))
    p.append(2**(n-1)*s[n])
    print n, s[n], p[n], Erel(p[n],4.0*atan(1.0))

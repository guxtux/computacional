# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 03:49:17 2012

@author: emmanuel
"""

"""
La formula de Debye para la capacidad calorífica Cv de un sólido es
Cv=9Nkg(u), donde

g(u)=u³ integral ((x⁴e^x)/(e^x-1)) en (0,1/u)

los términos de la ecuación son:
    N=numero de particulas en el solido
    k=cte de Boltzmann
    u=T/0D
    T=Temperatura absoluta
    0D=Temperatura de Debye
Calcular g(u) para u=0 a 1.0 en intervalos de 0.05, grafica los resultados.
"""

from math import *
from scipy import *
from scipy.integrate import romberg

def f(x): return ((x**4.)*exp(x))/(-1.+exp(x))

u=0.0
while u<=1.0:
    print '-----------------------'
    if u==0:
        g=0.
        print g
    else:
        resultado=romberg(f,0,1/u,show=True)
        g=resultado*(u**3.)
        print g
    print '-----------------------'
    u=u+0.05
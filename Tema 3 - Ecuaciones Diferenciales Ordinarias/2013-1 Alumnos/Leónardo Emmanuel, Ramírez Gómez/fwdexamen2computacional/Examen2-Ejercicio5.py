# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 00:49:34 2012

@author: emmanuel
"""

"""
Evaluar integral de (-1,1) de cos(2*cos⁻¹x)
con la regla de 1/3 de Simpson, usando 2, 4 y 6 bloques.Explicar los resultados.
"""

from math import *

def f(x): return cos(2/cos(x))

a=-1.
b=1.
n=2.
h=(b-a)/n
I=(f(a)+4.*f(a+h)+f(a+2.*h))*h/3.
print 'Para',n,'bloques'
print 'I=',I
print '-----------------'

n=4.
h=(b-a)/n
I=(f(a)+4.*f(a+h)+2.*f(a+2.*h)+4.*f(a+3.*h)+f(a+4.*h))*h/3.
print 'Para',n,'bloques'
print 'I=',I
print '-----------------'

n=6.
h=(b-a)/n
I=(f(a)+4.*f(a+h)+2.*f(a+2*h)+4.*f(a+3*h)+2.*f(a+4*h)+4.*f(a+5*h)+f(6*h))*h/3.
print 'Para',n,'bloques'
print 'I=',I
print '-----------------'

#Al graficar la funcion cos(2/cos(x)), en el intervalo pedido, la función queda
#por debajo del cero, quedando asi los valores negativos, y siendo más
#aproximado el valor para 6 bloques
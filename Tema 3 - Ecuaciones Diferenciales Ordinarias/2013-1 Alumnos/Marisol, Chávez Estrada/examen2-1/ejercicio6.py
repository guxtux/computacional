# -*- coding: utf-8 -*-
"""
PROBLEMA 6

Determina el valor de int (de 1 a inf) (1+x^4)^-1 dx
con la regla del trapecio, suand 5 bloques


@author: marisolchavez
"""

from math import *
import numpy as np


a=0.0
b=1.0
H=b-a

def f(t):
    return 1/((t**(4.0/3.0)) +1.0)

I=((H/16)*(f(a)+2*f(a+H/4.0)+2*f(a+H/2)+2*f(a+3*H/4)+f(b))) + (H/8)*(f(a+H/8)+f(a+3*H/8)+f(a+5*H/8)+f(a+7*H/8))

print "El valor de la integral es:" , I/3.0

valortrap= I/3.0
valorreal=0.24375
#El error entonces es comparando co la integra exacta que es de 0.24375

error= abs(valorreal-valortrap)/valorreal

print "El error es: " , error 
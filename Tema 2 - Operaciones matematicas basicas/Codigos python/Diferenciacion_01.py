# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:57:08 2020

@author: gusto
"""

from ModuloDiferenciacion import seg_derivada_dif_central
from math import exp, fabs

def funcion(x):
    return exp(-x)

def error_relativo(real, aprox):
    return (fabs(real - aprox)/real)*100
    
h = 0.64
x = 1.

print('h \t Segunda derivada \t Error relativo')

for i in range(1, 11):
    aproximacion = seg_derivada_dif_central(funcion, x, h)
    print('{0:} \t {1:} \t {2:1.5e}'.format(h, aproximacion, error_relativo(0.36787944,aproximacion)))
    h = h*0.5
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:23:25 2020

@author: gusto
"""

import numpy.polynomial as npp

def f(t):
    return t**2 + 3


integral = 0

abscisas, pesos = npp.hermite.hermgauss(2)

print('Las abscisas nodales son:')
print(abscisas)

print('\nLos pesos son:')
print(pesos)

for i in range(len(abscisas)):
    integral += pesos[i]*f(abscisas[i])

print('\nEl valor de la integral es = {0:1.10f}'.format(integral))
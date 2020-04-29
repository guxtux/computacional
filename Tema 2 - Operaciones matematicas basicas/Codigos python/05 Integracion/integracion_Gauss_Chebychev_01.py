# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:04:48 2020

@author: gusto
"""

import numpy as np

def pesos(n):
    return np.pi/(n+1)

def abscisas(x, n):
    a = (2*x + 1)* np.pi
    b = 2*n + 2
    xi = np.cos(a/b)
    return xi

def f(x):
    return (1 - x**2)**2

I_exacta = (3*np.pi)/8

n = 2
suma = 0

for i in range(0, n):
    suma += suma + f(abscisas(i, n))

integral = suma * pesos(n)

print('El valor de la integral es = {0:1.16f}'.format(integral))
print('El error relativo es {0:1.5e}'.format((np.abs(I_exacta-integral)/I_exacta)*100))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:25 2020

@author: gustavo
"""

import math

def error_relativo(exacto, aproximado):
    return math.fabs(math.sin(exacto)- aproximado)/math.sin(exacto)*100

x = float(input('Teclea el valor a evaluar: '))


#x = [-1.5, -1, -0.5, 0.5, 1, 1.5]



tolerancia = 1e-8
n = 10


suma = x
term =  x


print('x \t exacta \t   suma \t  error')
for i in range(2, n):
    term = (-term *x*x)/((2*i-1)*(2*i-2))
    suma  = suma + term
    print('{0:} \t {1:1.10f} \t {2:1.10f} \t {3:1.5e}'.format(x, math.sin(x), suma, error_relativo(x, suma)))
    
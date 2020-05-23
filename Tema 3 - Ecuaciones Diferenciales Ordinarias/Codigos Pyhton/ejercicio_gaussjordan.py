# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:00:13 2020

@author: gusto
"""

from modulo_gaussjordan import gaussjordan

a = [[-0.2222, 1.6667, 0, 0, 0],
     [0.3333, -0.2222, 1.6667, 0, 0],
     [0, 0.3333, -0.2222, 1.6667, 0],
     [0, 0, 0.3333, -0.2222, 1.6667],
     [0, 0, 0, 0.3333, -0.2222]]

b = [-0.1111, 0, 0, 0, -0.0117]

X, A = gaussjordan(a, b)

print('La solución es: ')
print(X)
print('La matriz a transformada es: ')
print(A)
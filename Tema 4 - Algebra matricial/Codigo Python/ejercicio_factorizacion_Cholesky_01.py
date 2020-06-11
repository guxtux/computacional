# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:11:11 2020

@author: gusto
"""

import scipy.linalg as sla
import numpy as np
import scipy as sc
import cmath

A = sc.array([[ 1, 1, 1], [1, 2, 2], [1, 2, 3]])

b = sc.array([1., 3./2, 3.])

print('Los valores propios de la matriz A son:\n')
valores = sla.eigvals(A)
positivo = 0
print(valores)


for i in range(len(valores)):
    if valores[i].real <= 0:
        print('La matriz no es definida positiva\n')
    else:
        positivo += 1
    if positivo == len(valores):
        print('La matriz es definida positiva')
        
        
L = sla.cholesky(A, lower=True)

print('\nLa matriz triangular inferior es:\n')
print(L)

print('Se comprueba que L multiplicada por la transpuesta L^T es la matriz A\n')
print(L @ L.T)

c, low = sla.cho_factor(A)

x =  sla.cho_solve((c, low), b)

print('\nEl vector solución es:')
print(x)

print('\nLa comprobación de la solución es:')
print(np.allclose(A @ x - b, np.zeros(3)))
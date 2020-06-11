# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:54:12 2020

@author: gusto
"""

import scipy.linalg as sla
import numpy.linalg as nla
import numpy as np
import scipy as sc


A = sc.array([[-3, 6, -4], [9, -8, 24], [-12, 24, -26]])

b = sc.array([-3, 65, -42])

print('El determinante de la matriz A es = {0:1.6f}'.format(sla.det(A)))

print('\nEl número de condición de la matriz A es = {0:1.6f}'.format(nla.cond(A)))

print('\nLa norma de la matriz A es = {0:1.6f}'.format(sla.norm(A)))

p, l , u = sla.lu(A)

print('La matriz L')
print(l)

print('\nLa matriz U')
print(u)

lu, piv = sla.lu_factor(A)

x = sla.lu_solve((lu, piv), b)

print('\nLa solución al sistema es: ', x)

print('\nComprobación de la solución: ', np.allclose(A @ x - b, np.zeros((3,))))
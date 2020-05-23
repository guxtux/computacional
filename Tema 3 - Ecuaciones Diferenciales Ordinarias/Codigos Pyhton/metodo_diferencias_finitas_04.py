# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:53:02 2020

@author: gusto
"""

import numpy as np


def tamanoh(a, b, N):
    paso = (b - a)/N
    return paso

def espacio_n(a, b, N):
    tn = np.arange(a, b+0.01, h)   
    return tn

def funcionp(t):
    p = -(2.*t)/(1+t**2)
    return p

def funcionq(t):
    q = -2./(1+t**2)
    return q


def coeficientes(h, p, q):
    aij_1 = 1 - (h/2)*p
    aij = q*h**2 - 2
    aij1 = 1 + (h/2)*p
    return aij_1, aij, aij1

a = 0
b = 4
N = 20
f = 1

h = tamanoh(a, b, N)
puntos = espacio_n(a, b, N)

valorp = []
valorq = []
valoraij_1 = []
valoraij = []
valoraij1 = []

for i in range(len(puntos)):
    valorp.append(funcionp(puntos[i]))
    valorq.append(funcionq(puntos[i]))

for i in range(len(puntos)):
    valoraij_1.append(coeficientes(h, valorp[i], valorq[i])[0])
    valoraij.append(coeficientes(h, valorp[i], valorq[i])[1])
    valoraij1.append(coeficientes(h, valorp[i], valorq[i])[2])

    
    

for i in range(1, len(puntos)-1):
    print('{1:1.1f} \t {1:1.2f} \t {2:1.4f} \t {3:1.4f} \t {4:1.4f} \t {5:1.4f} \t {6:1.4f} \t {7:1.4f}'.format(i, \
          puntos[i], valorp[i], valorq[i], valoraij_1[i], valoraij[i], valoraij1[i], \
          f*h**2))

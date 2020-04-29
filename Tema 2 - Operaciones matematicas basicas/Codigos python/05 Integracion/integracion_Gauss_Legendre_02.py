# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:55:33 2020

@author: gusto
"""
import numpy as np
import numpy.polynomial as npp
import scipy.integrate as scpin

puntos, pesos = npp.legendre.leggauss(4)

print(puntos)
print(pesos)

#puntos_chev, pesos_chev = npp.chebyshev.chebgauss(2)
#
#print(puntos_chev)
#print(pesos_chev)

def f(x):
    return (np.sin(x)/x)**2

def cuad_gauss_legendre(n):
    suma = 0
    puntos, pesos = npp.legendre.leggauss(n)
    for i in range(n):
        suma = suma + f(puntos[i])
    
    return suma * pesos[0]
#
integral = cuad_gauss_legendre(4)
#
print(integral)

integral2 = scpin.quadrature(f, 0.0, np.pi)

print(integral2)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:43:56 2020

@author: gusto
"""

import numpy as np

def derivada_adelante_orden_h2(x0, x1, x2, h):
    aproximacion = (-3*x0 + 4*x1 - x2)/(2*h)
    return aproximacion

def derivada_atras_orden_h2(x0, x1, x2, h):
    aproximacion = (3*x0 - 4*x1 + x2)/(2*h)
    return aproximacion

def derivada_adelante_h1(x0, x1, h):
    aproximacion = (x1 - x0)/ (2*h)
    return aproximacion

alfas = np.array([0., 5., 10., 15., 20., 25., 30.])
betas = np.array([1.6595, 1.5434, 1.4186, 1.2925, 1.1712, 1.0585, 0.9561])

h = ((5*np.pi)/180)

velocidades= []

beta_cero = 25*derivada_adelante_orden_h2(betas[0], betas[1], betas[2], h)
velocidades.append(beta_cero)

for i in range(1, len(betas)-1):
    beta = 25*derivada_adelante_h1(betas[i-1], betas[i+1], h)
    velocidades.append(beta)

beta_ultima = 25*derivada_atras_orden_h2(betas[-1], betas[-2], betas[-3], h)
velocidades.append(beta_ultima)

print('alfa \t beta')

for j in range(len(betas)):
    print('{0:2.0f} \t {1:1.6f}'.format(alfas[j], velocidades[j]))




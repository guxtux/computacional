# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:12:05 2020

@author: gusto
"""
import numpy as np
from scipy import integrate

integral, error = integrate.quadrature(np.cos, 0.0, np.pi/2)

print('El valor de la integral es I = {0:1.16f}'.format(integral))
print('\nEl error estimado es {0:1.6e}'.format(error))

# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:45:46 2020

@author: gusto
"""

import numpy as np

datos = np.loadtxt('potencias05.txt', delimiter='\t', skiprows=3)

tiempo = datos[:,0]
velocidad = datos[:,1]

print(tiempo)
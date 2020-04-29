# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:00:01 2020

@author: gusto
"""

def f(t):
    return t**2 + 3

n = 1
abscisas = [-0.707107, 0.707107]
peso = 0.886227
integral = 0

for i in range(len(abscisas)):
    integral += peso*f(abscisas[i])

print('El valor de la integral es = {0:1.10f}'.format(integral))
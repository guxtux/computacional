# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:46:18 2020

@author: gusto
"""
from math import cos, acos

def qSimpson(Func, a, b, n):
   if (n % 2 == 0): n += 1

   h = (b-a)/(n-1)
   s1 = s2 = 0e0
   for i in range(2,n-2,2): s1 += Func(a + i*h)
   for i in range(1,n-1,2): s2 += Func(a + i*h)

   return (h/3)*(Func(a) + 4*s2 + 2*s1 + Func(b))

def f(x):
    return cos(2*acos(x))

for i in range(1, 4):
    print('Para n = {0:} bloques'.format(i*2))
    print('La integral I vale = {0:1.10f}'.format(qSimpson(f, -1., 1., i*2)))
    
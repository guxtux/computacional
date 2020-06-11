# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:48:19 2020

@author: gusto
"""

from scipy import array, linalg, dot

A = array([[8., -6. , 2.],[-4., 11., -7.],[4., -7, 6.]])

P, L, U = linalg.lu(A)

print ('P')
print (P)

print ('L')
print (L)

print ('U')
print (U)

print(dot(L, U))

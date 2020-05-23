# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:47:27 2020

@author: gusto
"""

import numpy as np

def gaussjordan(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    
    #bucle principal
    for k in range(n):
        #pivoteo parcial
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k, n):
                        a[k,j], a[i,j] = a[i,j], a[k,j]
                    b[k], b[i] = b[i], b[k]
                    break
        
        #División en el renglón pivote
        pivote = a[k,k]
        for j in range(k, n):
            a[k,j] /= pivote
        b[k] /= pivote
        
        #bucle de eliminación
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            factor = a[i,k]
            for j in range(k, n):
                a[i,j] -= factor * a[k,j]
            b[i] -= factor * b[k]
    
    return b, a
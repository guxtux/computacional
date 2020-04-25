# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:43:11 2020

@author: gusto
"""
import math
import numpy as np

def gaussNodes(m, tol=10e-9):
    
    def legendre(t, m):
        p0 = 1.0; p1 = t
        for k in range(1, m):
            p = ((2.0*k + 1.0)*t*p1 - k*p0)/(1.0 + k )
            p0 = p1; p1 = p
        
        dp = m*(p0 - t*p1)/(1.0 - t**2)
        
        return p,dp
    
    A = np.zeros(m)
    x = np.zeros(m)
    
    nRoots = int((m + 1)/2) # Number of non-neg. roots
    
    for i in range(nRoots):
        t = math.cos(math.pi*(i + 0.75)/(m + 0.5))# Approx. root
        
        for j in range(30):
            p,dp = legendre(t,m) # Newton-Raphson
            dt = -p/dp; t = t + dt # method
            if abs(dt) < tol:
                x[i] = t; x[m-i-1] = -t
                A[i] = 2.0/(1.0 - t**2)/(dp**2) # Eq.(6.25)
                A[m-i-1] = A[i]
                break
    return x, A


def gaussQuad(f, a, b, m):
    c1 = (b + a)/2.0
    c2 = (b - a)/2.0
    x, A = gaussNodes(m)
    sum = 0.0
    for i in range(len(x)):
        sum = sum + A[i]*f(c1 + c2*x[i])
    
    return c2*sum

def f(x): return (1 - x**2)**(3/2)

a = -1.0
b = 1.0

I_exacta = (3*np.pi)/8

for m in range(2, 12):
    I = gaussQuad(f, a, b, m)
    if math.fabs(I_exacta - I) < 1e-4:
        print('Número de nodos: ', m)
        print('La integral por cuadratura vale I = {0:1.8f}'.format(I))
        break



    
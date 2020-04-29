# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:43:11 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt

def nodosGauss(m, tol=10e-9):
    
    def legendre(t, m):
        p0 = 1.0; p1 = t
        for k in range(1, m):
            p = ((2.0*k + 1.0)*t*p1 - k*p0)/(1.0 + k )
            p0 = p1; p1 = p
        
        dp = m*(p0 - t*p1)/(1.0 - t**2)
        
        return p, dp
    
    A = np.zeros(m)
    x = np.zeros(m)
    
    nRaices = int((m + 1)/2) # Number of non-neg. roots
    
    for i in range(nRaices):
        t = np.cos(np.pi*(i + 0.75)/(m + 0.5))# Approx. root
        
        for j in range(30):
            p, dp = legendre(t,m) # Newton-Raphson
            dt = -p/dp; t = t + dt # method
            if abs(dt) < tol:
                x[i] = t; x[m-i-1] = -t
                A[i] = 2.0/(1.0 - t**2)/(dp**2) # Eq.(6.25)
                A[m-i-1] = A[i]
                break
    return x, A


def quadGauss(f, a, b, m):
    c1 = (b + a)/2.0
    c2 = (b - a)/2.0
    x, A = nodosGauss(m)
    sum = 0.0
    for i in range(len(x)):
        sum = sum + A[i]*f(c1 + c2*x[i])
    
    return c2*sum

def f(x): return (np.sin(x)/x)**2

def error_rel(I_exacta, integral):
    valor = np.abs(I_exacta - integral)/I_exacta
    return valor*100

a = 0.0
b = np.pi
I_exacta = 1.41815
x0 = np.linspace(-b, b, 200)
seccion = np.linspace(0.001, np.pi)

for m in range(2, 12):
    I = quadGauss(f, a, b, m)
    if np.abs(I_exacta - I) < 1e-5:
        print()
        print('Número de nodos: ', m)
        print('La integral por cuadratura vale I = {0:1.8f}'.format(I))
        print('El error relativo es E = {0:1.5e}'.format(error_rel(I_exacta, I)))
        break


plt.plot(x0, f(x0), color='k')
plt.xlim([-np.pi, np.pi])
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.axvline(x=0, lw=0.7, ls='dashed', color='k')
plt.fill_between(seccion, f(seccion))
plt.title('La región sombreada es el valor de la integral buscada')
plt.show()

    
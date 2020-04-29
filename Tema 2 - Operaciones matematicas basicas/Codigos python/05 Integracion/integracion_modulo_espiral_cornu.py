# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:30:13 2020

@author: gusto
"""
import numpy as np
from integracion_Romberg_Beu import qRomberg
import matplotlib.pyplot as plt


def CosF(u): return np.cos(0.5*np.pi*u*u) # integrands of Fresnel integrals
def SinF(u): return np.sin(0.5*np.pi*u*u)


eps = 1e-6 # relative integration precision
xmin = -3.5; xmax = 3.5 # interval
h = 0.05;                                             # plotting mesh spacing
n = int((xmax-xmin)/h) + 1                           # number of upper limits

x0 = np.linspace(xmin, xmax, 200)

x = [0]*(2*n+1); c = [0]*(2*n+1); s = [0]*(2*n+1)


for i in range(1, n+1):
    x[i] = xmin + (i-1)*h; x[i+n] = x[i]                         # upper limit
    c[i] = qRomberg(CosF,0e0,x[i],eps)                     # Fresnel integrals
    s[i] = qRomberg(SinF,0e0,x[i],eps)
    c[i+n] = s[i]



plt.plot(x, c)
#plt.plot(x, s, color='g', label='S')
plt.axhline(y=0, lw=0.7, color='k')
plt.axvline(x=0, lw=0.7, color='k')
plt.legend(loc='best')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.show()
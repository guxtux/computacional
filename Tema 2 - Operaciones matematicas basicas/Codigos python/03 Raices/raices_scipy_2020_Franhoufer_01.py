# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:01:10 2020

@author: gusto
"""

from math import pi, sin, cos
from raices_secante_01 import Secante
from raices_falsaposicion_01 import FalsPos
import matplotlib.pyplot as plt

def Intens(x):                                                    # intensity
   global I0                                              # maximum intensity
   sinc = sin(x)/x if x else 1e0
   return I0 * sinc * sinc
def dIntens(x):                                        # derivative of Intens
   global I0                                              # maximum intensity
   if (x):
      sinc = sin(x)/x
      return 2e0 * I0 * (cos(x) - sinc) * sinc / x
   else: return 0e0
def func(x):                            # function for half-width calculation
   global I0                                              # maximum intensity
   return Intens(x) - 0.5e0 * I0

I0 = 1e0
xmin = -10e0; xmax = 10e0

n = 101
x = [0]*(2*n+1); y = [0]*(2*n+1)

h = (xmax-xmin) / (n-1)
for i in range(1,n+1):
  xi = xmin + (i-1)*h
  x[i  ] = xi; y[i  ] = Intens(xi)
  x[i+n] = xi; y[i+n] = dIntens(xi)


xi = pi/2e0
(raiz, ierr) = Secante(func, 0e0, pi, xi)

print("Ancho medio del pico mayor = {0:8.5f}".format(raiz))


print("\nPosiciones de intensidad máxima:")

h = 0.5e0
a = xmin
while (a < xmax):                                      # root separation loop
   b = a + h                                      # new search interval [a,b]
   (xi, ierr) = FalsPos(dIntens,a,b)
   if ((ierr == 0) and (xi != b) and (Intens(xi) > 1e-10)):
     print("{0:8.5f}  en  ({1:5.2f},{2:5.2f})".format(xi, a, b))
   a = b                                                # shift left boundary



plt.plot(x[1:n], y[1:n], label='$I(x)$')
plt.plot(x[n+1:], y[n+1:], color='red', ls='dashed', lw=0.8, label='$I^{\prime}(x)$')
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.axvline(x=0, lw=0.7, ls='dashed', color='k')
plt.title('Difracción Franhoufer')
plt.legend(loc=1)
plt.xlim([-10, 10])
plt.show()

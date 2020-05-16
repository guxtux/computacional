# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:23:10 2020

@author: gusto
"""
from math import fabs
from Metodos_Directos import EulerCromer1

def Propag(x, y, nx, y0, dy0, Func):
   hx = x[2] - x[1]
   y[1] = y0; dy = dy0
   for m in range(1,nx):
      (y[m+1], dy) = EulerCromer1(x[m], hx, y[m], dy, Func)


def Disparo(x, y, nx, ya, yb, dy1, dy2, eps, Func):
   itmax = 100

   Propag(x, y, nx, ya, dy1, Func)
   f1 = y[nx] - yb
   Propag(x, y, nx, ya, dy2, Func)
   f2 = y[nx] - yb

   if (f1*f2 < 0):
      exist = 1
      for it in range(1,itmax+1):
         dy = 0.5e0*(dy1 + dy2)
         Propag(x, y, nx, ya, dy, Func)
         f = y[nx] - yb
         if (f1*f > 0): dy1 = dy
         else:          dy2 = dy
         if (fabs(f) <= eps): break

      if (it >= itmax): print("Método Disparo: se ha rebasado el número máximo de bisecciones!!")
   else:
      dy = 1e10; exist = 0

   return (dy, exist)
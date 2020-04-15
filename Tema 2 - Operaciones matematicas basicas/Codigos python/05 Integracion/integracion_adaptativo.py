# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:24:46 2020

@author: gusto
"""

from math import fabs

def IAdaptTrapecio(Func, a, b, eps = 1e-6):
   kmax = 30

   h = b - a
   n = 1
   t0 = 0.5*h*(Func(a) + Func(b))

   for k in range(1, kmax+1):
      sumf = 0e0
      for i in range(1, n+1): sumf += Func(a + (i - 0.5)*h)
      t = 0.5*(t0 + h*sumf)
      if (k > 1):
         if (fabs(t-t0) <= eps*fabs(t)): break
         if (fabs(t) <= eps and fabs(t) <= fabs(t-t0)): break
      h *= 0.5; n *= 2
      t0 = t

   if (k >= kmax): print("Se excedieron el número de iteraciones en el método adaptativo !")

   return t
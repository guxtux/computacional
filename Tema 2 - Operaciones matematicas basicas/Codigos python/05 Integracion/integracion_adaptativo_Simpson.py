# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:57:09 2020

@author: gusto
"""
from math import fabs

def qAdaptSimpson(Func, a, b, eps = 1e-6):
   kmax = 30

   h = b-a; n = 1
   s0 = t0 = 0.5*h*(Func(a) + Func(b))

   for k in range(1, kmax+1):
      sumf = 0e0
      for i in range(1, n+1): sumf += Func(a + (i-0.5)*h)
      t = 0.5*(t0 + h*sumf)
      s = (4*t - t0)/3
      if (k > 1):
         if (fabs(s - s0) <= eps*fabs(s)): break
         if (fabs(s) <= eps and fabs(s) <= fabs(s-s0)): break
      h *= 0.5; n *= 2
      s0 = s; t0 = t

   if (k >= kmax): print('Se excedieron el número de iteraciones del método adaptativo de Simpson!')

   return s
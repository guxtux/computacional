# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:46:45 2020

@author: gusto
"""

from math import fabs, exp

def qRomberg(Func, a, b, eps = 1e-6):
   kmax = 30
   r1 = [0]*(kmax + 1)
   r2 = [0]*(kmax + 1)

   h = b-a; n = 1
   r1[0] = 0.5*h*(Func(a) + Func(b))
   for k in range(1,kmax+1):
      sumf = 0e0
      for i in range(1,n+1): sumf += Func(a+(i-0.5)*h)
      r2[0] = 0.5*(r1[0] + h*sumf)
      f = 1e0
      for j in range(1,k+1):
         f *= 4
         r2[j] = (f*r2[j-1] - r1[j-1])/(f-1)

      if (k > 1):
         if (fabs(r2[k]-r1[k-1]) <= eps*fabs(r2[k])): break
         if (fabs(r2[k]) <= eps and fabs(r2[k]) <= fabs(r2[k]-r1[k-1])):break
      h *= 0.5; n *= 2
      for j in range(0,k+1): r1[j] = r2[j]

   if (k >= kmax):
      print("Método de Romberg: Se excedieron las iteraciones !")
      k -= 1

   return r2[k], k
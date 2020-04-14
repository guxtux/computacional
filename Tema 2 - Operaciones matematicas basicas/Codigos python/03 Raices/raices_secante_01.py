# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:13:56 2020

@author: gusto
"""

from math import fabs

def Secante(Func, a, b, x):
#----------------------------------------------------------------------------
#  Determines a real root x of function Func isolated in interval [a,b] by
#  the secant method. x contains on entry an initial approximation.
#  Error code: 0 - normal execution
#              1 - interval does not contain a root
#              2 - max. number of iterations exceeded
#----------------------------------------------------------------------------
   eps = 1e-10                                   # relative precision of root
   itmax = 1000                                      # max. no. of iterations

   x0 = x; f0 = Func(x0)
   x = x0 - f0                                          # first approximation
   for it in range(1,itmax+1):
      f = Func(x)
      df = (f-f0)/(x-x0)                             # approximate derivative
      x0 = x; f0 = f                      # store abscissa and function value
      dx = -f/df if fabs(df) > eps else -f                  # root correction
      x += dx                                             # new approximation
      if ((x < a) or (x > b)): return (x,1)   # [a,b] does not contain a root
      if (fabs(dx) <= eps*fabs(x)): return (x,0)          # check convergence

   print("Se excedió el número máximo de iteraciones!"); return (x,2)
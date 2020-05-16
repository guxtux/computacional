# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:08:51 2020

@author: gusto
"""

def Numerov(E, V, x, y, nx, y0, dy0):
   hx = x[2] - x[1]
   y[1] = y0; dy = dy0

   d2y = 2e0 * (V[1] - E) * y[1]
   dy += hx * d2y
   y[2] = y[1] + hx * dy

   h6 = hx*hx/6e0
   um1 = 1e0 - h6 * (V[1] - E)
   um  = 1e0 - h6 * (V[2] - E)
   for m in range(2,nx):
      up1 = 1e0 - h6 * (V[m+1] - E)
      y[m+1] = ((12e0 - 10e0*um) * y[m] - um1 * y[m-1]) / up1
      um1 = um; um = up1

      if (abs(y[m+1]) > 1e10): break

   return m

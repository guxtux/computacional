# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:56:43 2020

@author: gusto
"""

from math import fabs, exp

def qAdaptTrapecio(Func, a, b, eps = 1e-6):
    
    kmax = 30

    h = b-a; n = 1
    t0 = 0.5*h*(Func(a) + Func(b))

    for k in range(1,kmax+1):
        sumf = 0e0
        for i in range(1,n+1): sumf += Func(a+(i-0.5)*h)
        t = 0.5*(t0 + h*sumf)
        if (k > 1):
            if (fabs(t-t0) <= eps*fabs(t)): break
            if (fabs(t) <= eps and fabs(t) <= fabs(t-t0)): break
        h *= 0.5; n *= 2
        t0 = t

    if (k >= kmax): print("qAdatpTrapecio: Se excedieron el número de iteraciones !")

    return t, k


def qAdaptSimpson(Func, a, b, eps = 1e-6):
   kmax = 30

   h = b-a; n = 1
   s0 = t0 = 0.5*h*(Func(a) + Func(b))

   for k in range(1,kmax+1):
      sumf = 0e0
      for i in range(1,n+1): sumf += Func(a+(i-0.5)*h)
      t = 0.5*(t0 + h*sumf)
      s = (4*t - t0)/3
      if (k > 1):
         if (fabs(s-s0) <= eps*fabs(s)): break
         if (fabs(s) <= eps and fabs(s) <= fabs(s-s0)): break
      h *= 0.5; n *= 2
      s0 = s; t0 = t

   if (k >= kmax): print("qAdaptSimpson: Se excedió el max. de iteraciones!")

   return s, k


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


def error_relativo(aproximacion):
    exacta = 6 - 16*(exp(-1))
    valor = fabs(exacta - aproximacion)/exacta
    return valor*100

def Func(x): return (x*x*x) * exp(-x)


a = 0e0; b = 1e0; eps = 1e-14

I_AdaptTrapecio, i = qAdaptTrapecio(Func,a,b,eps)
I_AdaptSimpson, j = qAdaptSimpson(Func,a,b,eps)
I_Romberg, k = qRomberg(Func,a,b,eps)

print('Método \t\t Integral \t \t Error \t\t Iteraciones')
print('--'*35)
print("Adap. Trapecio \t {0:1.17f} \t {1:1.6e} \t {2:}".format(I_AdaptTrapecio, error_relativo(I_AdaptTrapecio), i))
print("Adap. Simpson \t {0:1.17f} \t {1:1.6e} \t {2:}".format(I_AdaptSimpson, error_relativo(I_AdaptSimpson),j))
print("Romberg \t {0:1.17f} \t {1:1.6e} \t {2:}".format(I_Romberg, error_relativo(I_Romberg), k))


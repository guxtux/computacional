# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:40:58 2020

@author: gusto
"""

from Metodos_Indirectos import Propag, Disparo

#%% Función que evalúa el polinomio de Legrende de orden n

def Legendre(n, x):
   if (n == 0):
      f = 1e0; d = 0e0
   else:
      f = x; fm1 = 1e0
      for i in range(2,n+1):
         fm2 = fm1; fm1 = f
         f = ((2*i-1)*x*fm1 - (i-1)*fm2)/i

      d = n*(x*f-fm1)/(x*x-1e0) if (x*x-1e0) else 0.5*n*(n+1)*f/x

   return (f, d)
#%%
   
#%%
def Func(x, y, dy):
   global n
   return (2e0*x*dy - n*(n+1)*y) / (1e0 - x*x)
#%%

n = 5
xa = 0e0
xb = 1e0; yb = 1e0
eps = 1e-4
hx = 1e-4

nx = int((xb-xa)/hx + 0.5) + 1

x = [0]*(nx+1); y = [0]*(nx+1)

for m in range(1,nx+1): x[m] = xa + (m-1)*hx

if (n % 2 == 0):
   ya = 1e0; dy = 0e0
   Propag(x, y, nx, ya, dy, Func)
   for m in range(1,nx+1): y[m] /= y[nx]
else:
   ya = 0e0
   dy1 = -1e3; dy2 = 1e3
   (dy, exist) = Disparo(x, y, nx, ya, yb, dy1, dy2, eps, Func)
   
salida = open("metododisparo.txt","w")
salida.write("dy = {0:8.5f}\n".format(dy))
salida.write("x \t P{0:1d} \t err\n".format(n))
for m in range(1, nx+1):
   (P, d) = Legendre(n, x[m])
   salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f}\n").format(x[m], y[m], P-y[m]))
salida.close()

print("dy = {0:8.5f}\n".format(dy))
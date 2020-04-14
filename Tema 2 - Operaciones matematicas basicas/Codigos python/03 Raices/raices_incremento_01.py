# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:45:25 2012

@author: IIFCES
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def buscaraiz(f, a, b, dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None#,None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1, x2
            
            
def f(x): return x**3 - 10*x**2 + 5.


        

a, b, dx = (0.0, 1.5, 0.2)

x0 = np.linspace(-2.5, 10.5, 200)

x1, x2 = buscaraiz(f, a, b, dx)

polinomio = [1., -10., 0, 5.]
xp = sp.arange(-2.5, 10.5, 0.02)
y = sp.polyval(polinomio, xp)

# Calculamos las raices del polinomio
raices = sp.roots(polinomio)
print(raices)
# Evaluamos el polinomio en las raices
s = sp.polyval(polinomio, raices)

print('Una raíz está en el intervalo: ({0:1.2f}, {1:1.2f})'.format(x1, x2))

plt.figure(1)
plt.plot(x0, f(x0))
plt.plot(raices, s, 'ro')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.title('Gráfica de la función')
plt.axis([-2.5, 10.5, -150, 100])
plt.text(-1, 10,'$x_{0}$', fontsize=14)
plt.text(1, 10,'$x_{1}$', fontsize=14)
plt.text(9, 10,'$x_{2}$', fontsize=14)

plt.figure(2)
plt.plot(x0, f(x0))
plt.plot(raices, s, 'ro')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.title('Gráfica de la función')
plt.axis([-0.8, 1, -4, 5.5])
plt.text(0.8, 0.5,'$x_{1}$', fontsize=14)

plt.figure(3)
plt.plot(x0, f(x0))
plt.plot(raices, s, 'ro')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0.6, ymin=0., ymax=0.7, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0.8, ymin=0., ymax=0.39, ls='dashed', lw=0.7, color='k')
plt.title('Intervalo en donde se encuentra una raíz')
plt.axis([0.5, 1, -4, 4])


plt.show()

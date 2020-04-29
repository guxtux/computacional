# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:34:13 2020

@author: gusto
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

f = lambda x: np.cos(x)

def f(x):
    return np.cos(x)

def error_relativo(exacta, aprox):
    valor = np.abs(exacta - aprox)/exacta
    return valor*100

exacta = np.sin(np.pi/2)-np.sin(0)

print('Orden \t Integral \t \t Error')
print('--'*25)

for i in range(2):
    integral = integrate.fixed_quad(f, 0.0, np.pi/2, n=i+4)
    print('{0:} \t {1:1.12f} \t {2:1.6e}'.format(i+4, integral[0], error_relativo(exacta, integral[0])))

x0 = np.linspace(0.0, np.pi, 200)
seccion = np.linspace(0.0, np.pi/2)

plt.plot(x0, f(x0), color='k')
plt.fill_between(seccion, f(seccion), color='yellow')
plt.xlim([0, np.pi])
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.title('El área sombreada corresponde a la integral buscada')
plt.text(0.5, 0.5, '$I$', fontsize=18)
plt.text(0.5, -0.5, '$I = \int_{0}^{\pi/2} \cos x \, dx$', fontsize=18)
plt.show()
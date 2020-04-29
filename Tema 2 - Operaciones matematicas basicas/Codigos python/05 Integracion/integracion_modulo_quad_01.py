# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:44:21 2020

@author: gusto
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x2 = lambda x: x**2

def f(x):
    return x**2


x0 = np.linspace(-4.0, 4.0, 200)
seccion = np.linspace(0.0, 4.0)

integral, error = integrate.quad(x2, 0.0, 4.0)

print('La integral vale I = {0:1.10f}'.format(integral))
print('\nEl error en la evaluación es E = {0:1.6e}'.format(error))
#(21.333333333333336, 2.368475785867001e-13)

plt.plot(x0, f(x0))
plt.fill_between(seccion, f(seccion))
plt.title('El área sombreada corresponde al valor de la integral')
plt.xlim([-4, 4])
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.axvline(x=0, lw=0.7, ls='dashed', color='k')
plt.text(3, 4,'$I$', fontsize=16)
plt.text(0.5, 10,'$I = \int_{0}^{4} x^{2} dx$', fontsize=16)
plt.show()
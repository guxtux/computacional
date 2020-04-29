# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:20:41 2020

@author: gusto
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x2 = lambda x: np.sin(x)

def f(x):
    return np.sin(x)


x0 = np.linspace(-np.pi, np.pi, 200)
seccion = np.linspace(0.0, np.pi)

integral = integrate.romberg(x2, 0.0, np.pi, show=1)

plt.plot(x0, f(x0), color='k')
plt.fill_between(seccion, f(seccion))
plt.title('El área sombreada corresponde al valor de la integral')
plt.xlim([-np.pi, np.pi])
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.axvline(x=0, lw=0.7, ls='dashed', color='k')
plt.text(1.5, 0.5,'$I$', fontsize=16)
plt.text(1, -0.5,'$I = \int_{0}^{\pi} \sin x dx$', fontsize=16)
plt.show()
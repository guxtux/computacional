# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:16:12 2020

@author: gusto
"""

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-8., 8., 100)
raices=[-2*np.pi, -np.pi, 0 , np.pi, 2*np.pi]




plt.plot(x, np.sin(x))
plt.plot(raices, np.sin(raices), 'ro')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.title('Raíces de la función seno(x)')
plt.xlim(-8, 8)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:22:11 2020

@author: gusto
"""
import numpy as np
import matplotlib.pyplot as plt

data01 = np.loadtxt('metododisparo.txt', delimiter='\t', skiprows=2)
plt.plot(data01[:,0], data01[:,1], color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Soluciones a la ecuación de legendre con $n=5$')
plt.show()
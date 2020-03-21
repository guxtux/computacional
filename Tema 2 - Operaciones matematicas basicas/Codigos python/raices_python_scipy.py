# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:07:38 2017

@author: Master Chief
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=10)

title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

font = {'fontname':'Comic Sans MS','fontsize':14}

# Creamos un polinomio
polinomio = [1.,-6.4,6.45,20.538,-31.752]   # polinomio = x^4 - 6.4  x^3 + 6.45 x^2 + 20.538 x - 31.752



def p(x):
    y = x**3 - 10 * x**2 + 5
    return y

x = np.linspace(-1,1.5,100)

raiz=sp.optimize.bisect(p, -1, 0)
print(raiz)

plt.plot(raiz,0,'bo', label='raíz estimada')
plt.plot(x,p(x), label='$x^{3} - 10 * x^{2} + 5$')
plt.axhline(y=0, lw=0.7, ls='dashed')
plt.axvline(x=0, lw=0.7, ls='dashed')
plt.axis([-1,1.5,-7.5,6])
plt.title('Se desea calcular las raíces de esta función',**font)
plt.legend(loc=1)
plt.show()
#print(raices)
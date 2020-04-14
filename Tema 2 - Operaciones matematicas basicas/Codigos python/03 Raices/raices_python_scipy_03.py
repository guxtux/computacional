# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:53:20 2017

@author: Master Chief
"""

import scipy
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=10)

title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

font = {'fontname':'Comic Sans MS','fontsize':14}

def f(x):
    y = x + 2*scipy.cos(x)
    return y
         
raiz= scipy.optimize.newton(f,  2)

print(raiz)

x = np.linspace(-5,5)

plt.plot(raiz, 0,'bo', label='Raíz calculada')
plt.plot(x,f(x), label='$x + \cos(x)$')
plt.axhline(y=0, lw=0.7, ls='dashed')
plt.axvline(x=0, lw=0.7, ls='dashed')
plt.title('Función a la que se desea calcular la raíz',**font_prop)
plt.legend(loc=1)
plt.show()
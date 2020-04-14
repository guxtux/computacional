# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:39:58 2017

@author: Master Chief
"""

import scipy as sp                  # Importamos scipy como el alias sp
import matplotlib.pyplot as plt     # Importamos matplotlib.pyplot como el alias plt
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=10)

title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

# Creamos un polinomio
polinomio = [1.,-10,0,5]   # polinomio = x^3 -10 x^2 + 5

# Creamos un array dimensional
x = sp.arange(-4,11,.02)

#  Evaluamos el polinomio en x mediante polyval.
y = sp.polyval(polinomio,x)

# Calculamos las raices del polinomio
raices = sp.roots(polinomio)

# Evaluamos el polinomio en las raices
s = sp.polyval(polinomio,raices)

# Las presentamos en pantalla
print ("Las raíces son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))

# Creamos la figura
plt.figure

# Dibujamos
plt.plot(x,y,'-', label = 'f(x)')

# Fibujamos en la figura anterior
#plt.hold('on')

# Dibujamos
plt.plot(raices, s,'ro', label = 'Raíces del polinomio')

# Etiquetas
plt.xlabel('x', fontname='Courier New')
plt.ylabel('f(x)', fontname='Courier New')
plt.title('Raíz positiva más pequeña del polinomio', **title_font)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
#plt.text(-1.5,0.5,'$x_{0}$', fontsize=14)
plt.text(1,0.5,'$x_{1}$', fontsize=14)
#plt.text(9,0.5,'$x_{2}$', fontsize=14)
plt.axis([-0.5,2,-3,6])
# Leyenda
#plt.legend(loc=9, prop=font_prop)

# Mostramos la figura en pantalla
plt.show()
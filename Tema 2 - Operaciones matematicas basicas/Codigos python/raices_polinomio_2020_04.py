# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:07:10 2020

@author: gusto
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=10)

title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

# Creamos un polinomio
polinomio = [1., -2., -3, 10]

## Creamos un array dimensional
x = sp.arange(-3, 3,.02)
#
##  Evaluamos el polinomio en x mediante polyval.
y = sp.polyval(polinomio, x)
#
## Calculamos las raices del polinomio
#raices = sp.roots(polinomio)
#
## Evaluamos el polinomio en las raices
#s = sp.polyval(polinomio, raices)
#
#print(len(raices))
## Las presentamos en pantalla
#for i in range(len(raices)):
#    #print ("Las raíces son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))
#    print ('Las raíces son %2.3f ' %(raices[i]))
    
x0 = -2.
x1 = 2+1j
x2 = 2-1j

raices = np.array([x0, x1, x2])
print(x1.real, x1.imag)
# Creamos la figura
#plt.figure

# Dibujamos
#plt.plot(x, y,'-', label = 'Función f(x)')

# Fibujamos en la figura anterior
#plt.hold('on')

# Dibujamos
fig, ax = plt.subplots()
ax.scatter(raices.real, raices.imag, c='b')
#plt.plot(raices, s,'ro', label = 'Raíces del polinomio')

# Etiquetas
plt.xlabel('Eje real', fontname='Courier New')
plt.ylabel('Eje imaginario', fontname='Courier New')
#plt.ylabel('f(x)', fontname='Courier New')
plt.title('Raíces en el plano de Argand ', **title_font)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.text(-2.1, 0.25,'$x_{0}$', fontsize=14)
plt.text(2.1, 1.25,'$x_{1}$', fontsize=14)
plt.text(2.1, -1.25,'$x_{2}$', fontsize=14)
plt.axis([-3, 3, -3, 3])
# Leyenda

#plt.legend(loc=4, prop=font_prop)

# Mostramos la figura en pantalla
plt.show()
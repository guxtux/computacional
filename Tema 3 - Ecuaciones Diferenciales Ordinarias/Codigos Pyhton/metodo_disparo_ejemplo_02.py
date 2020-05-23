# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:50:05 2020

@author: gusto
"""

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import bisect
import matplotlib.pyplot as plt

def exacta(x):
    return np.cos(np.pi*(x/2.)) + 2 * np.sin(np.pi*(x/2.)) - 1

def F(y, x):
    F = np.zeros((2), dtype='float64')
    F[0] = y[1]
    F[1] = - (np.pi*np.pi)/4.*(y[0] + 1.)
    return F

""" El valor de alfa == 1.0, y como no ajusta para la solucion
hay que modificar ese parametro hasta alcanzar la tolerancia
"""

#y0 = array([0.0, 3.1416])
y0 = np.array([0.0, 1.])
y1 = np.array([0.0, 5.])
#y0 = np.array([0.0, np.pi])
x = np.linspace(0.0, 1.0)




sol_y1 = odeint(F, y0, x)
sol_y2 = odeint(F, y1, x)


#valor = bisect(F(y0, x), 0.5, 0.9)
#print(valor)
###for i in range(len(y1)):
#print ('alfa = {} \t {} \t {}'.format(y0[-1], x[-1], y1[:,0][-1]))
#    
#
#alfa = [1., 1.5, 2., 2.5, 3., 3.5, 4.]
#y_alfa = [-0.363380, -0.045070, 0.273295, 0.591549, 0.909858, 1.228169, 1.546479]
#
#raiz = np.interp(1.0, y_alfa, alfa)
#print(raiz)

#plt.plot(alfa, y_alfa)
#plt.plot(raiz,1.0, 'or')
#plt.xlabel('alfa')
#plt.ylabel(r'$y_{\alpha}(1)$')
##plt.title(r'Graficamos los valores obtenidos con las pruebas de $\alpha$')
#plt.title(r'Con la interpolación tenemos que $\alpha = 3.14159$')
#plt.axhline(y=1, lw=0.75, ls='dashed', color='grey')
#plt.plot



    
plt.plot(x,sol_y1[:,0],'r+', label=r'solución con $\alpha = $' + str(y0[-1]))
plt.plot(x,sol_y2[:,0],'g+', label=r'solución con $\alpha = $' + str(y0[-1]))
plt.plot(x,exacta(x),'b-', label='solución exacta')
plt.xlabel('x')
plt.ylabel('u(x)')
#plt.title('Método de disparo')
plt.title('Las soluciones coinciden')
plt.xlim(0,1)
l = plt.axhline(y=0, color='k', lw=0.75, ls='dashed')
l2 = plt.axhline(y=1, color='r', lw=0.75, ls='dashed')
plt.legend(loc=5)
plt.show()
    
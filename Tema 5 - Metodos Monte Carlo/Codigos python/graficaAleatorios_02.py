# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:24:17 2017

@author: Master Chief
"""

import matplotlib.pyplot as plt
import random
#from pylab import rcParams
#rcParams['figure.figsize'] = 10, 5

def generaazar(muestra, semilla = None):
     
    def arreglo(lista):
        for i in range(muestra):
            nuevoValor = random.random()
            lista.append(nuevoValor)
        return lista
    
    random.seed(semilla)    
    lista1 = []
    lista2 = []
    
    valoresRandomX = arreglo(lista1)
    valoresRandomY = arreglo(lista2)
    
    return valoresRandomX, valoresRandomY



muestra = 500
x1, y1 = generaazar(muestra)
x2, y2 = generaazar(muestra, 500) 


plt.figure(figsize=(8,5))
ax = plt.subplot(111)
ax.plot(x1, y1,'b+', label='seed = hora del sistema')
ax.plot(x2, y2,'r+', label='seed = 500')
plt.legend(loc=1)
#ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad = 0.)
plt.title(u'Secuencia de números aleatorios usando seed')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
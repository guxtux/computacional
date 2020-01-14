# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:45:05 2012

@author: marisolchavez
"""

#Este programa evalua un polinomio mediante el metodo de Horner 

import numpy as np
import matplotlib.pyplot as plt

#Tenemos el polinomio 48+100x+70x^2-20x^3+2x^4
#Los coeficientes del polinomio [a0,a1,a2,a3,a4]

A=[48,100,70,-20,2]
b=A[4]


n=4

x=np.linspace(-4,-1,7) #inicial -4, final -1, intervalo 0.5

#Comienza el metodo de horner
while n >0:
       n=n-1
       b=A[n]+b*x

px=(b)   
#px.append(b)      

#Se imprimen en pantalla los valores para p y P(x):
    
print "*******************************************\n"
print "Los valores para el polinomio 48+100x+70x^2-20x^3+2x^4 evaluado en cada punto son:\n x=",x, "\n p(x)=",px
print "\n*******************************************"



#La grafica de los puntos obtenidos (en azul)
plt.plot(x,px,"bo")

#Y ahora la grafica del polinomio (linea roja)

y=np.linspace(-4,-1,100)
poli=48+y*(100+y*(70+y*(-20+y*2)))

plt.plot(y,poli,"r")

plt.title("Polinomio por el metodo de Horner")
plt.show()

#Como podemos observar en la grafica, los valores aproximados se ajustan bastante bien al polinomio real
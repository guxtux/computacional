# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Feb 26 18:30:31 2013
Examen 1, Ejercicio 3
"""
print "Método de Horner para evaluar el polinomio"
print "P(x)=48+100x+70x²-20x³+2x⁴"
print "en valores de x en el intervalo [-4,-1]\n"

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-4,-0.5,0.5)                 # Valores de x0 para evaluar P(x0)
a=[48,100,70,-20,2]                      # Coeficientes a de P(x)

def P_Horner(x):                         # Bucle del método de Horner
    P_Hor=0
    for n in range(len(a)-1,-1,-1):     
        P_Hor=a[n]+P_Hor*x
    return P_Hor

def P_Directo(x):                        # Bucle del método directo
    P_Dir=0
    for n in range(len(a)-1,-1,-1):
        P_Dir=a[n]*x**n+P_Dir
    return P_Dir

for i in range(len(x)):                 # Evaluación de valores de P(x0)
    print "P(%.2f) =" %x[i],P_Horner(x[i])
    
plt.xlabel("x")
plt.ylabel("P(x)")
plt.plot(x,P_Horner(x))
plt.plot(x,P_Directo(x))
plt.grid()
plt.show()

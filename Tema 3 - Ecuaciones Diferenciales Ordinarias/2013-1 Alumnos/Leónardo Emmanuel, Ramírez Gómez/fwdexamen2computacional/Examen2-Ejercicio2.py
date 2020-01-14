# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 23:25:36 2012

@author: emmanuel
"""

"""
La ecuación de equilibrio quimico en la produccion de metanol a partir de CO y
H2, es:
    E(3-2*E)²/(1-E)³=249.2
donde E es el grado de equilibrio de la reaccion. Determinar E.
"""
import numpy as np
import matplotlib.pyplot as plt

#funcion para calcular las raices de un polinomio
def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2

#Despejando la ecuación para tenerla igualada a cero obtenemos:

def f(E): return 253.2*E**3-759.6*E**2+756.6*E-249.2

a,b,dx=(-5.0,5.0,0.001)
print 'El intervalo es:'
x1,x2=buscaraiz(f,a,b,dx)
print x1,x2
r=(x2+x1)/2.
print 'El grado de equilibrio de la reaccion es aproximadamente: E=',r

#Grafica que muestra el polinomo y el rango en donde está su raíz
t1=np.arange(-10.0,10.0,0.01)
plt.figure(1)
plt.plot(t1,f(t1),'b-')    
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:25:31 2012

@author: emmanuel
"""

from math import *

#Calcula todas las raices reales de sin(x)-0.1*x0

#La función pra encontrar la raíz en un intérvalo
def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2
#Polinomio del que se quiere obtener las raices        
def f(x): return sin(x)-0.1*x

#El intervalo (a,b) va de -10 a 10 ya que gráficando en gnuplot el polinomio es
#observable que sus raices reales estan en este intervalo, además un intérvalo
#muy grande causa error en el programa
a,b,dx=(-10.,10.,0.001)
#ciclo para ir avanzando la sucecion de intervalos hasta completar el (a,b)
while a<b:
    print 'El intervalo es:'
    x1,x2=buscaraiz(f,a,b,dx)
    print '(',x1,',',x2,')'
    xmed=(x1+x2)/2.
#Se hace un promedio para tomar un valor como la raíz
    print 'la raiz aproximada es'
    print xmed
    print '---------------------'
    a=x2
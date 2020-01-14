# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 03:07:41 2012

@author: emmanuel
"""

"""
El periodo de un pendulo simple de longitud L es t=4(L/g*h(0o))**1/2
donde g es la aceleracion debida a la gravedad, 0o representa la amplitud angular
y:
    h(0o)=integral(1/(1-sin²(0o/2)*sin²(0))**1/2)  en (0,pi/2)
Calcular h(15°),h(30°),h(45°), comparar esos valores con h(0)=pi/2
"""
#Importamos las librerias
from math import *
from scipy import *
from scipy.integrate import romberg

#Definimos la función a integrar
def f(x): return (1-sin(t/2)*sin(x))**(-1/2)
t=pi/12.
o=15
while t<=pi/4.0:
    print '------------------------------'
    print 'Para h(',o,'°):'
#Se resuelve la integral por libreria
    resultado=romberg(f,0.0,pi/2.,show=True)
    t=t+pi/12.
    o=o+15
    print '------------------------------'

#comparando con h(0°)=pi/2, los resultados para 15°, 30° y 45° estan por encima
#del valor en 0, solo por aproximadamente 0.145, 0.326 y 0.554, notando que va
#incrementando en un valor casi de 0.18

# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:52:11 2017

@author: Master Chief
"""

import matplotlib.pyplot as plt

def genera(a, semilla, c, m, n):
    x = []

    for i in range (1, n):
       nueva_semilla = (a*semilla + c) % m
       semilla = nueva_semilla
       x.append(nueva_semilla)

    return x

def grafica(arreglo, color, a, m):
    plt.figure()
    plt.plot(arreglo, color+'+')
    plt.title('Secuencia de números aleatorios con a =' + str(a) + ' y m = ' + str(m))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    

d1 = genera(128, 10, 0, 509, 500)

d2 = genera(269, 10, 0, 2048, 500)

grafica(d1, 'b', 128, 509)
grafica(d2, 'r', 269, 2048)



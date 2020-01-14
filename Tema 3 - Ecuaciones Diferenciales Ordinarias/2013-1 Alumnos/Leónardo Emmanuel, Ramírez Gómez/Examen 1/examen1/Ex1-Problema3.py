# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 04:44:31 2012

@author: emmanuel
"""

#Las fuerzas que participan en este problema son la gravedad y la resistiva
# las cuales actuan sólo sobre el eje Y, por tanto tenemos:
#mÿ=mg-kv  o bien  ÿ=-g-kv/m
#cuya solución es: v(t)=(-Ce^-kt/m)+mg/k
#aplicando las condiciones con t=to v=vo
# v(t)=mg/k+(vo-mg/k)e^-k(t-to)/m   (1)

#para la velocidad terminal hacemos t a infinito y obtenemos:
#e^-k(t-to)/m --> 0
#vT=mg/k                            (2)

#Analizando (1) notamos que no hay dependencia directa de la altura que se lanza
#depende enteramente de las propiedades del medio y del objeto

#


import numpy as np
import matplotlib.pyplot as plt
#tomando la masa de la gota como:
m=2. #gramos
g=980 #cm/s²
#tomando valores de k entre 320g/s
a=np.arange(0.0125,0.05,0.00375) 
v1=a*g  #g y g/s  unidades de la v cm/s
#para caida libre, la velocidad esta dada por
#v2=vo+gt
plt.plot(a,v1,'r--')
plt.ylabel('velocidad terminal')
plt.xlabel('valores de m/k con m=2 gramos')
plt.show()

#la linea roja es en medio resistivo, y al aumentar k, m/k disminuye, y la
#velocidad terminal que alcanza es menor; mientras que al disminuir k, aumenta
#m/k, aumentando tambien el valor de la velocidad terminal que alcanza

#sin embargo en el vacio no se alcanza una velocidad terminal ya que la
#aceleración no llega a cero.
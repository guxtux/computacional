# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:23:17 2012

@author: marisolchavez
"""
from math import *
import matplotlib.pyplot as plt

#Programa de una gota que cae en un cmpo gravitacional con fuerza resistiva
#Se varia k desde 1 hasta 10, y se corre el programa para un tiempo de 0 a 1000
#Se anexa un archivo con el analisis teorico

#masa de la gota constante m=1
m=1.0
g=9.8

k=1.0
v=0.0
x=0.0

#la velocidad de la gota al tiempo t es:
    #v=(m*g/k)*(1.0-exp(-k*t/m))

#La posicion de la gota al tiempo t es:
    #x=((m*g/k)*(t+(m/k)*exp(-k*t/m)))-((g*m**2)/(k**2))


#Se genera un archivo de datos llamado datosgota donde se registran:
#las posiciones y veocidades finales para todos los valores de k

miarchivo = open("datosterminalesgota.dat", "w")

for k in range (1,11):

    for t in range (0,1000):
    
        v = v + (m*g/k)*(1.0-exp(-k*t/m))
        x = x + ((m*g/k)*(t+(m/k)*exp(-k*t/m)))-((g*m**2)/(k**2))
        
    print "\n Para k = ",k,"\n La altura final (t=1000) es= ", x, "\n La velocidad terminal (t=1000) es = ", v,
    
    miarchivo.write("%2d %3d %4d  \n" %(k,x,v))
    
    
#Aqui intente hacer las graficas pero no me salieron, solo me grafica el ultimo valor de x y de v obtenidos    
    
#Grafiquemos la velocidad de la gota contra el tiempo
    
for t in range (0,1000):
    
    plt.plot(t,x, "bo" )
plt.show()

#Grafiquemos la posicion de la gota contra el tiempo

for t in range (0,1000):
    plt.plot(t,v, "r+")
plt.show()
    
    


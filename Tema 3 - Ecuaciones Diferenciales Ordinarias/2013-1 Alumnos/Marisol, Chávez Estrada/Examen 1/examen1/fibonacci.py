# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 05:19:53 2012

@author: marisolchavez
"""

#Este programa calcula la sucesion de fibonacci mediante dos metodos: 
    # 1.-Usando una relacion de recurrencia
    # 2.-Usando una fórmula
    
    
from math import*

#METODO 1- Relacion de recurrencia

n = 50 # El poblema pide que se calculen los primero 50 terminos

print "*************"
print "Los primeros", n, "terminos (usando la relacion de recurrencia) de la serie son:"

serie = [1,1] #los primeros numeros

for k in range(2,n):
    (a,b) = serie[-2:]
    serie.append(a+b)
print serie

#METODO 2 - Formula

print "*************"
print "Ahora usando la fórmula:"

lambda1=1
lambda2=1


raiz=sqrt(5.0)

print lambda1
print lambda2

for i in range (3,50):
       
    termino=(1.0/raiz)*((1./2)*((1.0+raiz)**i)-((1./2)*(1.0-raiz)**i))

    print termino 
    
#Aqui no entiendo como es que debe funcionar la formula, por que los valores calculados
#no se acercan a los valores reales de la serie, ademas esa formula da lugar a 
#que los valores calculados sean de tipo real, lo que no conviene pues la serie
#esta formada por enteros.
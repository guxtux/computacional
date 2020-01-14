# -*- coding: utf-8 -*-

print '-Programa orbitas Halley-'
from math import * 

#definimos las constantes
G=6.67*10**-11
M=2*10**30
e=0.967
d=5280000000000

#ro es calculada con los valores en el afelio
#mediante la ecuación l²/Ma
#l=momento angular
#M=masa efectiva
#a=Gm¹m²
ro=174694250334.129417703

T=2.396736*10**9
t=0

# Numero de vueltas a la orbita
n=eval(raw_input('de el número de vueltas'))
print 'posiciones cada 0.05pi'
#El ciclo variando angulos y encontrar la posición r.
while t<=(n*pi):
    
    #ecuación solución para la orbita
    r=ro/(1+e*cos(t*pi))
    t=t+0.05
    print r

#a)las dimensiones adecuadas para calculos en el programa es las estandar m,s,Kg
#sin embargo en cuestiones numericas y para tener un error menor es mejor usar
#algunas como unidades astronomicas, años, etc.

t=pi*1.
error=ro/(1+e*cos(t))-d
print 'error es aprox',error

#b)El error de la funcion evaluada comparada al valor que debe dar en el afelio
#es muy grande, del orden de 10¹⁰. El error de periodo es apreciable solo en valores muy grandes de vueltas.
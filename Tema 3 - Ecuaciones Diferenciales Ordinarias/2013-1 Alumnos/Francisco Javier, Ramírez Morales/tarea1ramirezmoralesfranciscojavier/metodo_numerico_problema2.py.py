# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 16:15:23 2012

@author: vaio 
"""
from math import *

# ((g/k) + v0y)*(R/v0x)+(g/(k*k))*log(1.0-(R*k/v0x))

def f(R):
    return 














ec=raw_input('introduce la ecuacion trascendente')

# ec=((g/k)+v0y)*(x/v0x)+(g/k*K)log(1-(k/v0x)*x)
 
#Pedimos los extremos
#input produce un número
#el float se asegura de conseguir un numero de punto flotante
#aunque se proporcione un entero
x1=float(input('de el extremo inferior del intervalo aproximado: '))
x2=float(input('de el extremo superior del intervalo aproximado: '))
errordeseado=input('De el error deseado: ')#Establecemos el error deseado
 
#Definimos una funcion f con un argumento x
#eval es un enunciado que produce código python a partir de una cadena
#entonces return eval(ec) devuelve el resultado de evaluar el string
#se proporcionó "ec"
def f(x):
    return  eval(ec)

#Iniciamos un ciclo while
 
while True:
    xmed=(x1+x2)/2#calculamos el punto medio entre x1 y x2
    fxmed=f(xmed)#y en xmed
    if fxmed==0.0:#si fxmed es 0 pues es porque esta es la raiz
        break#salimos del while
 
    if (f(x1)*f(xmed))<0:#si es negativo entonces la raiz esta entre x1 y xmed
        x1=x1#actualizamos los valores
        x2=xmed
    else:#si es positivo, entonces esta entre xmed y x2
        x1=xmed#actualizamos los valores
        x2=x2
    error=abs(x2-x1)#el error es la diferencia entre x2 y x1 (valor absoluto)
    if error<errordeseado:#si el error es menor que el deseado,
        break#salimos del while
 
#imprimimos el resultado
print 'La raíz es',xmed
# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/est5/.spyder2/.temp.py
"""
from math import *

n=eval(raw_input('ingrese el número de iteraciones, n:'))
x=eval(raw_input('ingrese el valor, x:'))
i=1
j=0
suma=1.0

#def fact(x):                #se define la función factorial
   # while i<j:
   #     x=x*(x-1)
    #    i=i+1

for j in range(n):
     suma=suma + (x**j)/factorial(j)   #como se define en el examen, esta serie es alrededor de 0,
     j=j+1                             #no funciona muy bien para valores lejanos de este
     
emio=suma -1
print 'el número exp(x) es:', emio

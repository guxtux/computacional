# -*- coding: utf-8 -*-
 
n= float(raw_input('cual es el valor de x: '))
for i in range(1 , 1000):
    n =n + ((1 - (1/n))**n)
print n

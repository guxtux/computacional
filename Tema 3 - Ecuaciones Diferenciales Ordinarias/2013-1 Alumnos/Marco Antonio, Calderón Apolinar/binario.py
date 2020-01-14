# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:19:40 2012

@author: Calderon Apolinar Marco A
"""
a=[]
b=[]
x=eval(raw_input("dame un valor: "))
y=x//2       #obtiene la parte entera de la division
z=(x%2)//1   #obtiene el residuo entero
a.append(z)
a.append(1)
while y!=1:
    y=y//2
    z=y%2
    a.append(z)
a.append(1)
w=x-(x//1)   #obtiene la parte decimal
r=w*2        #multiplica por 2 la parte decimal
b.append(int(r))
r=r*2
b.append(int(r))
print a
print b
# Fibonacci 2 metodos
"""
Created on Sat Sep  8 23:40:07 2012

@author: Calderon Apolinar Marco A
"""

# Calculo de la serie con el primer metodo
A=[1]
a,b=0,1
while b<5000000000 :
    a,b=b,a+b
    A.append(b)
print A

# Calculo de la serie con el segundo metodo
from math import sqrt
b=sqrt(5)
a=[1,1]
for n in range(3,50):
   x=((0.5*(1+b))**n-(0.5*(1-b))**n)/b
   a.append(x)
print a
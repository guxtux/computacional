# -*- coding: utf-8 -*-

print 'Programa Constantes'

from math import*

print 'pi='
p=4.0
n=1.0
#ciclo para la sumatoria
while n<=1000:
    p+=4.0*((-1)**n/(2*n + 1))
    n+=1
    print p
#para el error comparando al ultimo termino
a=abs(pi-3.14259165434)
b=a/pi
e1=b*100
print 'El error relativo de pi es:' ,e1      
   
print 'e='
e=1
i=1.0
#ciclo para sumatoria
while i<20:
    e+=(1.0)/(factorial(i)) 
    i+=1.0
    print e
#calcular el error respecto al ultimo termino
c=abs(e-2.71828182846)
d=c/e
e2=d*100
print 'Error relativo de e', e2

print 'Constante de Euler='
E=0.0
k=1.0
while k<1000:
    E+=((1.0/k)-log(1+(1.0/k)))
    k+=1.0
    print E
f=abs(0.5772156649 - 0.576715581568)
g=f/0.5772156649
e3=g*100
print 'Error relativo de constante de Euler', e3



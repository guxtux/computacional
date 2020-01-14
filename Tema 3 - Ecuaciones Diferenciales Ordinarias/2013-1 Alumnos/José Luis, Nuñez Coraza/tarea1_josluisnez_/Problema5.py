#Ejercicio 5 calculo de e, pi

from math import *

n=input('ingrese el numero de iteraciones, n:')
a=2
i=1
alfa=1
suma=1
gammamia=1

while i<=n:
    alfa= alfa*((a)**0.5)/2
    a=2 + (a)**0.5
    i=i+1
pimio=2/alfa
print 'pi=', pimio

eab= pi- pimio
er=pimio/pi
print 'el error absoluto es:' , eab, ' y el error relativo es:', er
# es el error relativo

j=n

def fact(x):                #se define la funcion factorial
    while j>0:
        x=x*(x-1)
        j=j-1
while i <= n:
     suma=suma + 1/fact(i)
     i=i+1
emio=1+suma
print 'el numero e es:', emio

eab2= e- emio
er2=emio/e
print 'el error absoluto es:' , eab2, ' y el error relativo es:', er2
# es el error relativo

while i <= n:
    gammamia=gammamia + (1/i)
    i=i+1
g=gammamia - log(n)
print 'el numero gamma es:' , g

eab3=0.577215664901- gammamia #gamma=0.577215664901
er3=gammamia/0.577215664901
print 'el error absoluto es:' , eab3, ' y el error relativo es:', er3
# es el error relativo


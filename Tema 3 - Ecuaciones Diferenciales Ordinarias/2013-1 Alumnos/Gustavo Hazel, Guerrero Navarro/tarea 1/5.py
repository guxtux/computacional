#constantes matematicas

from math import *

n=eval(raw_input('ingrese el número de iteraciones, n:'))
a=2
i=1
alfa=1
suma=1
gammamia=1

for i <= n:
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

def fact(x):                #se define la función factorial
    while j>0:
        x=x*(x-1)
        j=j-1

for i <= n:
     suma=suma + 1/fact(i)
     i=i+1
emio=1+suma
print 'el número e es:', emio

eab2= e- emio
er2=emio/e
print 'el error absoluto es:' , eab2, ' y el error relativo es:', er2
# es el error relativo

for i <= n:
    gammamia=gammamia + (1/i)
    i=i+1
g=gammamia - log(n)
print 'el número gamma es:' , g

eab3= gamma- gammamia
er3=gammamia/gamma
print 'el error absoluto es:' , eab3, ' y el error relativo es:', er3
# es el error relativo


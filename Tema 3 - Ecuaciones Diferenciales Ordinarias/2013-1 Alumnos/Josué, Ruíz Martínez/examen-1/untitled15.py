#Josué Ruíz Martínez
#Problema 2
from math import factorial
from math import exp
x=0.0
a=100
b=1.0
n=range(1,100)
for i in n:
	y=factorial(i)
	c=a**i
	x=x+(c/y)
t=b-x
print t	
e=exp(-a)
y=abs(e-t)/e
print e
print y
#El factorial su pudo haber programado pero salian errores al iterar por lo que tuve que mandar a llamarlo.



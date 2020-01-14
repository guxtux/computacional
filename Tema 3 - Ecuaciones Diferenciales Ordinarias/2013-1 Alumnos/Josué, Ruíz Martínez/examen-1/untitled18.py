#Josué Ruíz Martínez
#Problema 5
from math import sqrt
a=sqrt(5)
b=.5
i=range(3,51)
l=1/a
c=b*(1+a)
d=b*(1-a)
for t in i:
	L=l*((c**t)-(d**t))	
	print L
A,B=0,1
while B<L:
    A,B=B,A+B    
    print B
    
    

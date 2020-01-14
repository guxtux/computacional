# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 18:39:05 2012

@author: vaio
"""
#este programa cambia un numero decimal a binario  en doble presicion bajo la norma IEEE 754
a=[]
t=eval(raw_input('introduce la parte entera'))
x=t//2
z=x%2
a.append(z)
while x !=1:
     
     
     x1=x%2
     a.append(x1)
     x=x//2
a.append(1)    
print a 
print ' es la representacion binaria de la parte entera en la forma [(a0),(a1),..(an)] '

b=[]
r=eval(raw_input('dame la parte decimal en la forma .abcdfg...'))
y=r*2
b.append(int(y))
while y !=1:
    y=(y-int(y))*2
    
    b.append(int(y))

print b 
print' es la representacion binaria de la parte decimal en la forma [(a.1),(a.2),(a.3),..,(a.n)]'
print' de esta forma la representacion completa del numero es:'
print' (an)...(a3)(a2)(a1)(a0).(a.1)(a.2)(a.3)...(a.n)'
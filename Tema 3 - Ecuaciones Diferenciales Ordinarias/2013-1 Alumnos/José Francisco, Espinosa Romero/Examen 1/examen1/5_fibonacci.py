# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:22:23 2012

@author: pako
"""

n=eval(raw_input('¿Qué número de Fibonacci deseas?'))
print '\nMétodo de recurrencia'
f,f1,f2,i,j=1,1,1,3,3
print 1,"\n",1
while i<=n:
    f=f1+f2
    f2=f1
    f1=f
    i+=1
    print f
print 'El número de Fibonacci para el término',i-1,'es:',f

print '\nMétodo por fórmula'
print 1,"\n",1
while j<=n:
    r=5**0.5
    a=0.5*(1+r)
    b=0.5*(1-r)
    F=((a**j)-(b**j))/r
    j+=1
    print F
print 'El número de Fibonacci para el término',i-1,'es:',F

# -*- coding: utf-8 -*-

print '-Programa problema 4-'
from math import*
import numpy as np
import matplotlib.pyplot as plt

x = eval(raw_input('Da el valor de x:')) 
f=(1-tanh(x))**-1
print 'la funcion valuada en ese punto es'
print f


def f(t):
    return (1-np.tanh(t))**-1
t1=np.arange(0.0,10000,1)
t2=np.arange(-1,20,0.5)
plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')    
plt.show()

#en la gráfica se observa que para valores mayores a 19 la función
#crece a infinito


n=0
while y!=0:
    y=19.+n(3.*10**-39)
    f=(1-tanh(y))**-1
    print n,f
    n=n+1

#Esta segunda parte marca error para n por lo que a partir de ese multiplo
#ya no esta definida
#No estoy seguro si tarde mucho por que la n es muy grande o si tiene algun error
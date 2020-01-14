# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:19:17 2012

@author: emmanuel
"""


from math import*

#La placa AB de longitud
#R=90 mm
#está girando con velocidad angular constante d0/dt=5000 rev/min
#La posición del pistón C como se muestra. varía con el ángulo 0

def f(x): return 90.*(cos(x)+((2.5**2.)-(sin(x))**2.)**.5)

#Escribe un programa en python que calcule la aceleración angular del pistón en
#0=0°,5°,10°,...,180° mediante diferenciación numérica


#tabla de posiciones, puede omitirse para el fin del programa
x=0.
h=pi/36.
a=[]
while x<=pi:
    y=f(x)
    a.append(y)
    x=x+h
print a
print ' '
print 'Ángulo(pi radianes)','-  ','Aceleración angular'
#para el angulo 0° usamos aproximaciones hacia adelante
x=0.
d2f=(2.*f(x)-5.*f(x+h)+4.*f(x+2.*h)-f(x+3.*h))/h**2.
print x,'              -   ',d2f

#Para los angulos mayores que 0° usamos aproximaciones centrales de orden 2 en O

x=pi*2./36.
while x<=pi*35./36.:
    d2f=(f(x+h)-2*f(x)+f(x-h))/h**2
    print x,'   -   ',d2f
    x=x+h

#para el ultimo angulo usamos aproximaciones hacia atras
x=pi
d2f=(2.*f(x)-5.*f(x-h)+4.*f(x-2.*h)-f(x-3.*h))/h**2.
print x,'   -   ',d2f

# -*- coding: utf-8 -*-
"""
PROBLEMA 7

El periodo de un pendulo simple de longitud L es tau=4sqrt((L/g))*h(theta0)
donde g es la gravedad, theta0 representa la amplitud angular y

h(theta0) =int(0 a pi/2) 1/sqrt(1-sin^2(theta0/2)*sin^2(theta))

Calcular h(15), h(30), h(45), compara esos valores con h(0)=pi/2 (que es el
valoraroximado para pequeñas amplitudes)

@author: marisolchavez
"""

#utilizando Romberg

from scipy import *
from scipy.integrate import romberg

#Convertimos a radianes 15,30,45º

theta00=0
theta01=(15.0*pi)/180.0 #15º
theta02=pi/6.0    #30º
theta03=(45.0*pi)/180.0 #45

#f0 para 0º
def f0(theta): return 1/sqrt(1-((sin(theta00/2.0))**2)*(sin(theta))**2)
resultado0 = romberg(f0,0,pi/2)

#f1 para 15º
def f1(theta): return 1/sqrt(1-((sin(theta01/2.0))**2)*(sin(theta))**2)
resultado1 = romberg(f1,0,pi/2)
#f2 para 30º
def f2(theta): return 1/sqrt(1-((sin(theta02/2.0))**2)*(sin(theta))**2)
resultado2 = romberg(f2,0,pi/2)

#f3 para 45º
def f3(theta): return 1/sqrt(1-((sin(theta03/2.0))**2)*(sin(theta))**2)
resultado3 = romberg(f3,0,pi/2)



print "h(0º)=", resultado0
print "h(15º)=", resultado1
print "h(30º)=", resultado2
print "h(45º)=", resultado3


#Ahora el error

err1=abs(resultado0-resultado1)/resultado0
err2=abs(resultado0-resultado2)/resultado0
err3=abs(resultado0-resultado3)/resultado0

print "el error para 15º es:", err1
print "el error para 30º es:", err2
print "el error para 45º es:", err3
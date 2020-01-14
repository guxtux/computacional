# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:47:09 2012
@author: Luciano Plascencia Valle
"""
from math import sqrt
print "Programa para calcular las soluciones de una ecuación cuadrática ax²+bx+c"
print "con discriminante d=b²-4ac>>0, tomando a=c=1, b=10^n,"
print "usando dos formas distintas de la chicharronera,"
print "y para calcular el error relativo entre ambas \n"

n=input("Escribe el valor de n: ")
a=c=1
b=10**n
d=b*b-4*a*c
print "a =",a,", b =",b,", c = ",c
print "Discriminante d =",d

x1=(-b+sqrt(d))/(2*a)
x2=(-b-sqrt(d))/(2*a)
x3=-(2*c)/(b-sqrt(d))
x4=-(2*c)/(b+sqrt(d))

errorabs14=abs(x1-x4)
errorabs23=abs(x2-x3)
errorrel14=abs((x1-x4)/x4)*100
errorrel23=abs((x2-x3)/x3)*100

print "x4 = %.20f \nx1 = %.20f \nx2 = %.20f\nx3 = %.20f \n" %(x4,x1,x2,x3)
print "Error abs.1,4 = %.2e\nError abs.2,3 = %.2e \n" %(errorabs14, errorabs23)
print "Error rel.1,4 = %.2e\nError rel.2,3 = %.2e \n" %(errorrel14, errorrel23)
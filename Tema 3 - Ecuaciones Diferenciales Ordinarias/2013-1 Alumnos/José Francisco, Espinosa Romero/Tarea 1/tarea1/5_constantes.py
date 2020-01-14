# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:26:58 2012

@author: pako
"""
print "Este programa calcula el valor de las constantes:\n pi,e y Euler con un cierto grado de aproximación\n"
from math import*

NP=eval(raw_input("Error porcentual deseado para la constante pi:"))
print "\nEl valor de pi es: ",pi
P,n,ep= 2.0,1,100
while NP<ep:
    m=4.0*n*n
    P=P*m/(m-1)
    ep = (abs(pi-P))*100/pi
    n+=1
print "El valor calculado para pi es:",P
print "El número de pasos fueron:", n-1
print "El valor del error de pi es :" ,ep, "%\n" #con respecto al ultimo elemento de la aproximación

Ne=eval(raw_input("Error porcentual deseado para la constante e: "))
print "\nEl valor de e es: ", exp(1)
e,i,e2= 1.0,1,100
while Ne<e2:
    e += (1.0)/(factorial(i)) 
    e2 = (abs(exp(1)-e))*100/e
    i += 1
print "El valor calculado para e es:",e
print "El número de pasos fueron:", i-1
print "El valor del error de e es: ", e2,"%\n"

Ng=eval(raw_input("Error porcentual deseado para la constante de Euler es:"))
G,k,g,eg= 0.0,1,0.577215664901532860606,100
print "\nEl valor de la constante de Euler es: ", g
while Ng<eg:
    a = 1.0/k
    G += (a-log(1+a))
    eg = (abs(g-G))*100/g
    k += 1
print "El valor calculado para la constante de Euler es: ", G
print "El número de pasos fueron:", k-1
print "El valor del error de la constante de Euler es: ",eg,"%"
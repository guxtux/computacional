# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 23:58:39 2012

@author: marisolchavez
"""

#Este programa calcula las 4 soluciones para una ecuacion de segundo orden ax^2+bx+c=0

from math import *
import cmath


#Pedimos al usuario que introduzca los valores de a, b y c 

a=eval(raw_input ("Ingresa un valor para a:"))
b=eval(raw_input ("Ingresa un valor para b:"))
c=eval(raw_input ("Ingresa un valor para c:"))


if a==0:
    print "No se puede dividir entre cero, ingresa otro valor para a"
    

#Definimos el discriminante 

discr = ((b*b)-(4*a*c))


# El discrminante determinara si la solucion es real o imaginaria:
    
if discr>=0:
    
    X1 =(-b+sqrt(discr))/2*a
    X2 =(-b-sqrt(discr))/2*a
    X3 =-2*c/(b+sqrt(discr))  
    X4 =-2*c/(b-sqrt(discr))
    
    print "El discriminante es positivo, la solucion será real. Discriminante=", sqrt(discr)
    print "Las soluciones son:"
    print "X1=",X1
    print "X2=",X2
    print "X3=",X3
    print "X4=",X4
    
#Error:
    #Suponiendo que X3 y X4 son una aproximacion a X1 y X2, El error relativo verdadero es:
        
    e1=(abs(X1-X3))/X1
    e2=(abs(X2-X4))/X2

    print "El error cuando se toma el signo positivo es:", e1
    print "El error cuando se toma el signo negativo es:", e2  



    
elif discr<0:
    
    X1c =(-b+cmath.sqrt(discr))/2*a
    X2c =(-b-cmath.sqrt(discr))/2*a
    X3c =-2*c/(b+cmath.sqrt(discr))
    X4c =-2*c/(b-cmath.sqrt(discr))
    
    print "El discriminante es negativo, la solucion será compleja. Discriminante=", cmath.sqrt(discr)
    print "Las soluciones son:"
    print "X1=",X1c
    print "X2=",X2c
    print "X3=",X3c
    print "X4=",X4c
    
    e1c=(abs(X1c-X3c))/X1c
    e2c=(abs(X2c-X4c))/X2c

    print "El error cuando se toma el signo positivo es:", e1c
    print "El error cuando se toma el signo negativo es:", e2c 
    

    
#FIN

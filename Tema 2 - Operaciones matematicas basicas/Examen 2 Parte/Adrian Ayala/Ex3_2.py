# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:08:56 2013

@author: acesimbrote
"""

#Para el primer inciso usé el cambio de variable x=e**u, este cambio 
#genera la integral f(u), la cual ya no cuenta con la sing. en 0.
#En este caso usé el método de trapecios, escogí este método ya que en este
#caso no se requiere tener un control sobre si es par el número de bloques 
#como es el caso del método de Simpson
 
#
#Para la segunda integral no encontré un cambio de variable, entonces lo que 
#hice fue no evaluar en la singularidad, los resultados para n=3,4,5 son los
#que parecen converger a un valor.

#En ambos casos usé wolfram mathematica para integrar, y así comparar mi
#resultado con uno determinado, pero el dicho software me devolvió resultados 
#no numéricos...  


from modromberg import *
from numpy import *
from integracion import *
#from scipy import *
#from scipy.integrate import romberg


def f(u): return u*exp(u)*exp(-exp(u))
def h(x): return (1+x)*-log(x)*1-(x**3)**-1
def g(t): return (1+exp(-exp(t))) * exp(2*t-exp(t))/(1-exp(-3*exp(t)))


n=7
print 'primera integral'
for i in range(n):
    if i==0:
        print '...'
    elif i==1:
        print '...'
    else:
#        print Sim13(f,-100.,100.,i)
        print trapecios(f,-100.,100.,i)



print 'segunda integral'

for i in range(n):
    if i==0:
        print '...'
    elif i==1:
        print '...'
    else:
        print trapecios(h,0.01,0.9,i) + trapecios(h,2.01,100,i)
    


#
#I12=integralsimpson13(f,-100.,100.,3)
#I14=integralsimpson13(f,-100.,100.,4)
#I16=integralsimpson13(f,-100.,100.,6)
#
#I22=integralsimpson13(f,0.,100.,512)
#I24=integralsimpson13(f,0.,100.,512)
#I26=integralsimpson13(f,0.,100.,512)

#
#print I12,I14,I16
#print I22,I24,I26

#I,n=romberg(f,-100,100)
#I1,n1=romberg(g,0.,100.)

#print 'Integral = ', I
#print 'n-bloques = ',n
#
#
#print 'Integral = ', I1
#print 'n-bloques = ',n1
#print sqrt(pi)
#
#Ia=factorial(9)
#Ib=sqrt(pi)
#print Ia
#
#I,n=romberg(f,0.,100.)
#I1,n1=romberg(g,0.,100.)
#
#print 'La función gamma(10), usando Romberg, tiene un valor,',I,'discretizando con',n,'puntos. Y se calculó un error de',abs(Ia-I)
#print 'La función gamma(10), usando Simpson 1/3, tiene un valor,',integralsimpson13(f,0.,100.,512),'Y se calculó un error de',abs(Ia-integralsimpson13(f,0.,100.,512))
#print 'La función gamma(1/2) tiene un valor,',I1,'discretizando con',n1,'puntos. Y se calculó un error de',abs(Ib-I1) 




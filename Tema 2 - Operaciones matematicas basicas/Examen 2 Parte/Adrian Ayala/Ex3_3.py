# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:53:50 2013

@author: acesimbrote
"""

#Para resolver este problema se utilizó el método de trapecios, como tal el
#código no lo puedo aplicar ya que se debe evaluar en una función, de esta manera
#calculé I3 usando la fórmula vista en clase I3=(1/2) I2(f(a+H/4)+f(a +3H/4))H/4



from integracion import *
from modromberg import *
from numpy import *
from secante import secante

secante(-1,2,20,0.005,"(1/2)*(sqrt(x-4*((1/((2-2*sqrt(1+x))/x)**12)-(1/((2-2*sqrt(1+x))/x)**6)))+2*sqrt(x-4*((1/((2/x)**12)-(1/((2/x)**6))) +sqrt(x-4*((1/((2+2*sqrt(1+x))/x)**12)-(1/((2+2*sqrt(1+x))/x)**6))))*((sqrt(x-4*((1/((2-sqrt(1+x)*(2+x))/x)**12)-(1/((2-sqrt(1+x)*(2+x))/x)**6))))+   ")


#def f1(e): return (2/e)*(1-sqrt(1+e)) #a
#def f2(e): return (2/e)*(1+sqrt(1+e)) #b
#def f3(e): return f2(e)-f1(e)         #H=b-a  
#
#def g1(e): return sqrt(e-4*((1/(f1(e))**12)-(1/(f1(e))**6))) #f(a)
#def g2(e): return sqrt(e-4*((1/(f2(e))**12)-(1/(f2(e))**6))) #f(b)
#def g3(e): return 2*sqrt(e-4*((1/(f1(e))**12)-(1/(f1(e))**6)))
  
           
#H=b-a
#ga=150
#
#
#def g(e): return sqrt(e-4*((1/((2/e)*(1-sqrt(1+e)))**12)-(1/((2/e)*(1-sqrt(1+e)))**6)))
#def h(e): return sqrt(e-4*((1/((2/e)*(1+sqrt(1+e)))**12)-(1/((2/e)*(1+sqrt(1+e)))**6)))
#
#
#sqrt(e-4*((1/((2/e)*(1-sqrt(1+e))**12))-(1/((2/e)*(1-sqrt(1+e))**6))))
#def h(e): return sqrt(e-4*((1/(2/e)*(1+sqrt(1+e))**12)-(1/(2/e)*(1+sqrt(1+e))**6)))
#fa= sqrt(e-4*((1/r**12)-(1/r**6)))
#
#z=f(a)


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



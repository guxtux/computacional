# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:50:57 2013

@author: acesimbrote
"""

#En el primer caso, para la función gamma(10) no se utilizó ningún cambio
#de variable, el intervalo de integración se escogió de 0 a 100, ya que más
#allá de 100 los resulados son incorrectos.
#En este ejercicio primero usé Romberg, después comparé con Simpson 1/3 
#usando n el número de bloques que me resultó de Romberg. Este procedimiento
#me dió un valor exacto para a integral.  

#En el segundo inciso para gamma(1/2), se usó el cambio de variable t=u**2
#de esta manera se elimina la singularidad en cero.
#Para este ejercicio usé Romberg, ya que para aplicar Simpson uno debe dar una
#n tal que el error sea mínimo, en este caso Romberg fue más eficiente.



from integracion import *
from modromberg import *
from numpy import *

def f(t): return (t**9)*exp(-t)
def g(t): return 2*exp(-t**2)


Ia=factorial(9)
Ib=sqrt(pi)
print Ia

I,n=romberg(f,0.,100.)
I1,n1=romberg(g,0.,100.)

print 'La función gamma(10), usando Romberg, tiene un valor,',I,'discretizando con',n,'puntos. Y se calculó un error de',abs(Ia-I)
print 'La función gamma(10), usando Simpson 1/3, tiene un valor,',integralsimpson13(f,0.,100.,512),'Y se calculó un error de',abs(Ia-integralsimpson13(f,0.,100.,512))
print 'La función gamma(1/2) tiene un valor,',I1,'discretizando con',n1,'puntos. Y se calculó un error de',abs(Ib-I1) 




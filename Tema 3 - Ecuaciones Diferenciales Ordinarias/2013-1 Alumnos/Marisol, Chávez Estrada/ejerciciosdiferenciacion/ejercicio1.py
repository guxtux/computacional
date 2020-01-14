# -*- coding: utf-8 -*-

"""
EJERCICIO 1

USANDO UNA APROXIMACION POR DIFERENCIAS FINITAS DE ORDEN O(h^2) 
CALCULA f'(2.36) y f''(2.36) A PARTIR DE LOS DATOS X, FX

@author: marisolchavez
"""


x = [2.36, 2.37, 2.38, 2.39]
fx = [0.85866, 0.86289, 0.86710, 0.87129]

h=0.01
"""
DIFERENCIAS

#hacia adelante (la usaremos para x=2.36)

f'(x) = (-f(x+2h) + 4f(x+h) - 3f(x) ) /2h

f''(x) =  (2f(x)-5f(x+h)+4f(x+2h)-f(x+3h) ) /h**2


"""
print "\n"
print "*****************************************************"
print "POR EL METODO DE DIFERENCIAS FINITAS DE ORDEN O(h^2):"
print "*****************************************************\n"
#la primera y segunda derivada en x=2.36 (hacia adelante)

primera_ad = (-fx[2]+4*fx[1]-3*fx[0] )/(2*h)
segunda_ad = (2*fx[0]-5*fx[1]+4*fx[2]-fx[3])/(h**2)

print "La primera derivada para x=2.36 es: f'(2.36)=", primera_ad
print "La segunda derivada para x=2.36 es: f''(2.36)=", segunda_ad
print "\n"


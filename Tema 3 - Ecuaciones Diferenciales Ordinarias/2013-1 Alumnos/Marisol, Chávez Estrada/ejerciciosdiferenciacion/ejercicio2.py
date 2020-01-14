# -*- coding: utf-8 -*-
"""
EJERCICIO 2

DADOS LOS SIGUIENTES DATOS X,FX, CALCULA f''(1) CON LA MAYOR PRECISION POSIBLE

@author: marisolchavez
"""

x = [0.84, 0.92, 1.00, 1.08, 1.16]
fx = [0.431711, 0.398519, 0.367879, 0.339596, 0.312486]




"""
Usamos el metodo de extrapolacion de Richardson con la segunda aproximacion de
diferencias finitas centrales con x=1

DIF CENTRALES O(h^2):
    
f''(x) = (f(x+h) - 2f(x) + f(x-h) ) /h**2

Con x=1

g(0.16) = f(1+0.16) - 2f(1) + f(1-0.16)  /0.16**2
g(0.08) = f(1+0.08) - 2f(1) + f(1-0.08)  /0.08**2


"""

h1=0.16
h2=0.08

print "\n"
print "****************************************************************"
print "POR EL METODO DE EXTRAPOLACION DE RICHARDSON\nCON EL METODO DE DIFERENCIAS FINITAS CENTRALES DE ORDEN O(h^2):"
print "****************************************************************\n"


segunda_cen_h2 = (fx[3]-2*fx[2]+fx[1])/(h2**2)
segunda_cen_h1 = (fx[4]-2*fx[2]+fx[0])/(h1**2)

print "En x=1, g(0.08)=", segunda_cen_h2
print "En x=1, g(0.16)=", segunda_cen_h1

"""
Y ahora
G=2^p*g(h1/2)-g(h1) / 2^p-1

con p=2

"""

G=((4*segunda_cen_h2)-segunda_cen_h1)/3

print "Entonces el valor para f''(1)=G=", G
print "\n"
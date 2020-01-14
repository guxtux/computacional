# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 01:38:25 2012

@author: emmanuel
"""

"""
Determina el valor de integral de (1,infinito) de (1+x⁴)⁻¹
con la regla del trapecio, usando cinco bloques y compara el resultado con la
integral exacta 0.24375.
"""

#Haciendo el cambio de x³=1/t, entonces x⁴=t**-4/3 y dx=(-1/3)*t**-4/3 dt
#La integral queda: -1/(1.+t**(4./3.))*3


#sacamos el 1/3 y lo ponemos al final
def f(t): return 1./(1.+t**(4./3.))

#Al cambiar el intervalo (1,0)a(0,1) eliminamos el signo negativo de la integral
a=0.
b=1.
n=5.
h=(b-a)/n
I=(f(a)+2.*f(a+h)+2.*f(a+2*h)+2.*f(a+3.*h)+2.*f(a+4.*h)+f(a+5.*h))*h/2.

#Introduciomos el 1/3 que sacamos de la integral
It=I/3
print 'Valor de la integral con',n,'bloques I=',It

#comparamos con el valor exacto
Ie=0.24375
print 'Valor exacto',Ie
Dif=abs(It-Ie)
print 'La diferencia del valor exacto es',Dif
Error=100*Dif/Ie
print 'El error es',Error,'%'
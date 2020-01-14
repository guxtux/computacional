# -*- coding: utf-8 -*-
from integral import *
from numpy import *
from grafica import *

def f(t,x=10):
    fx=(t**(x-1))*exp(-t)
    return fx


#como sabemos que esta funcion es positiva para todo t>0
#encuentra el limite en el que se hace pequeña
x=10
while f(x)>.1:
    while f(x)>1:
        while f(x)>10:
            x=x+10
        x=x+1
    x=x+.1

valorreal=362880    
a=0
b=30
n=10
#para mostrar la grafica quitar los comentarios de graffun y muestra
#graffun(f,a,b)
#muestra()
res=trapecios(f,a,b,n)
error=abs(res-valorreal)

tol=1
while error>tol:
    n=n*2
    res=trapecios(f,a,b,n)
    error=abs(res-valorreal)/valorreal

print("No se utiliza ningun cambio de variable")
print("se usan %2.0f puntos para la discretizacio"%(float(n)))
print("Se integra por el metodo del trapecio")
print("gamma(10)=%6.2f con un error(absoluto)=%3.6e respecto al valor conocido"%(res,error))



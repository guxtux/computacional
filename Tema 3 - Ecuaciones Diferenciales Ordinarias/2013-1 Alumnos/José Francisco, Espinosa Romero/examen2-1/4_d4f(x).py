# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:53:20 2012

@author: pako
"""

def d4f(f,x,h):
    d=(12.*f(x+h)+12.*f(x-h)-18.*f(x)-3.*f(x+2.*h)-3.*(x-2.*h))/h**4
    return d
    
"""
La forma de llegar a la fórmula es 
sumar las series de Taylor de f(x+h)+f(x-h)
y despejar f4(x), y como queda un segunda derivada,
se debe tomar de nuevo las diferencias centrales pero de la primer derivada 
y asi llegar a una expresión de la segunda derivada
en términos de la función en los puntos centrales
Para esta derivada de orden mayor,
se necesitan más puntos que para la de segundo orden 
que se poodía obtener con 3 puntos, 
esta necesita 5 puntos
"""

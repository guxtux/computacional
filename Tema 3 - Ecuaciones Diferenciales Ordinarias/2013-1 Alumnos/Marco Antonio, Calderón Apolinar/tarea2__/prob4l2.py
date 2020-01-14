# Problema 4, lista 2, calcular el tiempo en que se alcanza la vel. son.
"""
@author: Calderon Apolinar Marco A
"""
from math import log

# Desplazamos hacia arriba la funcion por 335 m/s

def f(x): return 2510*(log(2.8e6/(2.8e6-13.3e3*x)))-9.81*x-335

def df(x): return 2510*(13.3e3/(2.8e6-13.3e3*x))-9.81

def newtonRaphson(x,tol=1e-05):
    for i in range(100):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
        
    print 'son demasiadas iteraciones\n'
 
# A partir de la grafica damos el rango

raiz, numiter=newtonRaphson(100)
print 'El tiempo en que se alcanza la velocidad del sonido es:',raiz,'seg'
print 'numero de iteraciones=', numiter
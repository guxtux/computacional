# Problema 5,lista 2, energia de Gibbs
"""
@author: Calderon Apolinar Marco A
"""
from math import log

#Desplazamos la funcion por 10**5
def f(x): return -(8.311441)*x*(log((x/4.44418)**(5/2.)))+1.e5

def df(x): return -8.311441*(log((x/4.44418)**5/2.)-5/2.)

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
        
    print 'son demasiadas iteraciones\n'

raiz, numiter=newtonRaphson(900)
print 'La temperatura en que se alcanza la energia -10**5 es:',raiz,'K'
print 'numero de iteraciones=', numiter
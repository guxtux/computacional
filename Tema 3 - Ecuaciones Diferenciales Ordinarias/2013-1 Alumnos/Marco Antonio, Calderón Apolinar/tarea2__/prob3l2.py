# raices sinx-0.1x
"""
@author: Calderon Apolinar Marco A
"""
from math import sin, cos

def f(x): return sin(x)-0.1*x

def df(x): return cos(x)-0.1

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
        
    print 'son demasiadas iteraciones\n'
    
y=[-6,-2,1,2,5,6]
for c in y:
    
  raiz, numiter=newtonRaphson(c)
  print 'Raiz=', raiz
  print 'numero de iteraciones=', numiter
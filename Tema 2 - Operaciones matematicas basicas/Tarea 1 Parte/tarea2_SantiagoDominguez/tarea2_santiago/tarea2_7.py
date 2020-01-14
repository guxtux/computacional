# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:00:13 2013

@author: san
"""

from numpy import sinh,cosh
#Un cable de acero de longitud s esta suspendido. La tension de traccion
#maxima que en el cable, que se produce en los soportes es:
#"Om=O0coshB" donde:
l=77000.0
L=1000.0
s=1100.0
a=l*L
c=a/2
b=2/a
def f(x): return (b*x)*sinh(c/x) - s/L
def df(x): return b*sinh(c/x)-cosh(c/x)*(c/(x**2.0))*(b*x)

def newtonraphson(x,tol=1e-4):
    for i in range(100):
        dx = -f(x) / df(x)
        x = x + dx
        if abs (dx) < tol: return x , i
    print 'Son demasiadas iteraciones \ n'
    
raiz1 , numIter1=newtonraphson(6e7)

max=raiz1*cosh(c/raiz1)


print 'O_0= ' , raiz1
print 'Numero de iteraciones1= ', numIter1
print ' Tracción maxima en el cable = ',max
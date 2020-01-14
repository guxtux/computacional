# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:09:57 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
def f(x): return tan(x)-x+1
def df(x): return 1/(cos(x))**2-1

def newtonraphson(x,tol=1.0e-4):
    for i in range(30):
        dx = -f(x)/df(x) #m=1
#        dx = 2*(-f(x)/df(x))
	x = x + dx
	if abs(dx) < tol: return x,i
    print "muchas iteraciones\n"
raiz,numeroitera = newtonraphson(7.6)
print "raiz=", raiz
print "numero de iteraciones=",numeroitera
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:14:22 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
def f(x): return sin(x)-0.3*exp(x)
def df(x): return cos(x)-0.3*exp(x)

def newtonraphson(x,tol=1.0e-4):
    for i in range(30):
        dx = -f(x)/df(x) #m=1
#        dx = 2*(-f(x)/df(x))
	x = x + dx
	if abs(dx) < tol: return x,i
    print "muchas iteraciones\n"
raiz,numeroitera = newtonraphson(0.2)
print "raiz=", raiz
print "numero de iteraciones=",numeroitera
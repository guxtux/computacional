# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:32:23 2013

@author: san
"""


from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
def f(x): return 16*x**5-20*x**3+x**2+5*x-0.5
def df(x): return 80*x**4-60*x**2+2*x+5

def newtonraphson(x,tol=1.0e-4):
    for i in range(30):
        dx = -f(x)/df(x) #m=1
#        dx = 2*(-f(x)/df(x))
	x = x + dx
	if abs(dx) < tol: return x,i
    print "muchas iteraciones\n"
raiz,numeroitera = newtonraphson(0.7)
print "raiz=", raiz
print "numero de iteraciones=",numeroitera
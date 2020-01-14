# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:42:40 2013

@author: Deivid
"""
from numpy import *
from todo import *

g10=362880.
g5=sqrt(pi)

x=[0.,.5]
def f(t): return (t**9.)*e**-t
#el cambio de variable adecuado es t=u**2
def g(u): return 2*(e**(-u**2))
    
I,n= romberg (f,0.0,100.)
I2,n2= romberg (g,0.0,100.)


print 'a) el cambio de variable usado fue t=u**2'
print 'b) el número de puntos utilizados fue',n
print 'c) el metdo de integracion usado fue: romberg'
print 'd) el valor de las integrales calculadas son: pra x=10:',I,' y para x=1/2',I2
print 'e) el error para gamma(10)=',error(g10,I),' y para gamma(1/2)=',error(I2,g5)
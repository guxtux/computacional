# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:38:51 2013

@author: Deivid
"""

from todo import *
from numpy import *
#from scipy import *
#from scipy.integrate import romberg


def f(u): return u*exp(u)*exp(-exp(u))
def h(x): return (1+x)*-log(x)*1-(x**3)**-1
def g(t): return (1+exp(-exp(t))) * exp(2*t-exp(t))/(1-exp(-3*exp(t)))


n=7
print 'primera integral'
for i in range(n):
    if i==0:
        print '...'
    elif i==1:
        print '...'
    else:

        print trapecio1(f,-100.,100.,i)



print 'segunda integral'

for i in range(n):
    if i==0:
        print '...'
    elif i==1:
        print '...'
    else:
        print trapecio1(h,0.01,0.9,i) + trapecio1(h,2.01,100,i)
    
print 'a) el cambi de variable para la primer integral es x=e**t y para la segunda es x=e**-e**t, ln1/x =ln1−lnx=−lnx'
print 'b)el numero de puntos usados fue',n
print 'c)el metodo de interación fue romberg pues no nos limita a usar n=par'
print 'd)'
print 'e)'

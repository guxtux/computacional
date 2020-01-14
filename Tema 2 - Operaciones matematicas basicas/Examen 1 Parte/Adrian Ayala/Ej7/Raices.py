# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:41:56 2013

@author: acesimbrote
"""

##module raices

def raices(f,a,b,dx):
    x1 = a ; f1 = f(a)
    x2 = a + dx ; f2 = f(x2)
    while f1 * f2 > 0.0:
        if x1 >= b : return None
        x1 = x2 ; f1 = f2
        x2 = x1 + dx ; f2 = f(x2)
    else:
        return x1,x2
#

def bisect(f,x1,x2,switch=0,epsilon=0.0001):
    f1=f(x1)
    if f1 == 0.0: return x1
    f2= f(x2)
    if f2==0.0: return x2
    
    if f1*f2 > 0.0: print 'la raiz no se ha identificado en un inetrvalo'
    
    n=ceil(log(abs(x2-x1)/epsilon)/log(2.0))
    
    for i in arange(n):
        x3 = 0.5*(x1+x2); f3=f(x3)
        if (switch == 0) and (abs(f3)>abs(f1)) and (abs(f3)>abs(f2)):
            return None
        if f3 == 0.0:return x3
        if f2*f3 < 0.0:
            x1 = x3; f1=f3
        else:
            x2 =x3; f2=f3
    return (x1+x2)/2.0
    
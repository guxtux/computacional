# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:02:24 2012

@author: IIFCES
"""
#import numpy as np
from math import ceil, log, tan
import numpy as np

def rootsearch(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2

def bisect(f,x1,x2,switch=0,epsilon=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    
    if f1*f2 > 0.0: print 'La raiz no se ha identificado en un intervalo'

    n = ceil(log(abs(x2 - x1)/epsilon)/log(2.0))

    for i in np.arange(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) \
                        and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0: return x3
        if f2*f3 < 0.0:
            x1 = x3; f1 = f3
        else:
            x2 =x3; f2 = f3
    return (x1 + x2)/2.0

def f(x):return x - tan(x)

a,b,dx = (0., 20.0, 0.01)



print 'Intervalo (x1,x2)   raiz'
while 1:
    x1, x2 = rootsearch(f,a,b,dx)
    if x1 != None:
        a = x2
        root = bisect(f,x1,x2,1)
        if root != None: print '(%2.4f, %2.4f) %2.8f' %(x1, x2, root)
    else:
        print '\nDone'
        break
raw_input('Press return to exit')
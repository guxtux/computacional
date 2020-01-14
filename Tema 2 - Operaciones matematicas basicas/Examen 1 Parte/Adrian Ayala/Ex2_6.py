# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:18:59 2013

@author: acesimbrote
"""

import matplotlib.pyplot as plt
from funciones import *
import numpy as np
from Raices import *
from  math import *
#7.7,4.4
 #0.54,1.07
#1.32
#-0.9,-0.6,0.1,0.55,0.9    
   
def bisect(f,x1,x2,switch,epsilon=0.001):
    f1=f(x1)
    if f1 == 0.0: return x1
    f2= f(x2)
    if f2==0.0: return x2
    
    if f1*f2 > 0.0: print 'la raiz no se ha identificado en un intervalo'
    
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

dx=0.01
a,b=(3.,6.)
a1,b1=(5.,9.)
a2,b2=(0.,0.9)
a3,b3=(1.,2.)
a4,b4=(1.,3)
a5,b5=(-1.,-0.5)
a6,b6=(-0.8,0.)
a7,b7=(0.,1.)
a8,b8=(0.3,0.7)
a9,b9=(0.8,2)

r = bisect(f1,a,b,1)
r1 = bisect(f1,a1,b1,1)
print 'Las raices de tan(x)-x+1 son:', r1,',',r
r2 = bisect(f2,a2,b2,1)
r3 = bisect(f2,a3,b3,1)
print 'Las raices de sin(x) - 0.3*exp(x) son:', r2,',',r3
r4 = bisect(f3,a4,b4,1)
print 'La raiz de -x**3 + x + 1 es:', r4
r5 = bisect(f4,a5,b5,1)
r6 = bisect(f4,a6,b6,1)
r7 = bisect(f4,a7,b7,1)
r8 = bisect(f4,a8,b8,1)
r9 = bisect(f4,a9,b9,1)
print 'Las raices de 16*x**5 -20*x**3 +x**2 +5*x - 0.5 son:',r5,',',r6,',',r7,',',r8,',',r9








# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:45:48 2012

@author: est5
"""

import cmath
cmath.sqrt(-1)
1j
a=eval(raw_input('Ingrese a: '))
b=eval(raw_input('Ingrese b: '))
c=eval(raw_input('Ingrese c: '))
x1=(-b+(b**2-4*a*c)**0.5)/(2.0*a)
x2=(-b-(b**2-4*a*c)**0.5)/(2.0*a)
x11=-2*c/(b+(b**2-4*a*c)**0.5)
x22=-2*c/(b-(b**2-4*a*c)**0.5)
print 'Las raices de la ecuacion 1 son' 
print 'x1=',x1, 'x2=',x2
print 'Las raices de la ecuacion 2 son' 
print 'x1=',x11, 'x2=',x22
E1=abs((x1-x11)/x1*100)
E2=abs((x2-x22)/x2*100)
print 'Los errores son: E1=',E1, 'E2', E2
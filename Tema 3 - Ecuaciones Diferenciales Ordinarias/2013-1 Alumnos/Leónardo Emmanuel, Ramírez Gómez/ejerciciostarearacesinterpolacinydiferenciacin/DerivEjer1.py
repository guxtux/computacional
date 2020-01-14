# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 03:03:46 2012

@author: emmanuel
"""

#usando una aproximacion por diferencias finitas de orden O(h²), calcula
#f'(2.36) y f''(2.36), a partir de los datos:

"""
x       2.36        2.37        2.38        2.39
f(x)    0.85866     0.86289     0.86710     0.87129

"""
#con h=0.01
#las formulas con una aproximacion por diferencias finitas adelante de orden O(h²)
df=(-.86710+4.*.86289-3.*.85866)/(2.*.01)
d2f=(-.87129+4.*.86710-5.*.86289+2.*.85866)/(.01**2.)
print 'df(2.36)=',df
print 'd²f(2.36)=',d2f
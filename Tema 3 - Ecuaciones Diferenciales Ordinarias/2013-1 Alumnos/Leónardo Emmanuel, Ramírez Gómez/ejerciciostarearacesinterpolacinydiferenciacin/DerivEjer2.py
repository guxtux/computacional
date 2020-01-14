# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 03:21:14 2012

@author: emmanuel
"""

#Dados los datos
"""
x       0.84        0.92        1.00        1.08        1.16
f(x)    0.431711    0.398519    0.367879    0.339596    0.312486
"""
#Calcula f''(1)con la mayor precisión posible


#segunda aproximación por diferencias centrales de orden O(h²), con
#h=0.08 y h=0.16

g1=(.339596-2.*.367879+.398519)/(0.08**2.)
g2=(.312486-2.*.367879+.431711)/(0.16**2.)

#usando la extrapolación de Richardson, con p=2
G=((2.**2.)*g1-g2)/((2.**2.)-1.)
print 'h=0.08                  |   h=0.16'
print 'd²f(1.00)=',g1,'  |  ','d²f(1.00)=',g2
print ' '
print 'con mayor precision d²f(1.00)=',G
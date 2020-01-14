# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:37:36 2012
@author: est5
"""
a = eval(raw_input('da el valor de a'))
b = eval(raw_input('da el valor de b'))
c = eval(raw_input('da el valor de c'))
import cmath
dis=(b**2.)-(4.*a*c)

if dis<0:
        if c!=0:
            rc=cmath.sqrt(dis)
            x1=(-2.*c)/(b+rc)
            x2=(-2.*c)/(b-rc)
            print 'las soluciones son: x1=',x1,' x2=',x2
        if c!=0:
            rc=cmath.sqrt(dis)
            y1=(b-rc)/(-2.*a)
            y2=(b+rc)/(-2.*a)
            print 'las soluciones son: x1=',y1,' x2=',y2
            print 'las soluciones son complejas'

else:
    if c!=0:
            x1=(-2.*c)/(b+dis**(.5))
            x2=(-2.*c)/(b-dis**(.5))     
            print 'las soluciones son: x1=',x1,' x2=',x2
    if c!=0:
            y1=(b-dis**(.5))/(-2.*a)
            y2=(b+dis**(.5))/(-2.*a)    
            print 'las soluciones son: x1=',y1,' x2=',y2

er1=100*abs((x1-y1)/x1)
er2=100*abs((x2-y2)/x2)
print 'errores correspondientes',er1,'%','  ',er2,'%'

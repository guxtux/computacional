# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:47:37 2012

@author: pako
"""
import cmath
print "Este programa calcula las raíces de una ecuación cuadrática del tipo ax2 + bx + c = 0"
a=1.0*eval(raw_input("a = "))
b=1.0*eval(raw_input("b = "))
c=1.0*eval(raw_input("c = "))
if a==0:
    x=-c/b
    print "x = ",x
else :
    d=(b**2)-(4*a*c)
    if d<0:
        rc=cmath.sqrt(d)
        x5=(-b+rc)/(2*a)
        x6=(-b-rc)/(2*a)
        x7=(-2*c)/(b+rc)
        x8=(-2*c)/(b-rc)
        print "la ecuación tiene raíces complejas"
        print "x1 = ",x5
        print "x2 = ",x6
        print "x3 = ",x7
        print "x4 = ",x8
        e3=abs((x5-x7)/x5)*100
        e4=abs((x6-x8)/x6)*100
        print "El error relativo entre x1 y x3 es: ",e3,"%"
        print "El error relativo entre x2 y x4 es: ",e4,"%"
    else :
        r=d**0.5
        x1=(-b+r)/(2*a)
        x2=(-b-r)/(2*a)
        x3=(-2*c)/(b+r)
        x4=(-2*c)/(b-r)
        print "x1 = ",x1
        print "x2 = ",x2
        print "x3 = ",x3
        print "x4 = ",x4
        e1=abs((x1-x3)/x1)*100
        e2=abs((x2-x4)/x2)*100
        print "El error relativo entre x1 y x3 es: ",e1,"%"
        print "El error relativo entre x2 y x4 es: ",e2,"%"

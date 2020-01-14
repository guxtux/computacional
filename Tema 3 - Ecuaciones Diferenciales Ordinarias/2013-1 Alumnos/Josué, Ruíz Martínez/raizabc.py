# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 02:42:18 2012

@author: Marco A Calderon Apolinar
"""
miarchivo=open("raiz.dat","w")
a=eval(raw_input("dame el valor de a:"))
b=eval(raw_input("dame el valor de b:"))
c=eval(raw_input("dame el valor de c:"))
if a>0:
  from cmath import sqrt
  t1=(-b-sqrt(b*b-4*a*c))/2*a
  t2=(-b+sqrt(b*b-4*a*c))/2*a
  t3=-2*c/(b-sqrt(b**2-4*a*c))
  t4=-2*c/(b+sqrt(b**2-4*a*c))
  e1=abs((t1-t3)/t1)
  e2=abs((t2-t4)/t2)
  print "las raices del polinomio son : "
  print t1
  print t2
  print t3
  print t4
  print "el error entre las raices 1 y 3 es %f: " %(e1)
  print "el error entre las raices 2 y 4 es %f: " %(e2)
elif a==0:
    print "no se puede dividir entre cero"
    print "cambia el valor de a"
miarchivo.close()
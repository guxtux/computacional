# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/est5/.spyder2/.temp.py
"""
#sucesión Fibonacci

n=eval(raw_input('ingrese hasta qué número quiere calcular la serie, n:'))
a, b= 0, 1
c=1
while b < n:
    print b
    a, b= b, a+b

print 'va por la otra opción ;)'

for c in range(n):
      d=( ((1 + 5**0.5)/2)**c - ((1 - 5**0.5)/2)**c )/(5**0.5)
      print int(d)
      c=c+1
      

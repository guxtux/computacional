# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:44:07 2012

@author: pako
"""
d=open('2_polinomio.dat','w')
a=-4.0
while a<=-1:
    c = [48,100,70,-20,2]
    r=0
    n=4
    while n>=0: 
        r=c[n]+ a*r
        n=n-1
    print "P(",a,")= ", r
    d.write('%-12f %-12f\n'%(a,r))
    a=a+0.5

d.close()

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:19:27 2012

@author: est5
"""

a=eval(raw_input('da el numero a convertir a binario'))
print 'el numero binario en sentido inverso es:'
if a<0:
    print '1 - signo'
if a>0:
    print '0 - signo'
b=a-(a//1)
while a>1:
    p=a/2.
    q=a//2
    r=p-q
#    print p,q,r
    if r>0 :
        print '1'
    elif r==0 :
        print '0'
    if q==0:
        print '1'
    a=q

print 'la parte decimal es:'
#print b
while b!=0:
    s=b*2
    t=s//1
    if t==0:
        print '0'
        s=s
    elif t!=0:
        print '1'
        s=s-1
    b=s
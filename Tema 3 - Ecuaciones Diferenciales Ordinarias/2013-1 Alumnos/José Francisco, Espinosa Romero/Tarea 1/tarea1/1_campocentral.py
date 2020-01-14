# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/tmp/guest-sYRpal/.spyder2/.temp.py
"""
from math import *
g=open('Cometa Halley','w')
s=open('sol','w')
s.write('0.0000000 0.000000')
s.close()

Q=(5.28*10**12)/(1.5*10**11)
G=(6.67*10**-11)/((1.5*10**11)**3)
M=1.99*10**30
k=G*M
V=912/(1.5*10**11)
e=0.96799
a=Q/(1+e)
r0=a*(1-e*e)
e1=1-(V**2)/k
print "La excentricidad calculada fue:",e1,"y la real:",e
w=0.0
while w<8*pi:
    r=(r0)/(1+e*cos(w)) 
    print "(w,r)=(",w,"rad,",r,"UA)"
    g.write('%f %f\n'%(w,r))
    w=w+pi/6
g.close()
P=2*pi*((a**3)/k)**0.5
P=P/(3600*24*365)
print "El periodo del cometa halley es de:",P,"años"